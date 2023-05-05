import turtle as t

def rectangle(length_1, length_2, degree):
    for i in range(2):
        t.fd(length_1)
        t.lt(degree)
        t.fd(length_2)
        t.lt(degree)
        
def place_pen(x, y, z):
    t.penup()
    t.goto(x,y)
    t.setheading(z)
    t.pendown()
    
def triangle(length, degree):
    for i in range(3):
        t.lt(degree)
        t.fd(length)
        
def main():
    t.speed(0)
#     rectangle(100, 100, 90)
    place_pen(100, 100, 0)
#     triangle(100, 120)
#     place_pen(40, 0, 0)
#     rectangle(20, 40, 90)
#     place_pen(10, 50, 0)
#     rectangle(20, 20, 90)
#     place_pen(70, 50, 0)
#     rectangle(20, 20, 90)

if __name__=="__main__":
    main()
    
''' Original Code:
import turtle

turtle.speed(0)

# Draw a rectangle with width 100 and height 100
for i in range(2):
    turtle.forward(100)
    turtle.lt(90)
    turtle.forward(100)
    turtle.lt(90)

# Move the turtle to (100, 100) to start the roof
turtle.penup()
turtle.goto(100, 100)
turtle.setheading(0)
turtle.pendown()

# Draw a triangle with sides of length 100
for i in range(3):
    turtle.lt(120)
    turtle.forward(100)

# Move the turtle to (40, 0) to start the door
turtle.penup()
turtle.goto(40, 0)
turtle.setheading(0)
turtle.pendown()

# Draw a rectangle with width 20 and height 40
for i in range(2):
    turtle.forward(20)
    turtle.lt(90)
    turtle.forward(40)
    turtle.lt(90)

# Move the turtle to (10, 50) to start the left window
turtle.penup()
turtle.goto(10, 50)
turtle.setheading(0)
turtle.pendown()

# Draw a rectangle with width 20 and height 20
for i in range(2):
    turtle.forward(20)
    turtle.lt(90)
    turtle.forward(20)
    turtle.lt(90)

# Move the turtle to (70, 50) to start the right window
turtle.penup()
turtle.goto(70, 50)
turtle.setheading(0)
turtle.pendown()

# Draw a rectangle with width 20 and height 20
for i in range(2):
    turtle.forward(20)
    turtle.lt(90)
    turtle.forward(20)
    turtle.lt(90)

turtle.mainloop()
'''