import pygame, sys
import random
import math
from pygame.locals import *
# Define some colors
import os
currentDirectory = os.getcwd()



black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
background_colour = (255,255,255)
(width, height) = (800, 600)

Launcher_height = 100
Fire_speed =100
angle_of_launcher= math.pi
draw_bullet = 0
score=0
screen = pygame.display.set_mode((width, height))

 
class Launcher():
    def __init__(self, height):
        self.height= height
        self.x = self.height*math.cos(angle_of_launcher)
        self.y = self.height*math.sin(angle_of_launcher)
    
        
Cannon = Launcher(Launcher_height)
Cannon.x = Cannon.height*math.cos(angle_of_launcher)
Cannon.y = Cannon.height*math.sin(angle_of_launcher)



            

class earth(pygame.sprite.Sprite):
    def __init__(self, (x, y), size):
        pygame.sprite.Sprite.__init__(self) 
        self.x = 300
        self.y = 300
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 10
        

    def display(self, ):
        self.image= pygame.image.load(currentDirectory + "\\planet.png").convert()
        #pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
        screen.blit(self.image, (int(self.x -25), int(self.y-25)))
        
        pygame.draw.polygon(screen, self.colour, [(x+2,y+2),(x+2,y+2), (x+ Cannon.x,y+ Cannon.y)], self.thickness-10)
        #print "ok"
        #print self.x

    def move(self):
        self.x = x
        self.y = y

class missile(pygame.sprite.Sprite):
        def __init__(self, color , size,):
            pygame.sprite.Sprite.__init__(self) 
            self.size = size
            self.colour = color
            self.thickness = 4
            self.x = Cannon.x + x
            self.y = Cannon.y + y
            missile.angle = angle_of_launcher
            self.image = pygame.Surface([800, 600])
            self.rect = self.image.get_rect()
            #self.image.fill(green)
            #self.image.set_colorkey(green)
            self.rect.x = Cannon.x + x 
            self.rect.y = Cannon.y + y
            ##screen.blit(self.image, (100, 25))
            pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
            ##screen.blit(self.image, (25, 25))
        def display(self, color):
            self.colour = color
            
            pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
            #pygame.draw.circle(self.image, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
            #screen.blit(self.image, (25, 25))
        def move(self, speed):
            self.speed= speed
            self.x += self.speed *t/100.0*math.cos(missile.angle)
            self.y += self.speed *t/100.0*math.sin(missile.angle)
            self.rect.x += self.speed *t/100.0*math.cos(missile.angle)
            self.rect.y += self.speed *t/100.0*math.sin(missile.angle)
            #print self.x



        
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('My Game')

size = 50
x = 400
y = 300
earth = earth((x, y), size)
t =1

class target(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(currentDirectory + "\\planet.png").convert()
        #pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
        screen.blit(self.image, (25, 25))
        
        #self.image = pygame.Surface([100, 100])
        
        
        #self.image.fill(green)
        #self.image.set_colorkey(green)
        #pygame.draw.circle(self.image, green, (100, 100), 100, 100)        
        
        #pygame.draw.circle(screen, green, (100, 100), 100, 100)

        #self.image = pygame.Surface([100, 100])
        #self.image.fill(white)
        #self.image.set_colorkey(white)
            #pygame.draw.ellipse(self.image,green,[0,0,100,100])
            #pygame.draw.circle(self.image, green, (100, 100), 100, 100)
        self.rect = self.image.get_rect()
        #self.rect.x =-4
        #self.rect.y = -4
    
target1 = target()
#target1.__init__()

pygame.init()
clock=pygame.time.Clock()


all_sprites_list = pygame.sprite.RenderPlain()
block_list = pygame.sprite.RenderPlain()
all_sprites_list.add(target1)
#print t

running = True

while running == True:
    clock.tick(30)    
    #pygame.init()

    # Used to manage how fast the screen updates
    #print ms

    
    
    
        
    keys = pygame.key.get_pressed()
    pygame.key.set_repeat (500, 30)
    screen.fill(black)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False
            pygame.quit()
            exit  
            
                
    if  keys[pygame.K_w]:
         Launcher_height+=1
         Cannon =Launcher(Launcher_height)

    if  keys[pygame.K_s]:
         Launcher_height+= -1
         Cannon =Launcher(Launcher_height)
         
    if  keys[pygame.K_q]:
         Fire_speed+=1
         
    if  keys[pygame.K_e]:
         Fire_speed+= -1
         
         
    if  keys[pygame.K_SPACE]:

           
         
         
         bullet_color = random.choice([green, red, white])
         bullet= missile(bullet_color,5)
         t += 1/30.0

         
         block_list.add(target1)
         draw_bullet = 1
           

    if keys[pygame.K_a]:
        
       #pygame.key.set_repeat (500, 30) 
        
        angle_of_launcher += 0.1
        Cannon.x = Cannon.height*math.cos(angle_of_launcher)
        Cannon.y = Cannon.height*math.sin(angle_of_launcher)
        Cannon.tip_x = Cannon.x + x
        Cannon.tip_y = Cannon.y + y


    if keys[pygame.K_d]:
              
        angle_of_launcher -= 0.1
        Cannon.x = Cannon.height*math.cos(angle_of_launcher)
        Cannon.y = Cannon.height*math.sin(angle_of_launcher)
        Cannon.tip_x = Cannon.x + x
        Cannon.tip_y = Cannon.y + y
    

   # x+=z
   # y+=t
    
    
        
    
    #target1.__init__()

    earth.move()
    earth.display()
    print all_sprites_list
    all_sprites_list.draw(screen)
    
    
    if draw_bullet == 1:
        bullet.move( Fire_speed)
        bullet.display(bullet_color)
         #-----------collision system---------
        
        
        #print block_list
        #print bullet
        blocks_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
        
    pygame.display.flip()
    
    
pygame.quit
