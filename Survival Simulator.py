import math
import os
#os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0, 30)
from pygame import * 
#import combinedsim
import random

ice = 0
sea = 1
areax = 500
areay = 500 
up = 2
down = 3
left = 4
right = 5
foodx = 975
foody = 675
age = 0
eat = 0
running = True
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)



alive=True

init()

#colours
OFFWHITE = (250,250,250)
BLUE = (153,204,255)
PURPLE = (192,179,255)
TURQUOISE = (172,255,242)
GREY = (192,192,192)
DARKPURPLE = (139,118,246)
BLUE2 = (0,77,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

x=510 #starting point for habitat scale
y=340 #y pos of fhabitat scale

x2=510 #starting point for food scale
y2=440 #y pos of food scale

x3=510 #starting point for birth rate scale
y3=540 #y pos of birth rate scale

#MOVING indicated whether or the the user is moving the scale
MOVING=False 
MOVING2=False
MOVING3=False


#go button in menu
goButton = image.load("gobutton.png") 
goButton = transform.scale(goButton, (100, 100))
waves = image.load("simulationwaves.png")
waves = transform.scale(waves, (50, 50))
icepattern = image.load("icereflection.png")
icepatterm = transform.scale(icepattern, (50, 50))
polarBear = image.load('polarbear.png') 
polarBear = transform.scale(polarBear, (50,50))
#polar bear image
polarBear = image.load('polarbear.png') 
polarBear = transform.scale(polarBear, (150,100))
polarSmall = transform.scale(polarBear, (40,30))
#fish image
fish = image.load('redfish.png') 
fish = transform.scale(fish, (40,40))

#Fonts
SIGNPAINTER = font.SysFont("SignPainter",80)
MARKERFELT = font.SysFont("Markerfelt",30)
FUTURA = font.SysFont("Futura",30)
ARIAL = font.SysFont("Arial",25)



SIZE = width, height = 1000, 700
screen = display.set_mode(SIZE)



def drawScene2(screen, mx, my, button, myList):
    draw.rect(screen, BLACK, (0, 0, width, height))
    startx = 0
    starty = 0
    widthx = 50
    widthy = 50
    counter = 1
    
    for i in range(len(myList)):
        if myList[i] == 1:
            color = (thickness[i], thickness[i], 255) #WHITE GOES AWAY BLUE STAYS
                                
        else:
            color = (0,0,255)
            
        if color == (0,0,255):
            draw.rect(screen, color, (startx, starty, widthx, widthy))
            waterxList.append(startx)
            wateryList.append(starty)                  
            screen.blit(waves,(startx,starty))
                  
        else:
            draw.rect(screen, color, (startx, starty, widthx, widthy))
            screen.blit(icepattern,(startx,starty))
        draw.rect(screen, BLACK, (startx, starty, widthx, widthy), 1)
        counter+=1
        if counter == 21:
            startx = 0
            counter = 1
            starty += widthy
        else:
            startx += widthx
    display.flip()


#function to draw bear multiple times in menu
def drawBear(x,y):
    screen.blit(polarBear, (x,y))

#main drawing function for menu
def drawScene(screen,button,mx,my):
    #if page == 1 you are on the menu page
    if page == 1:
        screen.fill(TURQUOISE)
        title = SIGNPAINTER.render("MENU", 1, DARKPURPLE)
        screen.blit(title,(425,100))
        instructions = MARKERFELT.render("Please select the parameters.", 1, DARKPURPLE)
        screen.blit(instructions,(325,200))  

        draw.rect(screen, OFFWHITE, (250,300,500,75))#habitat white rect


        draw.line(screen,BLACK,(510,340),(730,340),2)#scalehabitat
        draw.line(screen,BLACK,(510,340),(510,350),2)
        draw.line(screen,BLACK,(730,340),(730,350),2)


        circle1 = draw.circle(screen,BLUE,(x,y),10) #scrollhabitat
        valuePrint = ARIAL.render(str(value), 1, BLACK)
        screen.blit(valuePrint,(x-20,300))


        draw.rect(screen, OFFWHITE, (250,400,500,75)) #food white rect

        draw.line(screen,BLACK,(510,440),(730,440),2)#scalefood
        draw.line(screen,BLACK,(510,440),(510,450),2)
        draw.line(screen,BLACK,(730,440),(730,450),2)    


        circle2= draw.circle(screen,BLUE,(x2,y2),10) #scrollfood
        value2Print = ARIAL.render(str(value2), 1, BLACK)
        screen.blit(value2Print,(x2-20,400))    



        draw.rect(screen, OFFWHITE, (250,500,500,75))  #birth rate white rect

        draw.line(screen,BLACK,(510,540),(730,540),2)#scalebrate
        draw.line(screen,BLACK,(510,540),(510,550),2)
        draw.line(screen,BLACK,(730,540),(730,550),2)      

        value3Print = ARIAL.render(str(value3), 1, BLACK)
        screen.blit(value3Print,(x3-20,500))    

        circle3= draw.circle(screen,BLUE,(x3,y3),10) #scrollbrate

        #labelling the scales
        hLoss = FUTURA.render("Initial ice quantity", 1, BLUE2)
        screen.blit(hLoss,(250,320))    
        fSource = FUTURA.render("Food source", 1, BLUE2)
        screen.blit(fSource,(300,420))  
        bRate = FUTURA.render("Birth rate", 1, BLUE2)
        screen.blit(bRate,(300,520))   


        screen.blit(goButton,(450,580))


        for i in range(1,700,100): #polar bear design on menu
            drawBear(50,i)
            drawBear(800,i)
    display.flip()

def bear(screen, vitalityList, bearxList, bearyList ,ageList): #bear life cycle
    for i in range (len(bearxList)-1,-1,-1):
        vitalityList[i] -= 10
        ageList[i] += 1
        
        direction = random.randint(2,5)
        
        if direction == up:
            if bearxList[i] <= 25:
                bearxList[i] += 50
            else: 
                bearxList[i] -= 50      
        if direction == down:
            if bearxList[i] >= 975:
                bearxList[i] -= 50
            else: 
                bearxList[i] += 50
        if direction == left:
            if bearyList[i] <= 25:
                bearyList[i] += 50
            else: 
                bearyList[i] -= 50
        if direction == right:
            if bearyList[i] >= 675:
                bearyList[i] -= 50
            else: 
                bearyList[i] += 50   

        for j in range (len(foodxList)-1,-1,-1):
            if bearxList[i] == foodxList[j] and bearyList[i] == foodyList[j]:
                vitalityList[i] += 30
                del(foodxList[j],foodyList[j])
        for j in range (len(waterxList)-1,-1,-1):
            if bearxList[i] == waterxList[j] and bearyList[i] == wateryList[j]:
                vitalityList[i] -= 30
        
        screen.blit(polarSmall,(bearxList[i], bearyList[i]))
        if ageList[i] == 30 or vitalityList[i] <= 0:
            del(bearxList[i],bearyList[i],ageList[i],vitalityList[i])
        display.flip()
    

def food (screen,foodxList, foodyList):
    for i in range (len(foodxList)-1,-1,-1):        
        directionf = random.randint(2,5)
        
        if directionf == up:
            if foodxList[i] <= 25:
                foodxList[i] += 50
            else: 
                foodxList[i] -= 50        
        if directionf == down:
            if foodxList[i] >= 975:
                foodxList[i] -= 50
            else: 
                foodxList[i] += 50
        if directionf == left:
            if foodyList[i] <= 25:
                foodyList[i] += 50
            else: 
                foodyList[i] -= 50
        if directionf == right:
            if foodyList[i] >= 675:
                foodyList[i] -= 50
            else: 
                foodyList[i] += 50    
        
        screen.blit(fish,(foodxList[i], foodyList[i]))
    display.flip()

def spawn (screen):
    #birth rate setup***************************************************************
    brate = int(value3*(len(bearxList))+1) 
    for i in range(value2):
        foodxList.append(random.randrange(50,1000,50))
        foodyList.append(random.randrange(50,700,50))    
    for i in range (brate):
        vitalityList.append(100)
        ageList.append(0)
        bearxList.append(random.randrange(50,1000,50))
        bearyList.append(random.randrange(50,700,50))
        display.flip()

#*******************************************************************************



running = True
page = 1
highlighted1 = False
highlighted2 = False
highlighted3 = False
userHab = 0

value = 40
value2 = 0
value3 = 0.1
button = 0
mx=0
my=0


#lists**************************************************************************
vitalityList = []
bearxList = []
bearyList = []
ageList = []
foodxList = []
foodyList = []
waterxList = []
wateryList = []



#list number setup**************************************************************
for i in range (10):
    vitalityList.append(100)
    ageList.append(0)
    bearxList.append(random.randrange(50,1000,50))
    bearyList.append(random.randrange(50,700,50))
for i in range (10):
    foodxList.append(random.randrange(50,1000,50))
    foodyList.append(random.randrange(50,700,50))

myList = []
thickness = []
iceTimer = time.get_ticks()







while running:
    bearFile = open("in.dat", "w")
    bearNum = (len(bearxList))
    if bearNum != 0:
        bearFile.write(str(bearNum))
            
    
    bearFile.close()    
    
    bearFile=open("in.dat","r") #readthefile
    
    
    
    for evnt in event.get():
        if evnt.type==MOUSEBUTTONDOWN:
            mx,my=evnt.pos
            button=evnt.button

            if 455<=mx<=550 and 590<=my<=690 and button==1 and page==1: #if go button clicked
                page=2
                userHab = value
                for y in range(1,userHab+1):
                    myList.append(1)
                for y in range(1,281-userHab):
                    myList.append(0)
                random.shuffle(myList)
                
                for i in range(len(myList)):
                    if myList[i] == 1:
                        ice = random.randint(1, 255)
                    else:
                        ice = 0
                    thickness.append(ice)                


            #if the user clicks the scale and is within the limits, the circle moves
            if button==1 and 500<=mx<=740 and 330<my<350:
                MOVING=True

            elif button==1 and 500<=mx<=740 and 430<my<450:
                MOVING2=True   

            elif button==1 and 500<=mx<=740 and 530<my<550:
                MOVING3=True


        if evnt.type==MOUSEBUTTONUP:
            #the circle stops following the mouse after the user stops holding down the mouse
            if button==1:
                MOVING=False
                MOVING2 = False
                MOVING3=False




        if evnt.type==MOUSEMOTION: #while mouse moving
            mx,my=evnt.pos

            #stops the scircle from moving beyond the scale
            if MOVING==True:
                x=mx
                if mx<510:
                    x=510
                elif mx>730:
                    x=730


                    #assigns values to certain positions on the habitat scale   
                if 510<=x<=541:
                    value = 40

                elif 541<x<=572:
                    value = 80

                elif 572<x<=603:
                    value = 120

                elif 603<x<=634:
                    value = 160

                elif 634<x<=665:
                    value = 200

                elif 665<x<=696:
                    value = 240

                else:
                    value = 280        



        #assigns values to certain positions on the food scale
            if MOVING2==True:
                x2=mx
                if mx<510:
                    x2=510
                elif mx>730:
                    x2=730      

                if 510<=x2<=530:
                    value2 = 0

                elif 530<x2<=550:
                    value2 = 1

                elif 550<x2<=570:
                    value2 = 2

                elif 570<x2<=590:
                    value2 = 3

                elif 590<x2<=610:
                    value2 = 4

                elif 610<x2<=630:
                    value2 = 5

                elif 630<x2<=650:
                    value2 = 6

                elif 650<x2<=670:
                    value2 = 7

                elif 670<x2<=690:
                    value2 = 8 

                elif 690<x2<=710:
                    value2 = 9

                else:
                    value2 = 10              

            #assigns values to positions on birth rate scale
            if MOVING3==True:
                x3=mx
                if mx<510:
                    x3=510
                elif mx>730:
                    x3=730        


                if 510<=x3<=530:
                    value3 = 0.1

                elif 530<x3<=550:
                    value3 = 0.2

                elif 550<x3<=570:
                    value3 = 0.3

                elif 570<x3<=590:
                    value3 = 0.4

                elif 590<x3<=610:
                    value3 = 0.5

                elif 610<x3<=630:
                    value3 = 0.6

                elif 630<x3<=650:
                    value3 = 0.7

                elif 650<x3<=670:
                    value3 = 0.8

                elif 670<x3<=690:
                    value3 = 0.9

                elif 690<x3<=710:
                    value3 = 0.1

                else:
                    value3 = 0.11     
                    
                    

        if evnt.type == QUIT:
            running = False
            
            
    if page == 1:
        drawScene(screen,button,mx,my)

    elif page == 2:     
        drawScene2(screen, button, mx, my, myList)
        food(screen,foodxList,foodyList)
        bear(screen,vitalityList,bearxList,bearyList,ageList)    
        spawn(screen)
        time.wait(100)
        if time.get_ticks() - iceTimer > 100:
            for i in range(len(myList)):
                if myList[i] == 1:
                    thickness[i] -= 1
                    if thickness[i] == 0:
                        myList[i] = 0
            #adjust my ice thickness
            iceTimer = time.get_ticks()   
            
quit()