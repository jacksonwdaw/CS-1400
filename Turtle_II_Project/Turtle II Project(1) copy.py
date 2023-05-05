import turtle as t

def triangle(length):
    for i in range(3):        
        t.fd(length)
        t.lt(120)
        
def square(turtle,l1, l2):
    for i in range(2):
        turtle.fd(l1)
        turtle.lt(90)
        turtle.fd(l2)
        turtle.lt(90)
        
def circle(radius, extent):
    t.circle(radius, extent)

def pen_placer(turtle,x,y,z):
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(z)
    turtle.pendown()

def the_big_frame(l1,l2):
    pen_placer(-500,-250,0)
    square(l1,l2)

def portrait(l1,l2):
    pen_placer(-150,-250,0)
    t.fillcolor("#7F461B")
    t.begin_fill()
    square(l1,l2)
    t.end_fill()
    pen_placer(-125,-225,0)
    t.fillcolor("#87CEEB")
    t.begin_fill()
    square(l1-50,l2-50)
    t.end_fill()

def createTree():
    treeShape = t.Turtle()
    x=1
    return tree(treeShape, x,0,0,10,100,50)

def tree(treeShape, x,y,z,l1,l2,length):
    pen_placer(treeShape,x,y,z)
    treeShape.fillcolor("#48260D")
    treeShape.begin_fill()
    square(treeShape,l1,l2)
    treeShape.end_fill()
    treeShape.lt(90)
    treeShape.fd(l2)
    treeShape.lt(90)
    treeShape.fd(l1 * 2)
    treeShape.rt(180)
    treeShape.fillcolor('green')
    treeShape.begin_fill()
    for i in range(3):
        triangle(length)
        treeShape.lt(90)
        treeShape.penup()
        treeShape.fd(length * .3)
        treeShape.rt(90)
        treeShape.pendown()
    treeShape.end_fill()
    return t

def main():
    t.screensize(1000,500)
    t.speed(0)
    t.pencolor("black")
    createTree()
    # the_big_frame(1000,700)
    # portrait(300,400)
    # for i in range(3):
    #     t.goto(10,30)
    #     t.shape('circle')
    #     t.color('blue')
    #     stamploc = t.stamp()



    t.hideturtle()
    t.done()
        
if __name__ == "__main__":
    main()