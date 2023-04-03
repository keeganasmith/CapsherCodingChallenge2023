import pygame
import Projectile
import math
class Tower:
    def __init__(self, x_coord = 210, y_coord = 230, center_coord = [-1, -1], height = 70, width = 70, color = 'Orange', firerate = 900, cost = 75):
        self.surface = pygame.Surface((height,width))
        self.surface.fill(color)
        if(center_coord != [-1, -1]):
            x_coord = center_coord[0] - (width //2);
            y_coord = center_coord[1] - (width //2)

        self.loc = (x_coord, y_coord)
        self.range = 200
        self.shots = []
        self.fire_rate = firerate #higher means slower!!!
        
        self.cp = self.calcCenter()
        self.last_shot = -5;
        self.cost = cost
        self.type = "regular"
    def calcCenter(self):
        return (pygame.Surface.get_width(self.surface)//2 + self.loc[0], pygame.Surface.get_height(self.surface)//2 + self.loc[1])
        
    def inRadius(self, enemy):
        return pygame.math.Vector2(self.cp).distance_to(enemy.get_Center()) <= self.range
    
    def getCost(self):
        return self.cost


    def shoot(self, enimies, projectiles_on_screen = []):
        if(pygame.time.get_ticks() - self.last_shot < self.fire_rate):
            return;
        for enemy in enimies:
            if(self.inRadius(enemy) and pygame.time.get_ticks() - self.last_shot >= self.fire_rate):
                angle_data = self.calcAngle(enemy);
                projectiles_on_screen.append(Projectile.Projectile(angle_data[0], angle_data[1], angle_data[2], self.cp))
                self.last_shot = pygame.time.get_ticks()
                return;
                
    def updateShots(self, scr, enimies):
        self.shoot(enimies)
        for shot in self.shots:
            shot.update()
            shot.draw(scr)
            
    def calcAngle(self, enemy):
        centp = enemy.get_Center()
        bot = abs(self.cp[0]- centp[0])
        degrs = 0
        top = abs(self.cp[1]-centp[1])
        horizontal_coefficient = 1
        vertical_coefficient = 1
        if(top == 0):
            top = .00001
        if(bot == 0):
            bot = .00001
        if(self.cp[0] > centp[0]):
            horizontal_coefficient = -1

        if(self.cp[1] > centp[1]):
            vertical_coefficient = -1
        
        degrs = math.atan(top/bot)
        return [degrs, horizontal_coefficient, vertical_coefficient]
    
    def draw(self, scr):
        scr.blit(self.surface, self.loc)
    
        
class slow_tower(Tower):
    def __init__(self, center_coords = [-1, -1], tower_id = 1):
        super().__init__(color = "Blue", cost = 120, center_coord= center_coords)
        self.type = "slow"
        self.slow_factor = 2
        self.tower_id = tower_id
    def shoot(self, enemies, projectiles_on_screen = []):
        for enemy in enemies:
            if((not enemy.slowed) and self.inRadius(enemy)):
                enemy.speed /= self.slow_factor;
                enemy.slowed = True
                enemy.slow_id = self.tower_id
            elif(enemy.slowed and enemy.slow_id == self.tower_id and not self.inRadius(enemy)):
                enemy.speed *= self.slow_factor;
                enemy.slowed = False

class aoe_tower(Tower):
    def __init__(self, center_coords = [-1, -1]):
        super().__init__(color = "Purple", cost = 135, center_coord = center_coords)
        self.type = "aoe"
        self.range = 150
        self.damage = 1.7;
    def shoot(self, enemies):
        found_enemy = False;
        proj = None;
        for enemy in enemies:
            if((not found_enemy) and self.inRadius(enemy)):
                angle_data = self.calcAngle(enemy)
                proj = Projectile.flame(angle_data[0], angle_data[1],angle_data[2], self.cp)
                found_enemy = True
            if(found_enemy):
                if(proj.hits(enemy)):
                    enemy.health -= self.damage
        return proj
class sniper_tower(Tower):
    def __init__(self, center_coords = [-1, -1], sniper_number = 0):
        super().__init__(color = "Brown", cost = 110, center_coord = center_coords)
        self.type = "sniper"
        self.fire_rate = 1700
        self.range = 1280
        self.sniper_number = sniper_number;
    def shoot(self, enemies, projectiles_on_screen= [], game_counter =0):
        if(pygame.time.get_ticks() - self.last_shot < self.fire_rate):
            return;
        if(len(enemies) == 0):
            return;
        max_health = enemies[0].health
        best_target = enemies[0];
        for enemy in enemies:
            if(enemy.health > max_health):
                best_target = enemy
                max_health = enemy.health
        angle_data = self.calcAngle(best_target)
        projectiles_on_screen.append(Projectile.sniper_bullet(angle_data[0], angle_data[1], angle_data[2], self.cp))
        self.last_shot = pygame.time.get_ticks()


