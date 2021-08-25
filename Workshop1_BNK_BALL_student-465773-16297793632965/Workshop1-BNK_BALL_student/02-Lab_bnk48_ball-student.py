# Lab_BNK48 
import pygame as pg
import math
import random
# TODO 1 : กำหนด width : 1000 , height : 600 และ FPS : 60
width = 1000
height = 600
FPS = 60

# TODO 2 : กำหนดค่าสีดังนี้ pink : (197,142,195) , white : (255,255,255)
pink = pg.Color(197,142,195)
white = pg.Color(255,25,255)
bglist = [pg.Color(197,142,195),pg.Color(197,142,155),pg.Color(197,202,195),pg.Color(157,142,195)]
# TODO 3 : กำหนดความเร็วให้กับ member แต่ละคน [ 3 member ]
ball1_speed = [2,2]
ball2_speed = [-3,4]
ball3_speed = [3,-2]
b1speed = math.sqrt(8)
b2speed = math.sqrt(25)
b3speed = math.sqrt(13)
# TODO 4 : initialize pygame variable and create clock
pg.init()
clock = pg.time.Clock()
running =True

# TODO 5 : create screen [pygame.display.set_mode] 
# and set caption [pygame.display.set_caption] => "BNK_BALL (Heavy Collision)"
screen = pg.display.set_mode([width, height])
pg.display.set_caption("BNK_BALL (Heavy Collision)")

# TODO 6
#Load sound [change your sound filepath according to your computer]
# pg.mixer.init()
# pg.mixer.music.load("C:\\Users\\jiray\\Desktop\\Workshop1_BNK_BALL_student-465773-16297793632965\\Workshop1-BNK_BALL_student\\source\\sound.mp3")
# pg.mixer.music.play(-1, 0.0)

# ใช้คำสั่ง soundeffect.play() เพื่อเล่นเสียง effect ตอนลูกบอลชนกัน
# soundeffect = pg.mixer.Sound("C:\\Users\\jiray\\Desktop\\Workshop1_BNK_BALL_student-465773-16297793632965\\Workshop1-BNK_BALL_student\\source\\effect.wav")

# Choose 3 members from BNK48 and create pygame object from  get_rect
# [ load , resize , get_rect ]

# Member 1 [size : (150 , 150) , center : (500 , 250) ]
ball1_img = pg.image.load("source/BNK48/Wee_cc.png").convert_alpha()
ball1_img = pg.transform.scale(ball1_img, (150, 150))
ball1_rect = ball1_img.get_rect(center=(random.randint(400,600),random.randint(150,300)))

# TODO 7 : create object with attribute in each comment
# Member 2 [size : (100 , 100) , center : (250 , 120)]
ball2_img = pg.image.load("source/BNK48/Kate_cc.png").convert_alpha()
ball2_img = pg.transform.scale(ball2_img, (100, 100))
ball2_rect = ball2_img.get_rect(center = (random.randint(100,300),random.randint(100,300)))



# Member 3 [size : (120 , 120) , center : (800 , 400)]
ball3_img = pg.image.load("source/BNK48/Jib_cc.png").convert_alpha()
ball3_img = pg.transform.scale(ball3_img, (120, 120))
ball3_rect = ball3_img.get_rect(center=(random.randint(600,700),random.randint(300,500)))

def iscollapse(pos1,r1,pos2,r2):
    d = ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5
    return d <= r1+r2
theta =0
ind = 0
while running:
    # TODO 8 : set ให้ตัวเกมส์แสดงผลด้วยความเร็วที่เหมาะสม [clock.tick(...)]
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running=False
            pg.quit()

    if running:
        # TODO 9 :ใส่สี background สีชมพู (screen.fill(...))
        screen.fill(bglist[ind])

        # TODO 10 : ให้ member ทั้ง 3 คนเคลื่อนที่ตามทิศทางและความเร็วเป็นไปตาม speed ของแต่ละคน
        ball1_rect = ball1_rect.move(ball1_speed)
        ball2_rect = ball2_rect.move(ball2_speed)
        ball3_rect = ball3_rect.move(ball3_speed)
        

        
        # TODO 11 : วาด text คำว่า "Heavy Collision" [size : 150 , center :(width/2 , height/3), สีขาว]
        font_name = pg.font.match_font('arial')  # กำหนดชื่อ Font
        font = pg.font.Font(font_name, 150)  # กำหนดขนาด font
        
        text_surface = font.render("Heavy Collision",True,pg.Color(255,255,255))
        textRect = text_surface.get_rect()
        textRect.center = (width//2,height//2)
        screen.blit(text_surface,textRect)


        # TODO 12 : วาด text รหัสนิสิต ลงไป ข้างใต้คำว่า "Heavy Collision" [size : 100 ,center :(width/2 , height/1.5), สีขาว]
        # [ขนาดและตำแหน่งสามารถปรับได้ตามความเหมาะสม]
        font = pg.font.Font(font_name, 100)
        text_surface = font.render("6432023321",True,pg.Color(255,255,255))
        textRect = text_surface.get_rect()
        textRect.center = (width//2,height/1.3)
        screen.blit(text_surface,textRect)


        # TODO 13 : เขียนเงื่อนไขไม่ให้ตกกรอบทุกด้านให้กับ member ทั้ง 3 คน
        if ball1_rect.left < 0 or ball1_rect.right > width:
            ball1_speed[0] = -ball1_speed[0]
        if ball1_rect.top < 0 or ball1_rect.bottom > height:
            ball1_speed[1] = -ball1_speed[1]
        if ball2_rect.left < 0 or ball2_rect.right > width:
            ball2_speed[0] = -ball2_speed[0]
        if ball2_rect.top < 0 or ball2_rect.bottom > height:
            ball2_speed[1] = -ball2_speed[1]
        if ball3_rect.left < 0 or ball3_rect.right > width:
            ball3_speed[0] = -ball3_speed[0]
        if ball3_rect.top < 0 or ball3_rect.bottom > height:
            ball3_speed[1] = -ball3_speed[1]

        
        
        # Special point ทำให้ลูกบอลชนกันแล้วเด้งในทิศตรงกันข้าม
        
        if iscollapse(ball1_rect.center,75,ball2_rect.center,50):
            theta = math.atan(abs(ball1_rect.center[1]-ball2_rect.center[1]) / abs(ball1_rect.center[0]-ball2_rect.center[0]))
            ball1_speed = [b1speed * abs(math.cos(theta)) , b1speed * abs(math.sin(theta))]
            ball2_speed = [b2speed * abs(math.cos(theta)) , b2speed * abs(math.sin(theta))]
            if ball1_rect.center[0] < ball2_rect.center[0]:
                ball1_speed[0] *=-1
            else:
                ball2_speed[0] *=-1
            if ball1_rect.center[1] < ball2_rect.center[1]:
                ball1_speed[1] *=-1
            else:
                ball2_speed[1] *=-1
            ind = random.randint(0,3)
        if iscollapse(ball1_rect.center,75,ball3_rect.center,60):
            theta = math.atan(abs(ball1_rect.center[1]-ball3_rect.center[1]) / abs(ball1_rect.center[0]-ball3_rect.center[0]))
            ball1_speed = [b1speed * abs(math.cos(theta)) , b1speed * abs(math.sin(theta))]
            ball3_speed = [b3speed * abs(math.cos(theta)) , b3speed * abs(math.sin(theta))]
            if ball1_rect.center[0] < ball3_rect.center[0]:
                ball1_speed[0] *=-1
            else:
                ball3_speed[0] *=-1
            if ball1_rect.center[1] < ball3_rect.center[1]:
                ball1_speed[1] *=-1
            else:
                ball3_speed[1] *=-1
                ind = random.randint(0,3)
        if iscollapse(ball2_rect.center,50,ball3_rect.center,60):
            theta = math.atan(abs(ball3_rect.center[1]-ball2_rect.center[1]) / abs(ball3_rect.center[0]-ball2_rect.center[0]))
            ball2_speed = [b2speed * abs(math.cos(theta)) , b2speed * abs(math.sin(theta))]
            ball3_speed = [b3speed * abs(math.cos(theta)) , b3speed * abs(math.sin(theta))]
            if ball3_rect.center[0] < ball2_rect.center[0]:
                ball3_speed[0] *=-1
            else:
                ball2_speed[0] *=-1
            if ball3_rect.center[1] < ball2_rect.center[1]:
                ball3_speed[1] *=-1
            else:
                ball2_speed[1] *=-1
            ind = random.randint(0,3)
        print(math.cos(theta))







        ################################################

        # TODO 14 : เอาภาพของ member แต่ละคนใส่ลงใน object ของตนเอง
        screen.blit(ball1_img, ball1_rect)
        screen.blit(ball2_img, ball2_rect)        
        screen.blit(ball3_img, ball3_rect)
        


        ##########################################################

        pg.display.flip()