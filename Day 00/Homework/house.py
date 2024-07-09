from turtle import *

width(5)
# draw a square

color("yellow")
begin_fill()

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
 
end_fill()


penup()
goto(200,200)
pendown()

#roof
color("purple")
begin_fill()
right(135)
forward(141)
left(90)
forward(141)
end_fill()


penup()
goto(75,0)
pendown()

#door
color("red")
begin_fill()
right(135)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()


penup()
goto(20,180)
pendown()

# window 1
color("green")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()
penup()
goto(180,180)
pendown()

#window 2
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()








exitonclick()