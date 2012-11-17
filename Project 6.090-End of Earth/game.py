import pygame
'''import pygame package to implement GUI'''
import math
import os
CurrentDir = os.getcwd()
'''import math package to allow for mathematical manipulation of variables'''
from random import choice
pygame.init() #initialize pygame package
'''set height and width of display screen'''
height=600 
width=1000
'''initialize color values'''
pygame.display.init() #initialize the display function of the pygame package
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pink=[255,0,255]
yellow=[242,248,24]
white=[255,255,255]
black=[0,0,0]
red=[255,0,0]
blue=[74,89,221]
brown=[129,81,54]
green=[0,255,0]
'''set initial height of launcher'''
Launcher_height = 80
'''set initial speed of missiles'''
Fire_speed =50
'''set initial angle of launcher'''
angle_of_launcher= math.pi
'''condition that handles drawing missiles'''
draw_bullet = 0
screen=pygame.display.set_mode((width, height)) #publishing display screen
pygame.display.set_caption('End of Earth') #caption of screen
all_sprites_list=pygame.sprite.RenderPlain() #initializing group to handle all sprites  
block_list=pygame.sprite.RenderPlain() #initializing another group to handle certain sprites

'''Parent class called planet that has attributes and methods to be inherited'''
class planets(pygame.sprite.Sprite): #setting this object to be a sprite
    def __init__(self,path,rect_x,rect_y,angle,radius,speed,name,flag=0, colors_got =set()): #initializing object with attributes
        self.name = name #name of object
        pygame.sprite.Sprite.__init__(self) #initializing attributes and methods of sprites 
        self.path=path #path of file that contains object image
        self.image=pygame.image.load(self.path).convert() #getting image and converting it to pixel format on screen
        '''x,y position of objects on screen'''
        self.rect_x=rect_x 
        self.rect_y=rect_y
        ''' initial angle of objects to start orbiting'''
        self.angle=angle
        ''' speed of orbit'''
        self.speed=speed
        '''radius of orbit'''
        self.radius=radius
        self.rect=((self.rect_x,self.rect_y),(100,100)) #rectangular co-ordinates of object on screen
        self.flag = flag #variable that indicates when target planet is hit
        self.colors_got =colors_got #set of colors
        
    def __str__(self):
        return str(self.name)
    '''motion method of object defines and updates the movement of object on screen'''
    def motion(self): 
        self.rect=((self.rect_x,self.rect_y),(100,100)) #rectangular co-ordinates of object
        self.angle+=self.speed #increment angle of orbit by speed variable to change angle of rotation as well as the rate of change of angle of rotation
        '''change rectangular co-ordinates to make object have a circular trajectory'''
        self.rect_x=(width/2)+(self.radius*math.cos(math.radians(self.angle))) #change x co-ordinate of object by changing the angle 
        self.rect_x=int(self.rect_x) #convert float type varible x to an integer
        self.rect_y=(height/2)+(self.radius*math.sin(math.radians(self.angle))) #change y co-ordinate of bject by changing the angle
        self.rect_y=int(self.rect_y)#convert float type varible y to an integer
        '''check to see if flag of target_planet is green. If true, add the color green to the set of colors that has hit the target planet and change the image to that of a green planet'''
        if self.flag == green: 
            print self.name," green" 
            self.colors_got.add('green')
            self.image=pygame.image.load(CurrentDir + "\\" + str(self.name)+"green"+".jpg").convert()
            
        '''check to see if flag of target_planet is white. If true, add the color green to the set of colors that has hit the target planet and change the image to that of a white planet'''        
        if self.flag == white:
            print self.name," white"
            self.colors_got.add('white')
            self.image=pygame.image.load(CurrentDir + "\\" + str(self.name)+"white"+".jpg").convert()
        '''check to see if flag of target_planet is red. If true, add the color green to the set of colors that has hit the target planet and change the image to that of a red planet'''    
        if self.flag == red:
            print self.name," red"
            self.colors_got.add('red')
            self.image=pygame.image.load(CurrentDir + "\\" + str(self.name)+"red"+".jpg").convert()
        '''check to see if the target planet has been hit by missiles of all three colors. If true, then call score function'''
        if len(self.colors_got) ==3:
            print 'you are the winner'
            scored(len(self.colors_got))#call score function that uses the number of colors as a parameter
            
            
'''class to define object launcher to launch bullets'''        
class Launcher():
    def __init__(self, height):
        self.height= height #height of launcher
        '''x,y positions of launcher on screen'''
        self.x = self.height*math.cos(angle_of_launcher) 
        self.y = self.height*math.sin(angle_of_launcher)
    
        
Cannon = Launcher(Launcher_height) #assigning an instance of the class launcher

'''class to define central planet called earth'''
class earth(pygame.sprite.Sprite):
    def __init__(self, path,(x, y), size):
        pygame.sprite.Sprite.__init__(self) #initialize the object as a sprite containing all its attributes and methods
        '''x,y position of object on screen'''
        self.x = x
        self.y = y
        self.path=path #path directory of object image
        self.size = size 
        self.colour = (0, 0, 255) #colour of launcher on screen
        self.thickness = 10 #thickness of launcher on screen
        self.rect=([self.x,self.y],(50,50)) #rectangular co-ordinates of object on screen

    def show(self):
        self.image= pygame.image.load(self.path).convert() #get the object image and convert to pixel format
        screen.blit(self.image, (width/2-50, height/2-50)) #render the converted image to an object and display on screen
        pygame.draw.polygon(screen, self.colour, [((self.x)+2,(self.y)+2),((self.x)+2,(self.y)+2), ((self.x)+ Cannon.x,self.y+ Cannon.y)], self.thickness) #draw launcher on screen
      
        
'''co-ordinates of object'''
x=width/2
y=height/2
'''define instance of the earth class'''
earth = earth(CurrentDir + "\\earth.jpg",(x, y), 50)
t=1        
'''class to define bullets as objects'''
class missile(pygame.sprite.Sprite):
    def __init__(self, color , size,):
            pygame.sprite.Sprite.__init__(self) #define object as sprites containgin all its attributes and methods
            self.size = size #size of missile
            self.colour = color #color of missile
            self.thickness = 4 #thickness fo missile circle
            '''x,y positions of missile based on luncher position'''
            self.x = Cannon.x + x 
            self.y = Cannon.y + y
            self.angle = angle_of_launcher #angle of missile is set to be the same as that of the launcher
            self.image = pygame.Surface([10, 10])#image of missile with rectangular co-ordinates at 10,10
            self.rect = self.image.get_rect() #get rectangular co-ordinates of the missile
            pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness) #draw circular missile initially
            
    '''method to draw color and position of missile object'''
    def display(self, color):
        self.colour = color
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)#draw circular missile with updated co-ordinates
           
    '''method to define and update co-ordinates of missile object'''    
    def move(self, speed):
        self.speed= speed #speed of missile
        '''change in x and y positions of missile object. defining trajectory'''
        self.x += self.speed *t/100.0*math.cos(self.angle)
        self.y += self.speed *t/100.0*math.sin(self.angle)           

        
'''define class asteroids with attributes'''            
class asteroids(pygame.sprite.Sprite):
    def __init__(self,path,rect_x,rect_y):
        pygame.sprite.Sprite.__init__(self)#initialize the object as a sprite containing all its attributes  and methods
        self.path=path #path directory of object image
        self.image=pygame.image.load(self.path).convert() #loads and converts the object image to pixel format
        '''x,y positions of objects on screen'''
        self.rect_x=rect_x 
        self.rect_y=rect_y
        self.rect=([self.rect_x,self.rect_y],(10,10)) #rectangular co-ordinates of objects on screen
        
        
'''define subclass that inherits from parent class Planets'''        
class orbit_planets(planets): 
    """ inherit from planets """
    
'''define instances that inherit from orbit planets and have individual attributes'''     
uranus=orbit_planets(CurrentDir + "\\uranus.jpg",500,200,0,175,5,'uranus')
pluto=orbit_planets(CurrentDir + "\\uranus.jpg",500,200,0,175,2.5,'uranus')
mars=orbit_planets(CurrentDir + "\\mars.jpg",100,200,0,300,10,'mars')
jupiter=orbit_planets(CurrentDir + "\\jupiter.jpg",300,150,0,250,10,'jupiter')
'''define list of orbiting planets'''
orbit_planet_list=[mars,uranus, jupiter,pluto]
'''add orbiting planets to the all sprites list'''
all_sprites_list.add(mars, uranus, jupiter,pluto)


target_planet = 'mars'
flag=0 #initialize the hit count of the target planet to zero
'''function that displays the score to screen and ends game'''
def scored(flag):
    screen.fill(black) #changes screen color to black
    pygame.display.update() #updates the screen
    final=pygame.time.get_ticks() #get the time in milliseconds that the program has been running
    final=float(final) #converts integer variable to float 
    if flag<2: #if the target planet has not been hit by all three colored missiles, then the score is zero
        user_score=0
        color=white
        size=50
        winner='I am sorry...better luck next time :( ' #displays to screen a consolation message
    elif flag==3: #fit the target planet has been hit with all three colored missiles, then score is calculated based on time of play and displayed in large font to screen
        user_score=(1/(0.001*final))*50000 #calculate score from time of play
        color=red 
        size=100 #large font for object(text) display
        winner='Winner' #text to display to screen
    user_score=round(user_score) #round the float number to zero decimal places
    u_score="Your score is:"
    user_score=str(user_score) #convert float variable to a string
    u_score+=user_score #concatenates the u_score list to inclide the calculated score
    '''render user_score as an object to be displayed to screen'''
    words=pygame.font.Font(None,50)
    words=pygame.font.Font(None,size)
    msg=words.render(winner,True,color)
    text=words.render(u_score,True,white)
    screen.blit(text,(300,400))
    screen.blit(msg,(100,100))
    pygame.display.update()#update screen
    pygame.time.wait(1000) #pause screen for 1000 milliseconds
    pygame.quit() #quit pygame
    exit #exit program
    
'''list of x,y co-ordinates to position asteroids'''
x_coord=[0,850,0,900,900,50,500]
y_coord=[0,0,550,550,300,300,395]
n=0
'''create 7 asteroids and add them to the all_sprites_list group to be drawn to screen'''
for n in range(7):
    asteroid=asteroids(CurrentDir + "\\meteor.jpg",x_coord[n],y_coord[n])
    all_sprites_list.add(asteroid)
    
        
background=pygame.image.load(CurrentDir + "\\univ.jpg").convert() #get backgorund image and loads it to screen and converts it to pixel format
clock=pygame.time.Clock() #initialise clock to time updates
running=1 #condition used to continuously run loop


while running==1:
    
    
    screen.blit(background,(0,0)) #render the background image to screen
    keys = pygame.key.get_pressed() #get key pressed by user
    for event in pygame.event.get(): #allows user to put input and collects input in a queue
        '''checks to see if the user has tried to exit the program. if true, calls the score function'''   
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            scored(flag)
            
             
                   
                
    '''checks to see if the user presses the 'q' key on the keyboard and increments the speed of the bullet'''
    if  keys[pygame.K_q]:
         Fire_speed+=1
    '''checks to see if the user presses the 'e' key on the keyboard and decrements speed of bullet'''    
    if  keys[pygame.K_e]:
         Fire_speed+= -1
         
    '''checks to see if the user presses the 'space' key on the keyboard and if true, generates a bullet of random color'''  
    if  keys[pygame.K_SPACE]:
         
         bullet_color = choice([green, red, white])
         bullet= missile(bullet_color, 5)
         t += 1/30.0 # contained in defining co-ordinates of missile on screen
         sound = pygame.mixer.Sound(CurrentDir + '\\sound02.wav').play()


         
         draw_bullet = 1
    '''checks to see if the 'd' key on the keyboard is pressed and changes the angle of the launcher to allow it to rotate and update the position of the launcher'''
    if keys[pygame.K_a]:     
        
         angle_of_launcher += .05 #allows clockwise rotation
         Cannon.x = Cannon.height*math.cos(angle_of_launcher)
         Cannon.y = Cannon.height*math.sin(angle_of_launcher)
         Cannon.tip_x = Cannon.x + x
         Cannon.tip_y = Cannon.y + y

    '''checks to see if the 'd' key on the keyboard is pressed and changes the angle of the launcher to allow it to rotate and update the positio of the launcher'''
    if keys[pygame.K_d]:
        #draw_bullet == 0
        angle_of_launcher -= .05 #allows counterclockwise rotation
        Cannon.x = Cannon.height*math.cos(angle_of_launcher)
        Cannon.y = Cannon.height*math.sin(angle_of_launcher)
        Cannon.tip_x = Cannon.x + x
        Cannon.tip_y = Cannon.y + y
    

   

  
    earth.show() #call method of earth to show position of earth on screen
    
    '''checks to see if draw_bullet indicator is changed so as to draw bullet on screen'''
    if draw_bullet > 0:
        bullet.move( Fire_speed)
        bullet.display(bullet_color)
         #-----------collision detection system---------
        
        bullet.move( Fire_speed) #update speed and position of bullet
        bullet.display(bullet_color) #call method of bullet to display bullet position and color to screen 
        pygame.display.update(bullet.rect) #update only the rectangles of the bullet position
      
        for i in orbit_planet_list: #do for all the planets contained in the list orbit_planet_list
            
            if i.rect_x<= bullet.x <= i.rect_x+35: #if the x co-ordinate of the bullet is between that of a planet contained in the list, check the y co-ordinates of the same
                if i.rect_y +20 <= bullet.y <= i.rect_y+100: #if the y co-ordinates of teh bullet is between that of a planet, collision detected!
                        

                        
                        '''if the planet in collision is the target planet , kill bullet object and change flag color of planet'''
                        if i.name == target_planet: 
                            bullet.kill()
                            draw_bullet = 0 #does not draw bullet
                            i.flag = bullet_color
                            
                            '''if the planet in collision is not the target planet,kill the bulletand remove planet from list of orbiting planets so that it is no longer displayed to screen'''    
                        else:
                            bullet.kill()
                            draw_bullet = 0 #does not draw bullet
                            i.kill() #kill planet(sprite)
                            bulletsound = pygame.mixer.Sound(CurrentDir + "\\sound.wav").play()
                            orbit_planet_list.remove(i)
    '''all all the planets in the list orbit_planet_list, call their method motion to update the position on screen and to create movement'''    
    for d in orbit_planet_list:
        d.motion()
        
    all_sprites_list.draw(screen) #'draw attribute of sprites'-draw all sprites in group to screen
    pygame.display.update() #update screen
        
    clock.tick(60) #update screen every 60 milliseconds
pygame.quit() #end pygame
