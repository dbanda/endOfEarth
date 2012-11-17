import pygame
import math
import random
pygame.init()
height=1000
width=600
pink=[255,0,255]
yellow=[242,248,24]
white=[255,255,255]
black=[0,0,0]
blue=[74,89,221]
brown=[129,81,54]
screen=pygame.display.set_mode((height,width))
class planets(pygame.sprite.Sprite):
    def __init__(self,path,rect_x,rect_y,angle,radius,speed):
        pygame.sprite.Sprite.__init__(self) 
        self.path=path
        self.image=pygame.image.load(self.path).convert()
        self.rect_x=rect_x
        self.rect_y=rect_y
        self.angle=angle
        self.speed=speed
        self.radius=radius
        self.rect=[self.rect_x,self.rect_y]
        
    def motion(self):
        screen.blit(self.image, self.rect)
        pygame.display.update()
        self.angle+=self.speed
        self.rect_x=(height/2)+(self.radius*math.cos(math.radians(self.angle)))
        self.rect_x=int(self.rect_x)
        self.rect_y=(width/2)+(self.radius*math.sin(math.radians(self.angle)))
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
        self.pic=pygame.image.load(self.path).convert()
        self.x=x
        self.y=y
        self.rad=rad
        self.alt_angle=alt_angle
        self.alt_radius=alt_radius
        self.alt_speed=alt_speed
        self.rect=[self.x,self.y]
        
        
    def motion(self,flag):
        if flag==0:
            self.color=red
        elif flag==1:
            self.color=yellow
        elif flag==2:
            self.color=green
        else: self.color=red
        screen.blit(self.pic, (self.x,self.y))
        pygame.draw.circle(screen,self.color,(self.x+24,self.y+24),self.rad,3)
        pygame.display.update()
        self.alt_angle+=self.alt_speed
        self.x= (height/2) +(self.alt_radius*math.cos(math.radians(self.alt_angle)))
        self.x=int(self.x)
        self.y=(width/2)+(self.alt_radius*math.sin(math.radians(self.alt_angle)))
        self.y=int(self.y)
        self.rect=[self.x,self.y]
        
        
         
   
    
orbit_planet_list = pygame.sprite.RenderPlain()
m1=asteroids("C:\Python27\Project 6.090-End of Earth\missile.jpg",300,200,0,0,0)
d_planet=designated_planet("C:\Python27\Project 6.090-End of Earth\d_planet.jpg",red,800,150,25,0,300,8)
uranus=orbit_planets("C:\Python27\Project 6.090-End of Earth\uranus.jpg",500,200,0,300,5)
mars=orbit_planets("C:\Python27\Project 6.090-End of Earth\mars.jpg",100,200,0,175,2)
jupiter=orbit_planets("C:\Python27\Project 6.090-End of Earth\jupiter.jpg",300,150,0,250,10)
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
desig_planet.add(d_planet)
flag=0
def make_asteroid():
    x_coord=[0,100,0,900,970,970,690,55]
    y_coord=[10,125,450,400,50,550,0,575]
    for n in range(len(x_coord)):
     asteroid=asteroids("C:\Python27\Project 6.090-End of Earth\meteor.jpg",x_coord[n],y_coord[n],0,0,0)
     asteroid_list.add(asteroid)
     all_sprites_list.add(asteroid)
    return asteroid_list
make_asteroid()    
background=pygame.image.load("C:\Python27\Project 6.090-End of Earth\universe.jpg").convert()
clock=pygame.time.Clock()
running=1
while running==1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=0
    screen.blit(background,(0,0))
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
            
    
    d_planet.motion(flag)
    pygame.display.update()    
            
        
        
    clock.tick(25)
pygame.quit()
