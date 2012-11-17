'''import pygame package to run GUI and manage user interface'''
import pygame
import os
CurrentDir = os.getcwd()
'''initialize pygame functions'''
pygame.init()
'''initialize pygame font functions'''
pygame.font.init()
# initialize the height and width of the display screen
height=1000 
width=600
white=[255,255,255]
black=[0,0,0]
screen=pygame.display.set_mode((height,width)) #establish screen to enable user interface
global rect_x
global rect_y
'''function to display the contents of a file to screen. File contains Game storyline'''
def story():
    flag=1 #set varible flag to allow while loop to continue until condition is met met
    '''rectangular co-ordinates for publishing image on screen'''
    rect_x=50
    rect_y=0
    '''open file and read the contents'''
    storyline=open(CurrentDir + "\\storyline.txt","r")
    '''read first line of the open file'''
    read=storyline.readline()
    '''font of size 30'''
    words=pygame.font.Font(None,30)
    '''make text from file an object with the color black in order to be displayed to screen '''
    text=words.render(read,True,black)
    while flag==1: 
     #display created object made above on screen at rectangular co-ordinates set above''' 
        screen.blit(text,(rect_x,rect_y))
        '''if EOF, exit while loop'''
        if not read:   
            break
        '''read next line of file and display to screen 50 pixels down from the first object'''
        read=storyline.readline()
        text=words.render(read,True,black)
        rect_y+=50
        '''pause screen for 300 milliseconds before updating'''        
        pygame.time.wait(300)
        '''update screen'''
        pygame.display.update()
        
    '''close file'''        
    storyline.close()
    '''function that displays the game controls and their actions to screen'''
def controller():
    screen.fill(white)
    flag=1
    rect_x=50
    rect_y=0
    storyline=open(CurrentDir + "\\controls.txt","r") #open file that contains information on controls
    read=storyline.readline() # read first line from file
    words=pygame.font.Font(None,30) #initialze font size
    text=words.render(read,True,black)#make text from file into an object to be displayed to screen
    while flag==1:
        screen.blit(text,(rect_x,rect_y)) #display object (text) to screen
        '''check to see if EOF, if so then exit loop'''
        if not read:
            break 
        read=storyline.readline() #read next line of file
        text=words.render(read,True,black)
        rect_y+=50 #increment rectangular y co-ordinate to display object progressively 50 pixels downwards
        pygame.time.wait(300) #pause screen for 300 milliseconds
        pygame.display.update()#update screen
    storyline.close()#close file
    back='Press wait....you will be returned shortly' #courtesy notice about returning to main menu
    '''create object from text and display to screen at rectangular co-ordinates (50,450)'''
    wrd=pygame.font.Font(None,20)
    back_enter=wrd.render(back,True,black)
    screen.blit(back_enter,(50,450))
    pygame.display.update() #update screen
    pygame.time.wait(7000)# pause screen 
    menu()    #call menu function to return to main menu
    
   
'''function that displays menu options to screen'''    
def menu():
    '''set screen background to white'''
    screen.fill(white)
    flag=1
    '''text to display to screen'''
    '''display all text to screen'''
    read="PLAY" 
    txt="CONTROLS"
    main_m='MAIN MENU'
    words=pygame.font.Font(None,30)
    text=words.render(read,True,black)
    nex=words.render(txt,True,black)
    screen.blit(text,(450,300))
    screen.blit(nex,(450,350))
    main=pygame.font.Font(None,50)
    menu_text=main.render(main_m,True,black)
    screen.blit(menu_text,(400,200))
    pygame.display.update()
screen.fill(white)
clock=pygame.time.Clock() #set clock function
running=1    # set running to 1 as condition for the while loop that updates the screen
pygame.time.wait(1000) 
pygame.display.update()
story() #call story function to dispaly storyline to screen
while running==1:
    for event in pygame.event.get():
        '''get input from the keyboard'''
        keys = pygame.key.get_pressed()
        '''check to see if user chooses to exit function by pressing escape or ending program'''
        if event.type==pygame.QUIT or keys[pygame.K_ESCAPE] :
            running=0 # if user chooses exit signal,end loop and exit program
            exit
        menu()#call menu function to display list of options
        pos=pygame.mouse.get_pos() # get position of mouse cursor on screen
        x=pos[0]
        y=pos[1]
        play=pygame.Rect(450,300,50,50) #initialize options' rectangles
        control=pygame.Rect(450,350,100,100)
        '''check to see if mouse cursor is positioned over the rectangular co-ordinates of the option objects establishes and if the user presses the mouse key'''
        if play.collidepoint(x,y)==True and event.type==pygame.MOUSEBUTTONDOWN:
             execfile(CurrentDir + "\\game.py")#if user clicks the object 'play', execute external module game.py'''
        elif control.collidepoint(x,y) and event.type==pygame.MOUSEBUTTONDOWN:
             controller() #if the user clicks the object 'control', call the controller function'''
    clock.tick(25) #set the timer to run frameshifts every 25 milliseconds'''     
    pygame.display.update()
pygame.quit()#close pygame
    
