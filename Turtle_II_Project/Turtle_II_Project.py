'''
simple functions needed:
triangle
quadrilateral
circle
pen placer

complex shapes:
sun
tree
bush
painting frame
clouds
'''
import turtle as t

def triangle(length):
    for i in range(3):        
        t.fd(length)
        t.lt(120)
        
def square(l1, l2):
    for i in range(2):
        t.fd(l1)
        t.lt(90)
        t.fd(l2)
        t.lt(90)
        
def circle(radius, extent):
    t.circle(radius, extent)

def pen_placer(x,y,z):
    t.penup()
    t.goto(x,y)
    t.setheading(z)
    t.pendown()
        
def tree(x,y,z,l1,l2,length):
    pen_placer(x,y,z)
    t.fillcolor("#48260D")
    t.begin_fill()
    square(l1,l2)
    t.end_fill()
    t.lt(90)
    t.fd(l2)
    t.lt(90)
    t.fd(l1 * 2)
    t.rt(180)
    for i in range(3):
        triangle(length)
        t.lt(90)
        t.penup()
        t.fd(length * .3)
        t.rt(90)
        t.pendown()

def middle_trees(x,y,z,l1,l2,length):
    for i in range(3):
        tree(x,y,z,l1,l2,length)
        x -= (x*1.49)
        
def left_trees(x,y,z,l1,l2,length):
    for i in range(3):
        tree(x,y,z,l1,l2,length)
        x -= (x*.35)
        
def right_trees(x,y,z,l1,l2,length):
    for i in range(3):
        tree(x,y,z,l1,l2,length)
        x -= (x*.35)

def bush(x,y,z,radius,extent):
    pen_placer(x,y,z)
    for i in range(9):
        t.circle(radius,extent)
        t.lt(180)

def middle_bushes(x,y,z,radius,extent):
    for i in range(3):
        bush(x,y,z,radius,extent)
        x += 75
        
def left_bushes(x,y,z,radius,extent):
    for i in range(2):
        bush(x,y,z,radius,extent)
        x += 143

def right_bushes(x,y,z,radius,extent):
    for i in range(2):
        bush(x,y,z,radius,extent)
        x += 143

def inner_sun(x,y,z,radius,extent,length):
    pen_placer(x,y,z)
    t.fillcolor("yellow")
    t.begin_fill()
    circle(radius,extent)
    pen_placer(x,y,z)
    t.lt(90)
    t.fd(radius)
    t.rt(90)
    t.fd(radius)
    z += 300
    pen_placer(x,y,z)
    for i in range(9):
        t.fd(length)
        t.lt(130)
        t.fd(length)
        t.rt(120)
    t.end_fill()
    
def outer_sun(x,y,z,length):
    pen_placer(x,y,z)
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(40):
        t.fd(length)
        t.lt(130)
        t.fd(length)
        t.rt(120)
    t.end_fill()
        
def cloud(x,y,z,length,radius,extent):
    pen_placer(x,y,z)
    t.fillcolor("white")
    t.begin_fill()
    t.fd(length)
    for i in range(9):
        circle(radius,extent)
        t.lt(180)
    t.end_fill()
        
def portrait(x,y,z,l1,l2):
    pen_placer(x,y,z)
    t.fillcolor("#7F461B")
    t.begin_fill()
    square(l1,l2)
    t.end_fill()
    pen_placer(x+25,y+25,z)
    t.fillcolor("#87CEEB")
    t.begin_fill()
    square(l1-50,l2-50)
    t.end_fill()
             
def main():
    t.screensize(1000,500)
    t.speed(0)
    t.pencolor("black")
#     inner portrait
    

    portrait(-150,-150,0,300,400)
    # middle_trees(-105,-125,0,10,100,50)
    middle_bushes(-85,-125,0,4,-200)
    inner_sun(-125,175,0,50,90,10)
    # cloud(-15,130,0,100,8.7,200)

    left_trees(-500,-150,0,20,150,100)
    left_bushes(-440,-150,0,7,-200)
    right_trees(500,-150,0,20,150,100)
    right_bushes(240,-150,0,7,-200)
    outer_sun(250,300,300,15)
    # cloud(-100,260,0,200,17.5,200)
    # cloud(-550,260,0,300,26,200)
    # cloud(350,260,0,250,22,200)

    


    
    t.hideturtle()
    t.done()
        
if __name__ == "__main__":
    main()
    
    
    
    
    