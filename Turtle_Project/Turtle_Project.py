'''
Turtle_Project.py
Jackson Daw
CS-1400-002
2/6/2023

This code draws The Elden Ring, it's what holds The Lands Between together
in the game Elden Ring. The orangish runes are the Greatrunes of Death,
the golden Greatrune is Morgott's, the pale yellow Greatrune is Godrick's,
the red Melania's, and the purple Radahn's. I didn't use fill on any of these since
that would ruin the picture, but I did change the background if nothing else.
The reason I don't have many loops is because almost all the code is unique.
And I learned that I really don't understand functions.
I also learned that learning a library really just requires patience and troubleshooting.
I learned some neat tricks from the turtle guide that really helped out with a few things.
As for running the code, just follow the instructions: enter only positive integers. 

'''

import turtle
t = turtle


# def get_dimensions():
#     try:
#         width = int(input("Enter width: "))
#         height = int(input("Enter height: "))
#     except ValueError:
#         print("Please enter positive integers")
#     return
#     if width < 0 or height < 0:
#         print("Please enter positive integers")
#     return
    


def draw():
    try:
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
    except ValueError:
        print("Please enter positive integers")
        return
    if width < 0 or height < 0:
        print("Please enter positive integers")
        return
    
#     set screen size
    t.screensize(width, height)
    t.bgcolor("black")

#     set pen for drawing
    t.speed(0)
    t.colormode(255)
    t.pencolor((220,128,8))
    t.width(5.5)
    t.pu()
    t.goto(0,200)
    t.pd()
#     second biggest rune of death
    t.circle(250, 30)
    t.circle(250, -60)
    t.circle(250, 30)
#     big ol line
    t.width(7)
    t.rt(90)
    t.fd(15)
    t.pencolor((255, 184, 28))
    t.fd(335)
    t.pencolor((220,128,8))
    t.fd(100)
    t.backward(30)
    t.lt(90)
#     biggest rune of death
    t.width(5)
    t.circle(450, 30)
    t.circle(450, -60)
    t.circle(450, 30)
#     godricks great rune
    t.width(7)
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.pencolor((246, 235, 97))
    t.circle(100)
#     malenias and radahns runes
    t.pencolor((187, 0, 0))
    t.lt(35)
    t.circle(83)
    t.pencolor((75, 54, 95))
    t.rt(70)
    t.circle(83)
#     morgotts rune
    t.lt(125)
    t.fd(10)
    t.pencolor((255, 184, 28))
    t.fd(50)
    t.rt(90)
    t.circle(94)
#     third biggest rune of death
    t.pencolor((220,128,8))
    t.width(4.5)
    t.circle(300, 30)
    t.circle(300, -60)
    t.circle(300, 30)
#     smallest rune of death
    t.lt(90)
    t.width(7)
    t.pencolor((255, 184, 28))
    t.fd(87)
    t.rt(90)
    t.width(4)
    t.pencolor((220,128,8))
    t.circle(210, 30)
    t.circle(210, -60)
    t.circle(210, 30)
    
    t.hideturtle()
    t.done()
    
    
if __name__ == "__main__":
    draw()

    

