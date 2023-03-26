class Tower:
    def __init__(self):
        self.loc = (210, 230)
        self.range = 100
        self.shots = []
        self.fire_rate = 1000
        self.sprite = pygame.Surface((70,70))
        self.sprite.fill('Orange')
        self.cp = self.calcCenter()
        self.last_shot = -5;
        
    def calcCenter(self):
        return (pygame.Surface.get_width(self.sprite)/2 + self.loc[0], pygame.Surface.get_height(self.sprite)/2 + self.loc[1])
        
    def inRadius(self, enemy):
        return pygame.math.Vector2(self.cp).distance_to(enemy.get_Center()) <= self.range


    def shoot(self, enimies):
        for enemy in enimies:
            if(self.inRadius(enemy) and pygame.time.get_ticks() - self.last_shot >= self.fire_rate):
                print("Adding shot")
                self.shots.append(Projectile(self.calcAngle(enemy), self.cp))
                self.last_shot = pygame.time.get_ticks()
                
    def updateShots(self, scr, enimies):
        self.shoot(enimies)
        for shot in self.shots:
            shot.update()
            shot.draw(scr)
            
         
    def draw(self, scr):
        scr.blit(self.sprite, self.loc)
        
    def calcAngle(self, enemy):
        centp = enemy.get_Center()
        bot = self.cp[0]- centp[0]
        degrs = 0
        top = self.cp[1]-centp[1]
        print("top: ", top)
        print("bot: ", bot) 
        if self.cp[0] > centp[0] and self.cp[1] > centp[1]:
            bot *= -1
        # If path is horizontal
        print("top: ", top)
        print("bot: ", bot)
        if top == 0:
            # To the right
            if self.cp[0] < centp[0]:
                degrs = math.radians(0)
            #To the left
            else:
                degrs = math.radians(180)
        # Else
        
        elif bot == 0:
            if self.cp[1] < centp[1]:
                degrs = math.radians(90)
            #To the left
            else:
                degrs = math.radians(-90)
                
        else:
            degrs = math.atan(top/bot)
        print("Degrees: ", degrs)
        return degrs