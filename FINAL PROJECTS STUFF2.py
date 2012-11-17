import pygame, sys
import random
import math
from pygame.locals import *
# Define some colors

pink=[255,0,255]
yellow=[242,248,24]
white=[255,255,255]
black=[0,0,0]
blue=[74,89,221]
brown=[129,81,54]
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
pink=[255,0,255]
yellow=[242,248,24]
white=[255,255,255]
black=[0,0,0]
blue=[74,89,221]
brown=[129,81,54]
red      = ( 255,   0,   0)
background_colour = (255,255,255)
(width, height) = (1000, 600)

Launcher_height = 100
Fire_speed =100
angle_of_launcher= math.pi
draw_bullet = 0
score=0
screen = pygame.display.set_mode((1000, 600))
bullet_list =pygame.sprite.RenderPlain()

class planets(pygame.sprite.Sprite):
    def __init__(self,path,rect_x,rect_y,angle,radius,speed):
        pygame.sprite.Sprite.__init__(self) 
        self.path=path
        self.image=pygame.image.load(self.path).convert()
        self.rect = self.image.get_rect()
        self.rect_x=rect_x
        self.rect_y=rect_y
        self.angle=angle
        self.speed=speed
        self.radius=radius
        self.rect.x=self.rect_x
        self.rect.y = self.rect_y
        self.rect = self.image.get_rect()
        self.rect.x =-4
        self.rect.y = -4
        
    def motion(self):
        screen.blit(self.image, self.rect)
        #pygame.display.update()
        self.angle+=self.speed
        self.rect_x=(width/2)+(self.radius*math.cos(math.radians(self.angle)))
        self.rect_x=int(self.rect_x)
        self.rect_y=(height/2)+(self.radius*math.sin(math.radians(self.angle)))
        self.rect_y=int(self.rect_y)
        self.rect=[self.rect_x,self.rect_y]
        
        
        
            
class asteroids(planets):
    """inherit from planets"""
        
class orbit_planets(planets):
    """ inherit from planets """
    
    
class designated_planet(pygame.sprite.Sprite):
    def __init__(self,path,color,x,y,rad,alt_angle,alt_radius,alt_speed):
        pygame.sprite.Sprite.__init__(self) 
        self.color=color
        self.path=path
        self.image=pygame.image.load(self.path).convert()
        self.rect = self.image.get_rect()
        self.x=x
        self.y=y
        self.rad=rad
        self.alt_angle=alt_angle
        self.alt_radius=alt_radius
        self.alt_speed=alt_speed
        self.rect.x=self.x
        self.rect.y = self.y
        self.rect = self.image.get_rect()
        self.rect.x =-4
        self.rect.y = -4
        
    def motion(self,flag):
        if flag==0:
            self.color=red
        elif flag==1:
            self.color=yellow
        elif flag==2:
            self.color=green
        else: self.color=red
        screen.blit(self.image, (self.x,self.y))
        pygame.draw.circle(screen,self.color,(self.x+24,self.y+24),self.rad,3)
        #pygame.display.update()
        self.alt_angle+=self.alt_speed
        self.x= (width/2) +(self.alt_radius*math.cos(math.radians(self.alt_angle)))
        self.x=int(self.x)
        self.y=(height/2)+(self.alt_radius*math.sin(math.radians(self.alt_angle)))
        self.y=int(self.y)
        self.rect=[self.x,self.y]
        
    
class Launcher():
    def __init__(self, height):
        self.height= height
        self.x = self.height*math.cos(angle_of_launcher)
        self.y = self.height*math.sin(angle_of_launcher)
    
        
Cannon = Launcher(Launcher_height)
Cannon.x = Cannon.height*math.cos(angle_of_launcher)
Cannon.y = Cannon.height*math.sin(angle_of_launcher)



            

class earth(pygame.sprite.Sprite):
    def __init__(self,(earth_x, earth_y),size):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(currentDirectory + "\\planet.png").convert()
        self.x = earth_x
        self.y = earth_y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 10
        self.rect=[self.x,self.y]

    def display(self):
        self.image= pygame.image.load(currentDirectory + "\\planet.png").convert()
        #pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
        screen.blit(self.image, ((self.x-25), (self.y-25)))
        pygame.display.update()
        
        pygame.draw.polygon(screen, self.colour, [(earth_x+2,earth_y+2),(earth_x+2,earth_y+2), (earth_x+ Cannon.x,earth_y+ Cannon.y)], self.thickness-10)
        pygame.display.update()
        #print "ok"
        #print self.x

    def move(self):
        self.x = earth_x
        self.y = y

class missile(pygame.sprite.Sprite):
        def __init__(self, color , size,):
            pygame.sprite.Sprite.__init__(self) 
            self.size = size
            self.colour = color
            self.thickness = 4
            self.x = Cannon.x + earth_x
            self.y = Cannon.y + earth_y
            missile.angle = angle_of_launcher
            self.image = pygame.Surface([800, 600])
            self.rect = self.image.get_rect()
            #self.image.fill(green)
            #self.image.set_colorkey(green)
            self.rect.x = Cannon.x + earth_x 
            self.rect.y = Cannon.y + earth_y
            ##screen.blit(self.image, (100, 25))
            pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
            ##screen.blit(self.image, (25, 25))
            pygame.display.update() 
        def display(self, color):
            self.colour = color
            
            pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
            #pygame.display.update()
            #pygame.draw.circle(self.image, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
            #screen.blit(self.image, (25, 25))
        def move(self, speed):
            self.speed= speed
            self.x += self.speed *t/100.0*math.cos(missile.angle)
            self.y += self.speed *t/100.0*math.sin(missile.angle)
            self.rect.x += self.speed *t/100.0*math.cos(missile.angle)
            self.rect.y += self.speed *t/100.0*math.sin(missile.angle)
            #pygame.display.update()
            #print self.x



        
#screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('My Game')

size = 50
earth_x = 500
earth_y = 300
earth = earth((earth_x, earth_y), size)
t =1

''' class target(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("C:\Users\dalitsoanda\Dropbox\planet.png").convert()
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
    
target1 = target()'''
#target1.__init__()

pygame.init()
clock=pygame.time.Clock()


all_sprites_list = pygame.sprite.RenderPlain()
block_list = pygame.sprite.RenderPlain()
#all_sprites_list.add(target1)
#print t

orbit_planet_list = pygame.sprite.RenderPlain()
m1=asteroids(currentDirectory + "\\meteor.jpg",300,200,0,0,0)
d_planet=designated_planet(currentDirectory + "\\d_planet.jpg",red,800,150,25,0,300,8)
uranus=orbit_planets(currentDirectory + "\\uranus.jpg",500,200,0,300,5)
mars=orbit_planets(currentDirectory + "\\mars.jpg",100,200,0,175,2)
jupiter=orbit_planets(currentDirectory + "\\jupiter.jpg",300,150,0,250,10)
asteroid_list=pygame.sprite.RenderPlain()
all_sprites_list=pygame.sprite.RenderPlain()
desig_planet=pygame.sprite.RenderPlain()
missiles=pygame.sprite.RenderPlain()
orbit_planet_list.add(mars)
orbit_planet_list.add(uranus)
orbit_planet_list.add(jupiter)
all_sprites_list.add(mars)
all_sprites_list.add(uranus)
all_sprites_list.add(jupiter)
all_sprites_list.add(d_planet)
all_sprites_list.add(earth)
all_sprites_list.add(asteroid_list)

desig_planet.add(d_planet)
flag=0

def make_asteroid():
    x_coord=[0,100,0,900,970,970,690,55]
    y_coord=[10,125,450,400,50,550,0,575]
    for n in range(len(x_coord)):
     asteroid=asteroids(currentDirectory + "\\meteor.jpg",x_coord[n],y_coord[n],0,0,0)
     asteroid_list.add(asteroid)
     all_sprites_list.add(asteroid)
    return asteroid_list

make_asteroid()    
background=pygame.image.load(currentDirectory + "\\universe.jpg").convert()
clock=pygame.time.Clock()


running = True

while running == True:
    clock.tick(30)    
    #pygame.init()

    # Used to manage how fast the screen updates
    #print ms

    '''screen.blit(background,(0,0))
    asteroid_list.draw(screen)
    orbit_planet_list.draw(screen)
    mars.motion()
    jupiter.motion()
    uranus.motion()
    score=0
    color[3]
    if hit:
        score+=1
        for n in range(3):
            if score==1:
                flag=0
                color[1]=bullet_color
            elif score==2 and not(bullet_color==color[n]):
                flag=1
                color[2]=bullet_color
            elif score==3 and not(bullet_color==color[n]):
                flag==2
                color[3]=bullet_color
            else:
                flag=flag
            
    
    d_planet.motion(flag)'''
    
    
        
    keys = pygame.key.get_pressed()
    pygame.key.set_repeat (500, 30)
    #screen.fill(black)
    
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
         bullet_list.add(bullet)
         
         draw_bullet = 1
           

    if keys[pygame.K_a]:
        
       #pygame.key.set_repeat (500, 30) 
        
        angle_of_launcher += 0.1
        Cannon.x = Cannon.height*math.cos(angle_of_launcher)
        Cannon.y = Cannon.height*math.sin(angle_of_launcher)
        Cannon.tip_x = Cannon.x + earth_x
        Cannon.tip_y = Cannon.y + earth_y


    if keys[pygame.K_d]:
              
        angle_of_launcher -= 0.1
        Cannon.x = Cannon.height*math.cos(angle_of_launcher)
        Cannon.y = Cannon.height*math.sin(angle_of_launcher)
        Cannon.tip_x = Cannon.x + x
        Cannon.tip_y = Cannon.y + y
    

   # x+=z
   # y+=t
    
    
        
    
    #target1.__init__()

    '''earth.move()
    earth.display()
    print all_sprites_list
    all_sprites_list.draw(screen)'''
    
    
    if draw_bullet == 1:
        bullet.move(Fire_speed)
        bullet.display(bullet_color)
         #-----------collision system---------
        
        
        #print block_list
        #print bullet
        blocks_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
        
    #pygame.display.flip()
    screen.blit(background,(0,0))
    #asteroid_list.draw(screen)
    #orbit_planet_list.draw(screen)
    mars.motion()
    jupiter.motion()
    uranus.motion()
    score=0

    d_planet.motion(flag)
    #pygame.display.update()    

    #earth.move()
    #earth.display()
    print all_sprites_list
    #pygame.display.update()
    all_sprites_list.draw(screen)
    bullet_list.draw(screen)
    print bullet_list
    
pygame.quit
