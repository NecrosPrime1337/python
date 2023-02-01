#autor N3CR05.pr1m3
import base64
import turtle
import random

direct = 0  #direct of drawning labyrinth
distance = 0 #distance how much long line we are draw
colors = ['white','red','green','magenta','cyan']
color = "Cyan"
rads = 0
turtle.title("умная черепашка")

def drawRandom():
    turtle.title("не очень умная черепашка(ей скучно)")
    while True:
        direct = random.randint(0, 3)
        distance = random.randint(20, 100)
        turtle.pensize(random.randint(3, 7))
        turtle.pencolor(colors.__getitem__(random.randint(0, 4)))
        if direct == 0:
            turtle.forward(distance)
        elif direct == 1:
            turtle.back(distance)
        elif direct == 2:
            turtle.left(90)
            turtle.forward(distance)
        else:
            turtle.right(90)
            turtle.forward(distance)

def drawStar(angles, color, distance):
    angle = 180/angles
    turtle.pencolor(colors.__getitem__(color))
    turtle.pensize(1)
    i=0
    for i in range(int(angles)):
        turtle.fd(distance)
        turtle.left(180 - angle)
    main()
def easter():
    #this is a easter-egg
    #эта часть кода ДОЛЖНА (ОБЯЗАНА) БЫТЬ НЕЧИТАЕМА!!! так что я специально не использую циклы и отдельные методы упрощения))))
    #куда же без юмора то?)))
    turtle.title(base64.b64decode("RE9PTSBUVVJUTEUgU0xBWUVSISEh"))
    turtle.penup()
    turtle.pensize(2)
    turtle.setposition(-218, 149)
    turtle.pd()
    turtle.right(45)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(190)
    turtle.left(135)
    turtle.forward(100)
    turtle.left(45)
    turtle.forward(138)
    turtle.left(45)
    turtle.forward(5)
    turtle.left(45)
    turtle.forward(95)
    turtle.pu()
    turtle.setpos(-170, 100)
    turtle.pd()
    turtle.left(90)
    turtle.fd(70)
    turtle.left(135)
    turtle.fd(30)
    turtle.left(45)
    turtle.fd(55)
    turtle.left(90)
    turtle.fd(30)
    turtle.pu()
    turtle.setpos(-120, 147)
    turtle.pd()
    turtle.left(90)
    turtle.fd(140)
    turtle.left(45)
    turtle.fd(70)
    turtle.left(90)
    turtle.fd(30)
    turtle.left(45)
    turtle.fd(168)
    turtle.left(45)
    turtle.fd(7)
    turtle.left(45)
    turtle.fd(60)
    turtle.left(45)
    turtle.fd(7)
    turtle.pu()
    turtle.setpos(-100, 100)
    turtle.pd()
    turtle.left(45)
    turtle.fd(50)
    turtle.left(45)
    turtle.fd(35)
    turtle.left(135)
    turtle.fd(75)
    turtle.left(90)
    turtle.fd(30)
    turtle.pu()
    turtle.setpos(-45,147)
    turtle.pd()
    turtle.left(90)
    turtle.fd(168)
    turtle.left(45)
    turtle.fd(30)
    turtle.left(90)
    turtle.fd(70)
    turtle.left(45)
    turtle.fd(140)
    turtle.left(45)
    turtle.fd(7)
    turtle.left(45)
    turtle.fd(60)
    turtle.left(45)
    turtle.fd(7)
    turtle.left(45)
    turtle.pu()
    turtle.setpos(-20, 100)
    turtle.pd()
    turtle.fd(75)
    turtle.left(135)
    turtle.fd(35)
    turtle.left(45)
    turtle.fd(50)
    turtle.left(90)
    turtle.fd(30)
    turtle.pu()
    turtle.setpos(30,147)
    turtle.pd()
    turtle.left(90)
    turtle.fd(150)
    turtle.left(45)
    turtle.fd(40)
    turtle.left(135)
    turtle.fd(60)
    turtle.right(175)
    turtle.fd(30)
    turtle.left(170)
    turtle.fd(30)
    turtle.right(175)
    turtle.fd(70)
    turtle.left(45)
    turtle.fd(40)
    turtle.left(135)
    turtle.fd(200)
    turtle.right(45)
    turtle.fd(30)
    turtle.left(135)
    turtle.fd(45)
    turtle.left(80)
    turtle.fd(30)
    turtle.right(165)
    turtle.fd(30)
    turtle.left(85)
    turtle.fd(25)
    turtle.left(45)
    turtle.fd(7)
    turtle.pu()
    turtle.setpos(-100, -200 )
    turtle.pd()
    turtle.left(135)
    turtle.right(90)
    turtle.circle(50)
    turtle.pu()
    turtle.fd(15)
    turtle.pd()
    turtle.left(90)
    drawStar(5, 1, 100)
    #вот здесь заканчивается этот треш)))

def main():
    turtle.color("black", "cyan")
    turtle.begin_fill()
    turtle.bgcolor("black")
    turtle.pencolor("red")
    choice = turtle.numinput("что ты хочешь нарисовать? звезду или мне просто побегать?",
                             "0-рандомный рисунок, 1-звезда", 0, 0, 9999)
    turtle.clear()
    if choice == 0:
        drawRandom()
    if choice == 1:
        angles = turtle.numinput("сколько концов должно быть у звезды?", "5 минимум", 5, 5, 256)
        distance = turtle.numinput("размер", "больше 100 бери", 100, 20, 256)
        drawStar(angles, 1, distance)
    if choice == 1337:
        easter()

main()








