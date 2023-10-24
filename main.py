import turtle
from turtle import *
from random import randint

turtle.bgcolor('white')
turtle.speed(0)
turtle.penup()

finish = Turtle()
finish.shape("square")
finish.color("black")
finish.penup()

stamp_size = 20
square_size = 15
finish_line = 200

for i in range(10):
    finish.setpos(finish_line, (150 - (i * square_size * 2)))
    finish.stamp()

for j in range(10):
    finish.setpos(finish_line + square_size,
                  ((150 - square_size) - (j * square_size * 2)))
    finish.stamp()

bob = Turtle()

bob.speed(0)
bob.color("Blue")
bob.shape("turtle")

bob.penup()
bob.goto(-250, 100)
bob.pendown()

tom = Turtle()

tom.speed(0)
tom.color("Red")
tom.shape("turtle")

tom.penup()
tom.goto(-250, 50)
tom.pendown()

rik = Turtle()

rik.speed(0)
rik.color("Green")
rik.shape("turtle")

rik.penup()
rik.goto(-250, 0)
rik.pendown()

billy = Turtle()

billy.speed(0)
billy.color("yellow")
billy.shape("turtle")

billy.penup()
billy.goto(-250, -50)
billy.pendown()

t1 = 0
t2 = 0
t3 = 0
t4 = 0

for i in range(180):
    a = randint(1, 5)
    b = randint(1, 5)
    c = randint(1, 5)
    d = randint(1, 5)
    bob.forward(a)
    tom.forward(b)
    rik.forward(c)
    billy.forward(d)


    t1 += a
    t2 += b
    t3 += c
    t4 += d

    if t1>=480:
      bob.goto(0, -120)
      bob.goto(0, -150)
      turtle.write("Bob wins",font=("Arial", 24, "normal"))
      break     
  

    elif t2 >= 480:
      tom.goto(0, -120)
      tom.goto(0, -150)
      turtle.write("Tom wins", font=("Arial", 24, "normal"))
      break
        
    elif t3 >= 480:
      rik.goto(0, -120)
      rik.goto(0, -150)
      turtle.write("Rik wins", font=("Arial", 24, "normal"))
      break
        
    elif t4 >= 480:
      billy.goto(0, -120)
      billy.goto(0, -150)
      turtle.write("Billy wins", font=("Arial", 24, "normal"))
      break


