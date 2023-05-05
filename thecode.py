
#########initial = S Y

#####you are a blackberry cube
#####you are in middle of an war between the orange gang and the blackberry community, and as a part of the blackberry community.
#####your ultimate goal is to make it out here alive quary for more reinforcement.
#####this game is insanely hard, because I'm trying to simulate the actually scenerio. In a normal case, this separate group of 
#####blackberries are pushed against a corner and waiting for it's death impending. 
#####the entire maze is split into 4 parts.
###orangeberry -- the hardest part in this maze, the region took over by the intruder orange gang.
###blackberry -- our starting location.
###whiteberry -- a no mans land hidden inside a thick layer of salt, extremely lethal for berries, with an augmented salt wall created by oranges.
###blueberry forest -- where the ultimate salt melter located, somewhere inside this 5 km thick in width of blue world.
#####there are 6 types of stars 
###normal black star ----- for collective purpose.
###blue star ----- tells us where the ultimate salt melter located.
###gold star ----- the ultimate salt melter.
###the gradient star ----- explosive used to destory the salt wall.
###the green star ----- the main troops of blackberry community.
###and one mysterious star ----- can have really bad consequence if being touched.


background = Rect(0, 0, 400, 400, fill = "white")
Player = Rect(385, 15, 5, 5)
Rect(0, 0, 35, 35, fill=None, border="red")

r1 = Label(0, 5, 6)
r2 = Label(0, 14, 6)
r3 = Label(0, 23, 6)
r4 = Label(0, 32, 6)
blue = Label(0, 7, 20, fill = "blue", size = 15)
gold = Label(0, 28, 20, fill = "gold", size = 15)
red = Label(0, 17.5, 20, fill = "red", size = 15)
reguStar = Star(318, 113, 5, 5,visible = True)
reguStar2 = Star(200, 30, 5, 5, visible = True)
reguStar3 = Star(5 ,185 , 3, 5, visible = True)
reguStar4 = Star(250, 140, 5, 5, visible = True)
cheatingStar = Star(105, 125, 3, 5, visible = True, fill= "darkred")
blueStar = Star(75, 60, 3, 5, fill="blue", visible = True)
colorStar = Star(195, 225, 5, 5, visible = True, fill = 'gold')
doorStar = Star(55, 252.5, 4, 5, visible =True, fill = gradient("yellow", "red", "Yellow", "red"))
winStar = Star(5, 302.5, 3, 5, fill="yellowgreen", visible = True)
sugar = Label("The sugar melted", 200, 350, fill="white", visible = False, size = 40)

Line(0, 0, 400, 0)
Line(400, 0, 400, 400)
Line(400, 400, 0, 400)
Line(0, 400, 0, 0)


###Section1
#wall1
Rect(370, 0, 1, 150)
#wall2
Rect(320, 149, 50, 1)
#wall3
Rect(300, 170, 100, 1)
#wall4
Rect(300, 60, 1, 110)
#wall5
Rect(300, 129, 50, 1)
#wall6
Rect(350, 20, 1, 110)
#wall7
Rect(300, 100, 30, 1)
#wall8
Rect(300, 60, 30, 1)
#wall9
Rect(300, 20, 50, 1)
#wall10
Rect(280, 40, 50, 1)
#wall11
Rect(280, 40, 1, 110)
#wall12
Rect(240, 150, 40, 1)
#wall13
Rect(240, 60, 1, 90)
#wall14
Rect(240, 80, 20, 1)
#wall15
Rect(240, 130, 20, 1)
#wall16
Rect(240, 100, 20, 1)
#wall17
Rect(240, 60, 20, 1)
#wall18
Rect(245, 40, 1, 20)
#wall19
Rect(230, 40, 30, 1)
#wall20
Rect(150, 20, 110, 1)
#wall21
Rect(210, 20, 1, 80)
#wall22
Rect(190, 120, 30, 1)
#wall23
Rect(210, 120, 1, 30)
#wall24
Rect(150, 150, 90, 1)
#wall25
Rect(190, 40, 20, 1)
#wall26
Rect(170, 60, 40, 1)
#wall27
Rect(150, 20, 1, 60)
#wall28
Rect(190, 80, 1, 40)
#wall29
Rect(150, 80, 40, 1)
#wall30
Rect(150, 90, 20, 1)
#wall31
Rect(170, 90, 1, 40)
#wall32
Rect(150, 130, 20, 1)
#wall33
Rect(150, 100, 1, 30)

###Section2(the pain in the apple)
#wall1
Rect(130, 0, 1, 90, fill="orange")
#wall2
Rect(130, 90, 20, 1, fill="orange")
#wall3
Rect(140, 20, 10, 1, fill="orange")
#wall4
Rect(140, 100, 1, 50, fill="orange")
#wall5
Rect(140, 150, 10, 1, fill="orange")
#wall6
Rect(120, 100, 20, 1, fill="orange")
#wall7
Rect(120, 10, 1, 90, fill="orange")
#wall8
Rect(60, 10, 60, 1, fill="orange")
#wall9
Rect(60, 10, 1, 10, fill="orange")
#wall10
Rect(60, 20, 45, 1, fill="orange")
#wall11
Rect(50, 0, 1, 30, fill="orange")
#wall12
Rect(40, 30, 70, 1, fill="orange")
#wall13
Rect(40, 10, 1, 20, fill="orange")
#wall14
Rect(10, 40, 110, 1, fill="orange")
#wall15
Rect(20, 100, 100, 1, fill="orange")
#wall16
Rect(10, 40, 1, 60, fill="orange")
#wall17
Rect(10, 50, 40, 1, fill="orange")
#wall18
Rect(50, 50, 1, 40, fill="orange")
#wall19
Rect(50, 90, 60, 1, fill="orange")
#wall20
Rect(110, 80, 1, 10, fill="orange")
#wall21
Rect(90, 80, 20, 1, fill="orange")
#wall22
Rect(90, 50, 1, 30, fill="orange")
#wall23
Rect(70, 50, 20, 1, fill="orange")
#wall24
Rect(70, 50, 1, 30, fill="orange")
#wall25
Rect(20, 60, 1, 30, fill="orange")
#wall26
Rect(20, 60, 20, 1, fill="orange")
#wall27
Rect(40, 60, 1, 30, fill="orange")
#wall28
Rect(40, 90, 10, 1, fill="orange")
#wall29
Rect(30, 60, 1, 30, fill="orange")
#wall30
Rect(60, 50, 1, 40, fill="orange")
#wall31
Rect(80, 50, 1, 40, fill="orange")
#wall32
Rect(0, 110, 120, 1, fill="orange")
#wall33
Rect(60, 110, 1, 30, fill="orange")
#wall34
Rect(0, 120, 50, 1, fill="orange")
#wall35
Rect(50, 120, 1, 30, fill="orange")
#wall36
Rect(110, 110, 1, 40, fill="orange")
#wall37
Rect(70, 120, 60, 1, fill="orange")
#wall38
Rect(130, 120, 1, 30, fill="orange")
#wall39
Rect(120, 150, 10, 1, fill="orange")
#wall40
Rect(120, 130, 1, 20, fill="orange")
#wall41
Rect(100, 120, 1, 45, fill="orange")
#wall42
Rect(70, 130, 40, 1, fill="orange")
#wall43
Rect(70, 140, 30, 1, fill="orange")
#wall44
Rect(40, 130, 1, 20, fill="orange")
#wall45
Rect(10, 130, 30, 1, fill="orange")
#wall46
Rect(10, 130, 1, 10, fill="orange")
#wall47
Rect(10, 140, 20, 1, fill="orange")
#wall48
Rect(0, 150, 40, 1, fill="orange")

###Section3 (to change background color)
#wall1
Rect(260, 170, 20, 1, fill="blue")
#wall2
Rect(150, 170, 40, 1, fill="blue")
#wall3
Rect(190, 170, 1, 30, fill="blue")
#wall4
Rect(260, 170, 1, 30, fill="blue")
#wall5
Rect(190, 200, 30, 1, fill="blue")
#wall6
Rect(220, 170, 1, 60, fill="blue")
#wall7
Rect(260, 200, 60, 1, fill="blue")
#wall8
Rect(320, 200, 1, 10, fill="blue")
#wall9
Rect(290, 200, 1, 30, fill="blue")
#wall10
Rect(220, 230, 70, 1, fill="blue")
#wall11
Rect(240, 200, 1, 80, fill="blue")
#wall12
Rect(220, 255, 20, 1, fill="blue")
#wall13
Rect(220, 242.5, 1, 37.5, fill="blue")
#wall14
Rect(205, 243, 15, 1, fill="blue")
#wall15
Rect(205, 243, 1, 12, fill="blue")
#wall16
Rect(185, 255, 21, 1, fill="blue")
#wall17
Rect(185, 255, 1, 25, fill="blue")
#wall18
Rect(170, 185, 1, 95, fill="blue")
#wall19
Rect(170, 280, 15, 1, fill="blue")
#wall20(4 sides needed)
blueBox = Rect(185, 215, 20, 20, fill=None, border="blue", borderWidth = 1, visible = True)
#wall21
Rect(280, 230, 1, 50, fill="blue")
#wall22
Rect(260, 255, 60, 1, fill="blue")
#wall23
Rect(260, 255, 1, 25, fill="blue")
#wall24
Rect(280, 280, 40, 1, fill="blue")
#wall25
Rect(340, 200, 30, 1, fill="blue")
#wall26
Rect(340, 200, 1, 100, fill="blue")
#wall27
Rect(370, 200, 1, 56, fill="blue")
#wall28
Rect(355, 255, 15, 1, fill="blue")
#wall29
Rect(355, 255, 1, 25, fill="blue")
#wall30
Rect(355, 280, 25, 1, fill="blue")
#wall31
Rect(350, 215, 20, 1, fill="blue")
#wall32
Rect(350, 230, 20, 1, fill="blue")

###Section4(color change also the final stage)
#wall1
Rect(150, 150, 1, 150, fill = "blue")
#wall2
Rect(0, 160, 10, 1, fill = "orange")
#wall3
Rect(20, 160, 20, 1, fill = "orange")
#wall4
Rect(60, 160, 30, 1, fill = "orange")
#wall5
Rect(60, 160, 1, 20, fill = "orange")
#wall6
Rect(40, 160, 1, 20, fill = "orange")
#wall7
Rect(0, 180, 40, 1, fill = "orange")
#wall8
Rect(60, 180, 50, 1, fill = "orange")
#wall9
Rect(20, 180, 1, 20, fill = "white")
#wall10
Rect(10, 200, 20, 1, fill = "white")
#wall11
Rect(10, 200, 1, 10, fill = "white")
#wall12
Rect(10, 210, 10, 1, fill = "white")
#wall13
Rect(20, 210, 1, 30, fill = "white")
#wall14
Rect(20, 240, 10, 1, fill = "white")
#wall15
Rect(30, 220, 1, 20, fill = "white")
#wall16
Rect(110, 160, 1, 55, fill = "orange")
#wall17
Rect(30, 220, 10, 1, fill = "white")
#wall18
Rect(40, 210, 1, 10, fill = "white")
#wall19
Rect(40, 230, 1, 60, fill = "white")
#wall20
Rect(0, 230, 10, 1, fill = "white")
#wall21
Rect(10, 230, 1, 60, fill = "white")
#wall22
Rect(30, 240, 1, 50, fill = "white")
#wall23
Rect(40, 170, 20, 1, fill = "orange")
#wall24
Rect(0, 190, 10, 1, fill = "white")
#wall25
Rect(10, 250, 10, 1, fill = "white")
#wall26
Rect(10, 260, 10, 1, fill = "white")
#wall27
Rect(10, 270, 10, 1, fill = "white")
#wall28
Rect(10, 280, 10, 1, fill = "white")
#wall29
Rect(10, 290, 10, 1, fill = "white")
#wall30 
theDoor = Rect(50, 210, 1, 90, fill = "red", visible = True)
#wall31
Rect(40, 290, 10, 1, fill = "white")
#wall32
Rect(50, 210, 20, 1, fill = "white")
#wall33
Rect(70, 180, 1, 30, fill = "white")
#wall34
Rect(50, 200, 10, 1, fill = "white")
#wall35
Rect(60, 200, 1, 20, fill = "white")
#wall36
Rect(60, 220, 10, 1, fill = "white")
#wall37
Rect(50, 230, 30, 1, fill = "white")
#wall38
Rect(80, 200, 1, 30, fill = "white")
#wall39
Rect(80, 200, 20, 1, fill = "white")
#wall40
Rect(90, 200, 1, 30, fill = "white")
#wall41
Rect(90, 230, 10, 1, fill = "white")
#wall42
Rect(100, 215, 1, 16, fill = "white")
#wall43
Rect(110, 215, 20, 1, fill = "orange")
#wall44
Rect(140, 170, 10, 1, fill = "white")
#wall45
Rect(140, 170, 1, 120, fill = "white")
#wall46
Rect(130, 180, 1, 35, fill = "orange")
#wall47
Rect(120, 180, 10, 1, fill = "orange")
#wall48
Rect(120, 180, 1, 20, fill = "orange")
#wall49
Rect(50, 245, 60, 1, fill = "white")
#wall50
Rect(110, 230, 1, 15, fill = "white")
#wall51
Rect(120, 230, 1, 15, fill = "white")
#wall52
Rect(120, 245, 10, 1, fill = "white")
#wall53
Rect(130, 245, 1, 45, fill = "white")
#wall54
Rect(120, 255, 1, 45, fill = "white")
#wall55
Rect(90, 255, 30, 1, fill = "white")
#wall56
Rect(80, 275, 30, 1, fill = "white")
#wall57
Rect(90, 255, 1, 10, fill = "white")
#wall58
Rect(90, 265, 20, 1, fill = "white")
#wall59
Rect(50, 260, 10, 1, fill = "white")
#wall60
Rect(80, 245, 1, 30, fill = "white")
#wall61
Rect(60, 260, 1, 30, fill = "white")
#wall62
Rect(70, 260, 1, 30, fill = "white")
#wall62
Rect(60, 290, 50, 1, fill = "white")

#when you lose
lose = Rect(0, 0, 400, 400, fill = "red", visible = False)


#final line
Rect(10, 300, 400, 5, fill="red")

#Initial cover
telep_prev = Polygon(0, 0, 371, 0, 371, 30, 400, 30, 400, 400, 0, 400, fill = "red")
Init_msg = Label("Drag the mouse to start this game", 200, 300, size = 20)


def onMouseRelease(x, y):
    if winStar.visible == True:
        lose.visible = True
        Label("YOU ARE DEAD, RESTART THE GAME!", 200, 350, size = 20)
        Player.centerX = 385
        Player.centerY = 15
        sugar.visible = False
def onMouseDrag (mouseX, mouseY):
    if telep_prev.visible == False:
        Init_msg.visible = False
        Player.centerX = mouseX
        Player.centerY = mouseY
    else:
        if mouseX < 371 or mouseY > 30:
            lose.visible = True
            Init_msg.visible = False
            Label("YOU ARE DEAD, RESTART THE GAME!", 200, 350, size = 20)
        else:
            telep_prev.visible = False
    
    ###before sugar melted
    if colorStar.visible == True:
        if Player.centerX-2.5 < 200 and Player.centerY-2.5 < 130 and Player.centerX+2.5 > 201 and Player.centerY+2.5 > 150:
            onMouseRelease(mouseX, mouseY)
    ###final line reset
    if Player.centerY-2.5 < 305 and Player.centerX+2.5 > 10 and Player.centerY+2.5 > 300:
        onMouseRelease(mouseX, mouseY)
        
    ###Section 1 resets
    #wall1
    if Player.centerX-2.5 < 371 and Player.centerY-2.5 < 150 and Player.centerX+2.5 > 370 and Player.centerY+2.5 > 0:
        onMouseRelease(mouseX, mouseY)
        
    #wall2
    if Player.centerY-2.5 < 150 and Player.centerX+2.5 > 320 and Player.centerY+2.5 > 149 and Player.centerX-2.5 < 370:
        onMouseRelease(mouseX, mouseY)
        
    #wall3
    if Player.centerY-2.5 < 171 and Player.centerX+2.5 > 300 and Player.centerY+2.5 > 170 and Player.centerX-2.5 < 400:
        onMouseRelease(mouseX, mouseY)  
    #wall4
    if Player.centerX-2.5 < 301 and Player.centerY-2.5 < 170 and Player.centerX+2.5 > 300 and Player.centerY+2.5 > 60:
        onMouseRelease(mouseX, mouseY)
    #wall5
    if Player.centerY-2.5 < 130 and Player.centerX+2.5 > 300 and Player.centerY+2.5 > 129 and Player.centerX-2.5 < 350:
        onMouseRelease(mouseX, mouseY)
    #wall6
    if Player.centerX-2.5 < 351 and Player.centerY-2.5 < 130 and Player.centerX+2.5 > 350 and Player.centerY+2.5 > 20:
        onMouseRelease(mouseX, mouseY)
         
    #wall7
    if Player.centerY-2.5 < 101 and Player.centerX+2.5 > 300 and Player.centerY+2.5 > 100 and Player.centerX-2.5 < 330:
        onMouseRelease(mouseX, mouseY)
         
    #wall8
    if Player.centerY-2.5 < 60 and Player.centerX+2.5 > 300 and Player.centerY+2.5 > 61 and Player.centerX-2.5 < 330:
        onMouseRelease(mouseX, mouseY)
         
    #wall9
    if Player.centerY-2.5 < 21 and Player.centerX+2.5 > 300 and Player.centerY+2.5 > 20 and Player.centerX-2.5 < 350:
        onMouseRelease(mouseX, mouseY)
         
    #wall10
    if Player.centerY-2.5 < 41 and Player.centerX+2.5 > 280 and Player.centerY+2.5 > 40 and Player.centerX-2.5 < 330:
        onMouseRelease(mouseX, mouseY)
         
    #wall11
    if Player.centerX-2.5 < 281 and Player.centerY-2.5 < 150 and Player.centerX+2.5 > 280 and Player.centerY+2.5 > 40:
        onMouseRelease(mouseX, mouseY)
         
    #wall12
    if Player.centerY-2.5 < 151 and Player.centerX+2.5 > 240 and Player.centerY+2.5 > 150 and Player.centerX-2.5 < 280:
        onMouseRelease(mouseX, mouseY)
         
    #wall13
    if Player.centerX-2.5 < 241 and Player.centerY-2.5 < 150 and Player.centerX+2.5 > 240 and Player.centerY+2.5 > 60:
        onMouseRelease(mouseX, mouseY)
         
    #wall14
    if Player.centerY-2.5 < 81 and Player.centerX+2.5 > 240 and Player.centerY+2.5 > 80 and Player.centerX-2.5 < 260:
        onMouseRelease(mouseX, mouseY)
         
    #wall15
    if Player.centerY-2.5 < 131 and Player.centerX+2.5 > 240 and Player.centerY+2.5 > 130 and Player.centerX-2.5 < 260:
        onMouseRelease(mouseX, mouseY)
         
    #wall16
    if Player.centerY-2.5 < 101 and Player.centerX+2.5 > 240 and Player.centerY+2.5 > 100 and Player.centerX-2.5 < 260:
        onMouseRelease(mouseX, mouseY)
         
    #wall17
    if Player.centerY-2.5 < 61 and Player.centerX+2.5 > 240 and Player.centerY+2.5 > 60 and Player.centerX-2.5 < 260:
        onMouseRelease(mouseX, mouseY)
         
    #wall18
    if Player.centerX-2.5 < 246 and Player.centerY-2.5 < 60 and Player.centerX+2.5 > 245 and Player.centerY+2.5 > 40:
        onMouseRelease(mouseX, mouseY)
         
    #wall19
    if Player.centerY-2.5 < 41 and Player.centerX+2.5 > 230 and Player.centerY+2.5 > 40 and Player.centerX-2.5 < 260:
        onMouseRelease(mouseX, mouseY)
         
    #wall20
    if Player.centerY-2.5 < 21 and Player.centerX+2.5 > 150 and Player.centerY+2.5 > 20 and Player.centerX-2.5 < 260:
        onMouseRelease(mouseX, mouseY)
         
    #wall21
    if Player.centerX-2.5 < 211 and Player.centerY-2.5 < 100 and Player.centerX+2.5 > 210 and Player.centerY+2.5 > 20:
        onMouseRelease(mouseX, mouseY)
         
    #wall22
    if Player.centerY-2.5 < 121 and Player.centerX+2.5 > 190 and Player.centerY+2.5 > 120 and Player.centerX-2.5 < 220:
        onMouseRelease(mouseX, mouseY)
         
    #wall23
    if Player.centerX-2.5 < 211 and Player.centerY-2.5 < 150 and Player.centerX+2.5 > 210 and Player.centerY+2.5 > 120:
        onMouseRelease(mouseX, mouseY)
         
    #wall24
    if Player.centerY-2.5 < 151 and Player.centerX+2.5 > 150 and Player.centerY+2.5 > 150 and Player.centerX-2.5 < 240:
        onMouseRelease(mouseX, mouseY)
         
    #wall25
    if Player.centerY-2.5 < 41 and Player.centerX+2.5 > 190 and Player.centerY+2.5 > 40 and Player.centerX-2.5 < 210:
        onMouseRelease(mouseX, mouseY)
         
    #wall26
    if Player.centerY-2.5 < 61 and Player.centerX+2.5 > 170 and Player.centerY+2.5 > 60 and Player.centerX-2.5 < 210:
        onMouseRelease(mouseX, mouseY)
         
    #wall27
    if Player.centerX-2.5 < 151 and Player.centerY-2.5 < 80 and Player.centerX+2.5 > 150 and Player.centerY+2.5 > 20:
        onMouseRelease(mouseX, mouseY)
         
    #wall28
    if Player.centerX-2.5 < 191 and Player.centerY-2.5 < 120 and Player.centerX+2.5 > 190 and Player.centerY+2.5 > 80:
        onMouseRelease(mouseX, mouseY)
         
    #wall29
    if Player.centerY-2.5 < 81 and Player.centerX+2.5 > 150 and Player.centerY+2.5 > 80 and Player.centerX-2.5 < 190:
        onMouseRelease(mouseX, mouseY)
         
    #wall30
    if Player.centerY-2.5 < 91 and Player.centerX+2.5 > 150 and Player.centerY+2.5 > 90 and Player.centerX-2.5 < 170:
        onMouseRelease(mouseX, mouseY)
         
    #wall31
    if Player.centerX-2.5 < 171 and Player.centerY-2.5 < 130 and Player.centerX+2.5 > 170 and Player.centerY+2.5 > 90:
        onMouseRelease(mouseX, mouseY)
          
    #wall32
    if Player.centerY-2.5 < 131 and Player.centerX+2.5 > 150 and Player.centerY+2.5 > 130 and Player.centerX-2.5 < 170:
        onMouseRelease(mouseX, mouseY)
         
    #wall33
    if Player.centerX-2.5 < 151 and Player.centerY-2.5 < 130 and Player.centerX+2.5 > 150 and Player.centerY+2.5 > 100:
        onMouseRelease(mouseX, mouseY)
         
    
    ###Section 2 resets
    #wall1
    if Player.centerX-2.5 < 131 and Player.centerY-2.5 < 90 and Player.centerX+2.5 > 130 and Player.centerY+2.5 > 0:
        onMouseRelease(mouseX, mouseY)
         
    #wall2
    if Player.centerY-2.5 < 91 and Player.centerX+2.5 > 130 and Player.centerY+2.5 > 90 and Player.centerX-2.5 < 150:
        onMouseRelease(mouseX, mouseY)
         
    #wall3
    if Player.centerY-2.5 < 21 and Player.centerX+2.5 > 140 and Player.centerY+2.5 > 20 and Player.centerX-2.5 < 150:
        onMouseRelease(mouseX, mouseY)
         
    #wall4
    if Player.centerX-2.5 < 141 and Player.centerY-2.5 < 150 and Player.centerX+2.5 > 140 and Player.centerY+2.5 > 100:
        onMouseRelease(mouseX, mouseY)
         
    #wall5
    if Player.centerY-2.5 < 151 and Player.centerX+2.5 > 140 and Player.centerY+2.5 > 150 and Player.centerX-2.5 < 150:
        onMouseRelease(mouseX, mouseY)
         
    #wall6
    if Player.centerY-2.5 < 101 and Player.centerX+2.5 > 120 and Player.centerY+2.5 > 100 and Player.centerX-2.5 < 140:
        onMouseRelease(mouseX, mouseY)
         
    #wall7
    if Player.centerX-2.5 < 121 and Player.centerY-2.5 < 100 and Player.centerX+2.5 > 120 and Player.centerY+2.5 > 10:
        onMouseRelease(mouseX, mouseY)
         
    #wall8
    if Player.centerY-2.5 < 11 and Player.centerX+2.5 > 60 and Player.centerY+2.5 > 10 and Player.centerX-2.5 < 120:
        onMouseRelease(mouseX, mouseY)
         
    #wall9
    if Player.centerX-2.5 < 60 and Player.centerY-2.5 < 20 and Player.centerX+2.5 > 61 and Player.centerY+2.5 > 10:
        onMouseRelease(mouseX, mouseY)
         
    #wall10
    if Player.centerY-2.5 < 21 and Player.centerX+2.5 > 60 and Player.centerY+2.5 > 20 and Player.centerX-2.5 < 105:
        onMouseRelease(mouseX, mouseY)
         
    #wall11
    if Player.centerX-2.5 < 51 and Player.centerY-2.5 < 30 and Player.centerX+2.5 > 50 and Player.centerY+2.5 > 0:
        onMouseRelease(mouseX, mouseY)
         
    #wall12
    if Player.centerY-2.5 < 31 and Player.centerX+2.5 > 40 and Player.centerY+2.5 > 30 and Player.centerX-2.5 < 110:
        onMouseRelease(mouseX, mouseY)
         
    #wall13
    if Player.centerX-2.5 < 41 and Player.centerY-2.5 < 30 and Player.centerX+2.5 > 40 and Player.centerY+2.5 > 10:
        onMouseRelease(mouseX, mouseY)
         
    #wall14
    if Player.centerY-2.5 < 41 and Player.centerX+2.5 > 10 and Player.centerY+2.5 > 40 and Player.centerX-2.5 < 120:
        onMouseRelease(mouseX, mouseY)
         
    #wall15
    if Player.centerY-2.5 < 101 and Player.centerX+2.5 > 20 and Player.centerY+2.5 > 100 and Player.centerX-2.5 < 120:
        onMouseRelease(mouseX, mouseY)
         
    #wall16
    if Player.centerX-2.5 < 11 and Player.centerY-2.5 < 100 and Player.centerX+2.5 > 10 and Player.centerY+2.5 > 40:
        onMouseRelease(mouseX, mouseY)
         
    #wall17
    if Player.centerY-2.5 < 51 and Player.centerX+2.5 > 10 and Player.centerY+2.5 > 50 and Player.centerX-2.5 < 50:
        onMouseRelease(mouseX, mouseY)
         
    #wall18
    if Player.centerX-2.5 < 51 and Player.centerY-2.5 < 90 and Player.centerX+2.5 > 50 and Player.centerY+2.5 > 50:
        onMouseRelease(mouseX, mouseY)
         
    #wall19
    if Player.centerY-2.5 < 91 and Player.centerX+2.5 > 50 and Player.centerY+2.5 > 90 and Player.centerX-2.5 < 110:
        onMouseRelease(mouseX, mouseY)
         
    #wall20
    if Player.centerX-2.5 < 111 and Player.centerY-2.5 < 90 and Player.centerX+2.5 > 110 and Player.centerY+2.5 > 80:
        onMouseRelease(mouseX, mouseY)
         
    #wall21
    if Player.centerY-2.5 < 81 and Player.centerX+2.5 > 90 and Player.centerY+2.5 > 80 and Player.centerX-2.5 < 110:
        onMouseRelease(mouseX, mouseY)
         
    #wall22
    if Player.centerX-2.5 < 91 and Player.centerY-2.5 < 80 and Player.centerX+2.5 > 90 and Player.centerY+2.5 > 50:
        onMouseRelease(mouseX, mouseY)
         
    #wall23
    if Player.centerY-2.5 < 51 and Player.centerX+2.5 > 70 and Player.centerY+2.5 > 50 and Player.centerX-2.5 < 90:
        onMouseRelease(mouseX, mouseY)
         
    #wall24
    if Player.centerX-2.5 < 71 and Player.centerY-2.5 < 80 and Player.centerX+2.5 > 70 and Player.centerY+2.5 > 50:
        onMouseRelease(mouseX, mouseY)
         
    #wall25
    if Player.centerX-2.5 < 21 and Player.centerY-2.5 < 90 and Player.centerX+2.5 > 20 and Player.centerY+2.5 > 60:
        onMouseRelease(mouseX, mouseY)
         
    #wall26
    if Player.centerY-2.5 < 61 and Player.centerX+2.5 > 20 and Player.centerY+2.5 > 60 and Player.centerX-2.5 < 40:
        onMouseRelease(mouseX, mouseY)
         
    #wall27
    if Player.centerX-2.5 < 41 and Player.centerY-2.5 < 90 and Player.centerX+2.5 > 40 and Player.centerY+2.5 > 40:
        onMouseRelease(mouseX, mouseY)
         
    #wall28
    if Player.centerY-2.5 < 91 and Player.centerX+2.5 > 40 and Player.centerY+2.5 > 90 and Player.centerX-2.5 < 50:
        onMouseRelease(mouseX, mouseY)
         
    #wall29
    if Player.centerX-2.5 < 31 and Player.centerY-2.5 < 90 and Player.centerX+2.5 > 30 and Player.centerY+2.5 > 60:
        onMouseRelease(mouseX, mouseY)
         
    #wall30
    if Player.centerX-2.5 < 61 and Player.centerY-2.5 < 90 and Player.centerX+2.5 > 60 and Player.centerY+2.5 > 50:
        onMouseRelease(mouseX, mouseY)
         
    #wall31
    if Player.centerX-2.5 < 81 and Player.centerY-2.5 < 90 and Player.centerX+2.5 > 80 and Player.centerY+2.5 > 50:
        onMouseRelease(mouseX, mouseY)
         
    #wall32
    if Player.centerY-2.5 < 111 and Player.centerX+2.5 > 0 and Player.centerY+2.5 > 110 and Player.centerX-2.5 < 120:
        onMouseRelease(mouseX, mouseY)
         
    #wall33
    if Player.centerX-2.5 < 61 and Player.centerY-2.5 < 140 and Player.centerX+2.5 > 60 and Player.centerY+2.5 > 110:
        onMouseRelease(mouseX, mouseY)
         
    #wall34
    if Player.centerY-2.5 < 121 and Player.centerX+2.5 > 0 and Player.centerY+2.5 > 120 and Player.centerX-2.5 < 50:
        onMouseRelease(mouseX, mouseY)
         
    #wall35
    if Player.centerX-2.5 < 51 and Player.centerY-2.5 < 150 and Player.centerX+2.5 > 50 and Player.centerY+2.5 > 120:
        onMouseRelease(mouseX, mouseY)
         
    #wall36
    if Player.centerX-2.5 < 111 and Player.centerY-2.5 < 150 and Player.centerX+2.5 > 110 and Player.centerY+2.5 > 110:
        onMouseRelease(mouseX, mouseY)
         
    #wall37
    if Player.centerY-2.5 < 121 and Player.centerX+2.5 > 70 and Player.centerY+2.5 > 120 and Player.centerX-2.5 < 130:
        onMouseRelease(mouseX, mouseY)
         
    #wall38
    if Player.centerX-2.5 < 131 and Player.centerY-2.5 < 150 and Player.centerX+2.5 > 130 and Player.centerY+2.5 > 120:
        onMouseRelease(mouseX, mouseY)
         
    #wall39
    if Player.centerY-2.5 < 151 and Player.centerX+2.5 > 120 and Player.centerY+2.5 > 150 and Player.centerX-2.5 < 130:
        onMouseRelease(mouseX, mouseY)
         
    #wall40
    if Player.centerX-2.5 < 121 and Player.centerY-2.5 < 150 and Player.centerX+2.5 > 120 and Player.centerY+2.5 > 130:
        onMouseRelease(mouseX, mouseY)
         
    #wall41
    if Player.centerX-2.5 < 101 and Player.centerY-2.5 < 165 and Player.centerX+2.5 > 100 and Player.centerY+2.5 > 120:
        onMouseRelease(mouseX, mouseY)
         
    #wall42
    if Player.centerY-2.5 < 131 and Player.centerX+2.5 > 70 and Player.centerY+2.5 > 130 and Player.centerX-2.5 < 110:
        onMouseRelease(mouseX, mouseY)
         
    #wall43
    if Player.centerY-2.5 < 141 and Player.centerX+2.5 > 70 and Player.centerY+2.5 > 140 and Player.centerX-2.5 < 100:
        onMouseRelease(mouseX, mouseY)
         
    #wall44
    if Player.centerX-2.5 < 41 and Player.centerY-2.5 < 150 and Player.centerX+2.5 > 40 and Player.centerY+2.5 > 130:
        onMouseRelease(mouseX, mouseY)
         
    #wall45
    if Player.centerY-2.5 < 131 and Player.centerX+2.5 > 10 and Player.centerY+2.5 > 130 and Player.centerX-2.5 < 40:
        onMouseRelease(mouseX, mouseY)
         
    #wall46
    if Player.centerX-2.5 < 11 and Player.centerY-2.5 < 140 and Player.centerX+2.5 > 10 and Player.centerY+2.5 > 130:
        onMouseRelease(mouseX, mouseY)
         
    #wall47
    if Player.centerY-2.5 < 141 and Player.centerX+2.5 > 10 and Player.centerY+2.5 > 140 and Player.centerX-2.5 < 30:
        onMouseRelease(mouseX, mouseY)
         
    #wall48
    if Player.centerY-2.5 < 151 and Player.centerX+2.5 > 0 and Player.centerY+2.5 > 150 and Player.centerX-2.5 < 40:
        onMouseRelease(mouseX, mouseY)
         
    
    ###Section 3 resets
    #wall1
    if Player.centerY-2.5 < 171 and Player.centerX+2.5 > 260 and Player.centerY+2.5 > 170 and Player.centerX-2.5 < 280:
        onMouseRelease(mouseX, mouseY)
         
    #wall2
    if Player.centerY-2.5 < 171 and Player.centerX+2.5 > 150 and Player.centerY+2.5 > 170 and Player.centerX-2.5 < 190:
        onMouseRelease(mouseX, mouseY)
         
    #wall3
    if Player.centerX-2.5 < 191 and Player.centerY-2.5 < 200 and Player.centerX+2.5 > 190 and Player.centerY+2.5 > 170:
        onMouseRelease(mouseX, mouseY)
         
    #wall4
    if Player.centerX-2.5 < 261 and Player.centerY-2.5 < 200 and Player.centerX+2.5 > 260 and Player.centerY+2.5 > 170:
        onMouseRelease(mouseX, mouseY)
         
    #wall5
    if Player.centerY-2.5 < 201 and Player.centerX+2.5 > 190 and Player.centerY+2.5 > 200 and Player.centerX-2.5 < 220:
        onMouseRelease(mouseX, mouseY)
         
    #wall6
    if Player.centerX-2.5 < 221 and Player.centerY-2.5 < 230 and Player.centerX+2.5 > 220 and Player.centerY+2.5 > 170:
        onMouseRelease(mouseX, mouseY)
         
    #wall7
    if Player.centerY-2.5 < 201 and Player.centerX+2.5 > 260 and Player.centerY+2.5 > 200 and Player.centerX-2.5 < 320:
        onMouseRelease(mouseX, mouseY)
         
    #wall8
    if Player.centerX-2.5 < 321 and Player.centerY-2.5 < 210 and Player.centerX+2.5 > 320 and Player.centerY+2.5 > 200:
        onMouseRelease(mouseX, mouseY)
         
    #wall9
    if Player.centerX-2.5 < 291 and Player.centerY-2.5 < 230 and Player.centerX+2.5 > 290 and Player.centerY+2.5 > 200:
        onMouseRelease(mouseX, mouseY)
         
    #wall10
    if Player.centerY-2.5 < 231 and Player.centerX+2.5 > 220 and Player.centerY+2.5 > 230 and Player.centerX-2.5 < 290:
        onMouseRelease(mouseX, mouseY)
         
    #wall11
    if Player.centerX-2.5 < 241 and Player.centerY-2.5 < 280 and Player.centerX+2.5 > 240 and Player.centerY+2.5 > 200:
        onMouseRelease(mouseX, mouseY)
         
    #wall12
    if Player.centerY-2.5 < 256 and Player.centerX+2.5 > 220 and Player.centerY+2.5 > 255 and Player.centerX-2.5 < 240:
        onMouseRelease(mouseX, mouseY)
         
    #wall13
    if Player.centerX-2.5 < 221 and Player.centerY-2.5 < 280 and Player.centerX+2.5 > 220 and Player.centerY+2.5 > 243:
        onMouseRelease(mouseX, mouseY)
         
    #wall14
    if Player.centerY-2.5 < 244 and Player.centerX+2.5 > 205 and Player.centerY+2.5 > 243 and Player.centerX-2.5 < 220:
        onMouseRelease(mouseX, mouseY)
         
    #wall15
    if Player.centerX-2.5 < 206 and Player.centerY-2.5 < 255 and Player.centerX+2.5 > 205 and Player.centerY+2.5 > 243:
        onMouseRelease(mouseX, mouseY)
         
    #wall16
    if Player.centerY-2.5 < 256 and Player.centerX+2.5 > 185 and Player.centerY+2.5 > 255 and Player.centerX-2.5 < 206:
        onMouseRelease(mouseX, mouseY)
         
    #wall17
    if Player.centerX-2.5 < 186 and Player.centerY-2.5 < 280 and Player.centerX+2.5 > 185 and Player.centerY+2.5 > 255:
        onMouseRelease(mouseX, mouseY)
         
    #wall18
    if Player.centerX-2.5 < 171 and Player.centerY-2.5 < 280 and Player.centerX+2.5 > 170 and Player.centerY+2.5 > 185:
        onMouseRelease(mouseX, mouseY)
         
    #wall19
    if Player.centerY-2.5 < 281 and Player.centerX+2.5 > 170 and Player.centerY+2.5 > 280 and Player.centerX-2.5 < 185:
        onMouseRelease(mouseX, mouseY)
         
    ###blueBox
    #wall20
    if blueBox.visible == True:
        if Player.centerY-2.5 < 235 and Player.centerX+2.5 > 185 and Player.centerY+2.5 > 215 and Player.centerX-2.5 < 205:
            onMouseRelease(mouseX, mouseY)
         
    #wall21
    if Player.centerX-2.5 < 281 and Player.centerY-2.5 < 280 and Player.centerX+2.5 > 280 and Player.centerY+2.5 > 230:
        onMouseRelease(mouseX, mouseY)
         
    #wall22
    if Player.centerY-2.5 < 256 and Player.centerX+2.5 > 260 and Player.centerY+2.5 > 255 and Player.centerX-2.5 < 320:
        onMouseRelease(mouseX, mouseY)
         
    #wall23
    if Player.centerX-2.5 < 261 and Player.centerY-2.5 < 280 and Player.centerX+2.5 > 260 and Player.centerY+2.5 > 255:
        onMouseRelease(mouseX, mouseY)
         
    #wall24
    if Player.centerY-2.5 < 281 and Player.centerX+2.5 > 280 and Player.centerY+2.5 > 280 and Player.centerX-2.5 < 320:
        onMouseRelease(mouseX, mouseY)
         
    #wall25
    if Player.centerY-2.5 < 201 and Player.centerX+2.5 > 340 and Player.centerY+2.5 > 200 and Player.centerX-2.5 < 370:
        onMouseRelease(mouseX, mouseY)
         
    #wall26
    if Player.centerX-2.5 < 341 and Player.centerY-2.5 < 300 and Player.centerX+2.5 > 340 and Player.centerY+2.5 > 200:
        onMouseRelease(mouseX, mouseY)
         
    #wall27
    if Player.centerX-2.5 < 371 and Player.centerY-2.5 < 256 and Player.centerX+2.5 > 370 and Player.centerY+2.5 > 200:
        onMouseRelease(mouseX, mouseY)
         
    #wall28
    if Player.centerY-2.5 < 256 and Player.centerX+2.5 > 355 and Player.centerY+2.5 > 255 and Player.centerX-2.5 < 370:
        onMouseRelease(mouseX, mouseY)
         
    #wall29
    if Player.centerX-2.5 < 356 and Player.centerY-2.5 < 280 and Player.centerX+2.5 > 355 and Player.centerY+2.5 > 255:
        onMouseRelease(mouseX, mouseY)
         
    #wall30
    if Player.centerY-2.5 < 281 and Player.centerX+2.5 > 355 and Player.centerY+2.5 > 280 and Player.centerX-2.5 < 380:
        onMouseRelease(mouseX, mouseY)
         
    #wall31
    if Player.centerY-2.5 < 216 and Player.centerX+2.5 > 350 and Player.centerY+2.5 > 215 and Player.centerX-2.5 < 370:
        onMouseRelease(mouseX, mouseY)
         
    #wall32
    if Player.centerY-2.5 < 231 and Player.centerX+2.5 > 350 and Player.centerY+2.5 > 230 and Player.centerX-2.5 < 370:
        onMouseRelease(mouseX, mouseY)
         
    
    ###Section 4 resets
    #wall1
    if Player.centerX-2.5 < 151 and Player.centerY-2.5 < 300 and Player.centerX+2.5 > 150 and Player.centerY+2.5 > 150:
        onMouseRelease(mouseX, mouseY)
         
    #wall2
    if Player.centerY-2.5 < 161 and Player.centerX+2.5 > 0 and Player.centerY+2.5 > 160 and Player.centerX-2.5 < 10:
        onMouseRelease(mouseX, mouseY)
         
    #wall3
    if Player.centerY-2.5 < 161 and Player.centerX+2.5 > 20 and Player.centerY+2.5 > 160 and Player.centerX-2.5 < 40:
        onMouseRelease(mouseX, mouseY)
         
    #wall4
    if Player.centerY-2.5 < 161 and Player.centerX+2.5 > 60 and Player.centerY+2.5 > 160 and Player.centerX-2.5 < 90:
        onMouseRelease(mouseX, mouseY)
         
    #wall5
    if Player.centerX-2.5 < 61 and Player.centerY-2.5 < 180 and Player.centerX+2.5 > 60 and Player.centerY+2.5 > 160:
        onMouseRelease(mouseX, mouseY)
         
    #wall6
    if Player.centerX-2.5 < 41 and Player.centerY-2.5 < 180 and Player.centerX+2.5 > 40 and Player.centerY+2.5 > 160:
        onMouseRelease(mouseX, mouseY)
         
    #wall7
    if Player.centerY-2.5 < 181 and Player.centerX+2.5 > 0 and Player.centerY+2.5 > 180 and Player.centerX-2.5 < 40:
        onMouseRelease(mouseX, mouseY)
         
    #wall8
    if Player.centerY-2.5 < 181 and Player.centerX+2.5 > 60 and Player.centerY+2.5 > 180 and Player.centerX-2.5 < 110:
        onMouseRelease(mouseX, mouseY)
         
    #wall9
    if Player.centerX-2.5 < 21 and Player.centerY-2.5 < 200 and Player.centerX+2.5 > 20 and Player.centerY+2.5 > 180:
        onMouseRelease(mouseX, mouseY)
         
    #wall10
    if Player.centerY-2.5 < 201 and Player.centerX+2.5 > 10 and Player.centerY+2.5 > 200 and Player.centerX-2.5 < 30:
        onMouseRelease(mouseX, mouseY)
         
    #wall11
    if Player.centerX-2.5 < 11 and Player.centerY-2.5 < 210 and Player.centerX+2.5 > 10 and Player.centerY+2.5 > 200:
        onMouseRelease(mouseX, mouseY)
         
    #wall12
    if Player.centerY-2.5 < 211 and Player.centerX+2.5 > 10 and Player.centerY+2.5 > 210 and Player.centerX-2.5 < 20:
        onMouseRelease(mouseX, mouseY)
         
    #wall13
    if Player.centerX-2.5 < 21 and Player.centerY-2.5 < 240 and Player.centerX+2.5 > 20 and Player.centerY+2.5 > 210:
        onMouseRelease(mouseX, mouseY)
         
    #wall14
    if Player.centerY-2.5 < 241 and Player.centerX+2.5 > 20 and Player.centerY+2.5 > 240 and Player.centerX-2.5 < 30:
        onMouseRelease(mouseX, mouseY)
         
    #wall15
    if Player.centerX-2.5 < 31 and Player.centerY-2.5 < 240 and Player.centerX+2.5 > 30 and Player.centerY+2.5 > 220:
        onMouseRelease(mouseX, mouseY)
         
    #wall16
    if Player.centerX-2.5 < 111 and Player.centerY-2.5 < 215 and Player.centerX+2.5 > 110 and Player.centerY+2.5 > 160:
        onMouseRelease(mouseX, mouseY)
         
    #wall17
    if Player.centerY-2.5 < 221 and Player.centerX+2.5 > 30 and Player.centerY+2.5 > 220 and Player.centerX-2.5 < 40:
        onMouseRelease(mouseX, mouseY)
         
    #wall18
    if Player.centerX-2.5 < 41 and Player.centerY-2.5 < 220 and Player.centerX+2.5 > 40 and Player.centerY+2.5 > 210:
        onMouseRelease(mouseX, mouseY)
         
    #wall19
    if Player.centerX-2.5 < 41 and Player.centerY-2.5 < 290 and Player.centerX+2.5 > 40 and Player.centerY+2.5 > 230:
        onMouseRelease(mouseX, mouseY)
         
    #wall20
    if Player.centerY-2.5 < 231 and Player.centerX+2.5 > 0 and Player.centerY+2.5 > 230 and Player.centerX-2.5 < 10:
        onMouseRelease(mouseX, mouseY)
         
    #wall21
    if Player.centerX-2.5 < 11 and Player.centerY-2.5 < 290 and Player.centerX+2.5 > 10 and Player.centerY+2.5 > 230:
        onMouseRelease(mouseX, mouseY)
         
    #wall22
    if Player.centerX-2.5 < 31 and Player.centerY-2.5 < 290 and Player.centerX+2.5 > 30 and Player.centerY+2.5 > 240:
        onMouseRelease(mouseX, mouseY)
         
    #wall23
    if Player.centerY-2.5 < 171 and Player.centerX+2.5 > 40 and Player.centerY+2.5 > 170 and Player.centerX-2.5 < 60:
        onMouseRelease(mouseX, mouseY)
         
    #wall24
    if Player.centerY-2.5 < 191 and Player.centerX+2.5 > 0 and Player.centerY+2.5 > 190 and Player.centerX-2.5 < 10:
        onMouseRelease(mouseX, mouseY)
         
    #wall25
    if Player.centerY-2.5 < 251 and Player.centerX+2.5 > 10 and Player.centerY+2.5 > 250 and Player.centerX-2.5 < 20:
        onMouseRelease(mouseX, mouseY)
         
    #wall26
    if Player.centerY-2.5 < 261 and Player.centerX+2.5 > 10 and Player.centerY+2.5 > 260 and Player.centerX-2.5 < 20:
        onMouseRelease(mouseX, mouseY)
         
    #wall27
    if Player.centerY-2.5 < 271 and Player.centerX+2.5 > 10 and Player.centerY+2.5 > 270 and Player.centerX-2.5 < 20:
        onMouseRelease(mouseX, mouseY)
         
    #wall28
    if Player.centerY-2.5 < 281 and Player.centerX+2.5 > 10 and Player.centerY+2.5 > 280 and Player.centerX-2.5 < 20:
        onMouseRelease(mouseX, mouseY)
         
    #wall29
    if Player.centerY-2.5 < 291 and Player.centerX+2.5 > 10 and Player.centerY+2.5 > 290 and Player.centerX-2.5 < 20:
        onMouseRelease(mouseX, mouseY)
         
    #wall30
    if doorStar.visible == True:
        if Player.centerX-2.5 < 51 and Player.centerY-2.5 < 300 and Player.centerX+2.5 > 50 and Player.centerY+2.5 > 210:
            onMouseRelease(mouseX, mouseY)
         
    #wall31
    if Player.centerY-2.5 < 291 and Player.centerX+2.5 > 40 and Player.centerY+2.5 > 290 and Player.centerX-2.5 < 50:
        onMouseRelease(mouseX, mouseY)
         
    #wall32
    if Player.centerY-2.5 < 211 and Player.centerX+2.5 > 50 and Player.centerY+2.5 > 210 and Player.centerX-2.5 < 70:
        onMouseRelease(mouseX, mouseY)
         
    #wall33
    if Player.centerX-2.5 < 71 and Player.centerY-2.5 < 210 and Player.centerX+2.5 > 70 and Player.centerY+2.5 > 180:
        onMouseRelease(mouseX, mouseY)
         
    #wall34
    if Player.centerY-2.5 < 201 and Player.centerX+2.5 > 50 and Player.centerY+2.5 > 200 and Player.centerX-2.5 < 60:
        onMouseRelease(mouseX, mouseY)
         
    #wall35
    if Player.centerX-2.5 < 61 and Player.centerY-2.5 < 220 and Player.centerX+2.5 > 60 and Player.centerY+2.5 > 200:
        onMouseRelease(mouseX, mouseY)
         
    #wall36
    if Player.centerY-2.5 < 221 and Player.centerX+2.5 > 60 and Player.centerY+2.5 > 220 and Player.centerX-2.5 < 70:
        onMouseRelease(mouseX, mouseY)
    #wall37
    if Player.centerY-2.5 < 231 and Player.centerX+2.5 > 50 and Player.centerY+2.5 > 230 and Player.centerX-2.5 < 80:
        onMouseRelease(mouseX, mouseY)

    #wall38
    if Player.centerX-2.5 < 81 and Player.centerY-2.5 < 230 and Player.centerX+2.5 > 80 and Player.centerY+2.5 > 200:
        onMouseRelease(mouseX, mouseY)
    
    #wall39
    if Player.centerY-2.5 < 201 and Player.centerX+2.5 > 80 and Player.centerY+2.5 > 200 and Player.centerX-2.5 < 100:
        onMouseRelease(mouseX, mouseY)
        
    #wall40
    if Player.centerX-2.5 < 91 and Player.centerY-2.5 < 230 and Player.centerX+2.5 > 90 and Player.centerY+2.5 > 200:
        onMouseRelease(mouseX, mouseY)
    #wall41
    if Player.centerY-2.5 < 231 and Player.centerX+2.5 > 90 and Player.centerY+2.5 > 230 and Player.centerX-2.5 < 100:
        onMouseRelease(mouseX, mouseY)
    #wall42
    if Player.centerX-2.5 < 101 and Player.centerY-2.5 < 231 and Player.centerX+2.5 > 100 and Player.centerY+2.5 > 215:
        onMouseRelease(mouseX, mouseY)
    #wall43
    if Player.centerY-2.5 < 216 and Player.centerX+2.5 > 110 and Player.centerY+2.5 > 215 and Player.centerX-2.5 < 130:
        onMouseRelease(mouseX, mouseY)
    #wall44
    if Player.centerY-2.5 < 171 and Player.centerX+2.5 > 140 and Player.centerY+2.5 > 170 and Player.centerX-2.5 < 150:
        onMouseRelease(mouseX, mouseY)
    #wall45
    if Player.centerX-2.5 < 141 and Player.centerY-2.5 < 290 and Player.centerX+2.5 > 140 and Player.centerY+2.5 > 170:
        onMouseRelease(mouseX, mouseY)
    #wall46
    if Player.centerX-2.5 < 131 and Player.centerY-2.5 < 215 and Player.centerX+2.5 > 130 and Player.centerY+2.5 > 180:
        onMouseRelease(mouseX, mouseY)
    #wall47
    if Player.centerY-2.5 < 181 and Player.centerX+2.5 > 120 and Player.centerY+2.5 > 180 and Player.centerX-2.5 < 130:
        onMouseRelease(mouseX, mouseY)
    #wall48
    if Player.centerX-2.5 < 121 and Player.centerY-2.5 < 200 and Player.centerX+2.5 > 120 and Player.centerY+2.5 > 180:
        onMouseRelease(mouseX, mouseY)
    #wall49
    if Player.centerY-2.5 < 246 and Player.centerX+2.5 > 50 and Player.centerY+2.5 > 245 and Player.centerX-2.5 < 110:
        onMouseRelease(mouseX, mouseY)
    #wall50
    if Player.centerX-2.5 < 111 and Player.centerY-2.5 < 245 and Player.centerX+2.5 > 110 and Player.centerY+2.5 > 230:
        onMouseRelease(mouseX, mouseY)
    #wall51
    if Player.centerX-2.5 < 121 and Player.centerY-2.5 < 245 and Player.centerX+2.5 > 120 and Player.centerY+2.5 > 230:
        onMouseRelease(mouseX, mouseY)
    #wall52
    if Player.centerY-2.5 < 246 and Player.centerX+2.5 > 120 and Player.centerY+2.5 > 245 and Player.centerX-2.5 < 130:
        onMouseRelease(mouseX, mouseY)
    #wall53
    if Player.centerX-2.5 < 131 and Player.centerY-2.5 < 290 and Player.centerX+2.5 > 130 and Player.centerY+2.5 > 245:
        onMouseRelease(mouseX, mouseY)
    #wall54
    if Player.centerX-2.5 < 121 and Player.centerY-2.5 < 300 and Player.centerX+2.5 > 120 and Player.centerY+2.5 > 255:
        onMouseRelease(mouseX, mouseY)
    #wall55
    if Player.centerY-2.5 < 256 and Player.centerX+2.5 > 90 and Player.centerY+2.5 > 255 and Player.centerX-2.5 < 120:
        onMouseRelease(mouseX, mouseY)
    #wall56
    if Player.centerY-2.5 < 276 and Player.centerX+2.5 > 80 and Player.centerY+2.5 > 275 and Player.centerX-2.5 < 110:
        onMouseRelease(mouseX, mouseY)
    #wall57
    if Player.centerX-2.5 < 91 and Player.centerY-2.5 < 265 and Player.centerX+2.5 > 90 and Player.centerY+2.5 > 255:
        onMouseRelease(mouseX, mouseY)
    #wall58
    if Player.centerY-2.5 < 266 and Player.centerX+2.5 > 90 and Player.centerY+2.5 > 265 and Player.centerX-2.5 < 110:
        onMouseRelease(mouseX, mouseY)
    #wall59
    if Player.centerY-2.5 < 261 and Player.centerX+2.5 > 50 and Player.centerY+2.5 > 260 and Player.centerX-2.5 < 60:
        onMouseRelease(mouseX, mouseY)
    #wall60
    if Player.centerX-2.5 < 81 and Player.centerY-2.5 < 275 and Player.centerX+2.5 > 80 and Player.centerY+2.5 > 245:
        onMouseRelease(mouseX, mouseY)
    #wall61
    if Player.centerX-2.5 < 61 and Player.centerY-2.5 < 290 and Player.centerX+2.5 > 60 and Player.centerY+2.5 > 260:
        onMouseRelease(mouseX, mouseY)
    #wall62
    if Player.centerX-2.5 < 71 and Player.centerY-2.5 < 290 and Player.centerX+2.5 > 70 and Player.centerY+2.5 > 260:
        onMouseRelease(mouseX, mouseY)
    #wall63
    if Player.centerY-2.5 < 291 and Player.centerX+2.5 > 60 and Player.centerY+2.5 > 290 and Player.centerX-2.5 < 110:
        onMouseRelease(mouseX, mouseY)

    ###points
    if Player.centerX-2.5 < 320.5 and Player.centerY-2.5 < 115.5 and Player.centerX+2.5 > 315.5 and Player.centerY+2.5 > 110.5:
        reguStar.visible = False
        r1.value = 1
        
    if Player.centerX-2.5 < 252.5 and Player.centerY-2.5 < 142.5 and Player.centerX+2.5 > 247.5 and Player.centerY+2.5 > 137.5:
        reguStar4.visible = False
        r2.value = 1
        
    if Player.centerX-2.5 < 202.5 and Player.centerY-2.5 < 32.5 and Player.centerX+2.5 > 197.5 and Player.centerY+2.5 > 27.5:
        reguStar2.visible = False
        r3.value = 1
        
    if Player.centerX-2.5 < 6.5 and Player.centerY-2.5 < 186.5 and Player.centerX+2.5 > 3.5 and Player.centerY+2.5 > 183.5:
        reguStar3.visible = False
        r4.value = 1
    
    ###Blue star
    if blue.value == 0:
        if Player.centerX-2.5 < 76.5 and Player.centerY-2.5 < 61.5 and Player.centerX+2.5 > 73.5 and Player.centerY+2.5 > 58.5:
            blue.value = 1
            blueStar.visible = False
            blueBox.visible = False
    ###Gold star
    if gold.value == 0:
        if Player.centerX-2.5 < 197.5 and Player.centerY-2.5 < 227.5 and Player.centerX+2.5 > 193.5 and Player.centerY+2.5 > 223.5:
            sugar.visible = True
            gold.value = 1
            colorStar.visible = False
            background.fill = "grey"
    ###Final star
    if red.value == 0:
        if Player.centerX-2.5 < 57.5 and Player.centerY-2.5 < 255.5 and Player.centerX+2.5 > 52.5 and Player.centerY+2.5 > 250.5:
            red.value = 1
            theDoor.visible = False
            doorStar.visible = False
            
    ###cheat star
    if Player.centerX-2.5 < 106.5 and Player.centerY-2.5 < 126.5 and Player.centerX+2.5 > 103.5 and Player.centerY+2.5 > 123.5:
        cheatingStar.visible = False
        Rect(0, 300, 400, 100, fill = "red")
        Label("DON'T CHEAT", 200, 350, size = 50)
        Label("run the program again", 200, 385, size = 10)
        onMouseRelease(mouseX, mouseY)
    ###win
    if Player.centerX-2.5 < 6.5 and Player.centerY-2.5 < 304.5 and Player.centerX+2.5 > 3.5 and Player.centerY+2.5 > 301.5:
        winStar.visible = False
        background.fill = "black"
        Label("The blackberry community", 200, 300, fill= "yellow", size = 30)
        Label("is saved!!!! Good job!!", 200, 340, fill="yellow", size = 30)

    
        
        
        
        
        
        