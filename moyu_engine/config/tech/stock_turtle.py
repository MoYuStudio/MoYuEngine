import turtle
import random
import time


turtle.pensize(10)
turtle.pencolor('black')
turtle.penup()
turtle.goto(-350, 0)
turtle.pendown()
turtle.delay(1)
turtle.hideturtle()

a = 500

bFin = 0

while a != 0:
    b = random.randint(-10, 10)
    bFin += b
    print(turtle.pos())

    if -80 < bFin < 80:
        turtle.forward(1)
        turtle.left(b)
        a -= 1
        print(b, bFin)
        stock = b
        print('=' * 25)
        stockFin = '今日涨幅' + str(stock) + '%'
        print(stockFin)
        print('=' * 25)
    elif -80 >= bFin:
        b = random.randint(80, 150)
        bFin += b
        turtle.forward(1)
        turtle.left(b)
        a -= 1
        print(b, bFin)
        stock = b
        print('=' * 25)
        stockFin = '今日涨幅' + str(stock) + '%'
        print(stockFin)
        print('=' * 25)
    elif bFin >= 80:
        b = random.randint(80, 150)
        bFin += -b
        turtle.forward(1)
        turtle.left(-b)
        a -= 1
        print(-b, bFin)
        stock = -b
        print('=' * 25)
        stockFin = '今日涨幅' + str(stock) + '%'
        print(stockFin)
        print('=' * 25)
    else:
        print('Erro')

else:
    print('done')
