import pygame
import enemy
def collision_detection(enemy, projectiles):
    enemy_rect = enemy.rect;
    i = 0;
    while(i < len(projectiles)):
        if(enemy_rect.colliderect(projectiles[i].rect)):
            #print("got here")
            enemy.health -= projectiles[i].damage;
            del projectiles[i];
            if(enemy.health <= 0):
                break;
        else:
            i += 1
