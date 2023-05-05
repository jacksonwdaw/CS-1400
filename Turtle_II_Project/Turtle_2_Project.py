'''
this program takes a series of objects and draws a picture, but before anything is drawn a question is asked at the terminal to determine the season.
'''
import turtle as t
import sys

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

def the_big_frame(l1,l2,season_color):
    if season_color == 1:
        season_color = '#8ad8f6'
    elif season_color == 2:
        season_color = '#c3f9ff'
    t.fillcolor(season_color)
    t.begin_fill()
    pen_placer(-500,-250,0)
    square(l1,l2)
    t.end_fill()
 

def portrait(season_color,l1,l2):
    if season_color == 1:
        season_color = '#7bc7dd'
    elif season_color == 2:
        season_color = '#86feff'
    pen_placer(-150,-250,0)
    t.fillcolor("#7F461B")
    t.begin_fill()
    square(l1,l2)
    t.end_fill()
    pen_placer(-125,-225,0)
    t.fillcolor(season_color)
    t.begin_fill()
    square(l1-50,l2-50)
    t.end_fill()

def portrait_ground(season_color,x,y,l1,l2):
    if season_color == 1:
        season_color = '#81d681'
    elif season_color == 2:
        season_color = '#bb9b60'
    t.fillcolor(season_color)
    t.begin_fill()
    pen_placer(x,y,0)
    square(l1,l2)
    t.end_fill()  

def tree(season_color,x,y,z,scale):
    l1 = scale*10
    l2 = scale*100
    length = scale*50
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
    if season_color == 1:
        season_color = '#304529'
    elif season_color == 2:
        season_color = '#f05133'
    t.fillcolor(season_color)
    t.begin_fill()
    for i in range(3):
        triangle(length)
        t.lt(90)
        t.penup()
        t.fd(length * .3)
        t.rt(90)
        t.pendown()
    t.end_fill()

def user_input():
    try:
        season_pick = int(input("Pick a Season, 1 for Summer, 2 for Winter: "))
    except ValueError:
        print("please enter 1 or 2.")
        return
    season_color = 0
    if season_pick == 1:
        season_color = 1
    elif season_pick == 2:
        season_color = 2
    return season_color

def cloud(season_color,x,y,z,radius,extent):
    pen_placer(x,y,z)
    if season_color == 1:
        season_color = '#d3d3d3'
    elif season_color == 2:
        season_color = '#696969'
    t.fillcolor(season_color)
    t.begin_fill()
    for i in range(9):
        circle(radius,extent)
        t.lt(180)
    t.goto(x,y)
    t.end_fill()
    
def bush(season_color,x,y,z,radius,extent):
    pen_placer(x,y,z)
    if season_color == 1:
        season_color = '#4b8b3b'
    elif season_color == 2:
        season_color = '#9c5708'
    t.fillcolor(season_color)
    t.begin_fill()
    for i in range(9):
        circle(radius,extent)
        t.lt(180)
    t.goto(x,y)
    t.end_fill()

def inner_sun(season_color, x,y,z,radius,extent,length):
    pen_placer(x,y,z)
    if season_color == 1:
        season_color = '#FFFF66'
    elif season_color == 2:
        season_color = '#FFC02E'
    t.fillcolor(season_color)
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

def mountain(season_color,x,y,z,length):
    pen_placer(x,y,z)
    t.fillcolor('#6A5A5D')
    t.begin_fill()
    triangle(length)
    t.end_fill()
    t.fillcolor('white')
    t.begin_fill()
    if season_color == 1:
        season_color = triangle(length*.25)
    elif season_color == 2:
        season_color = triangle(length*.4)
    t.end_fill()

def outer_sun(season_color,x,y,z,length):
    pen_placer(x,y,z)
    if season_color == 1:
        season_color = '#FFFF66'
    elif season_color == 2:
        season_color = '#FFC02E'
    t.fillcolor(season_color)
    t.begin_fill()
    for i in range(40):
        t.fd(length)
        t.lt(130)
        t.fd(length)
        t.rt(120)
    t.end_fill()

def get_objects():
    return {
        'outer_mountain_1':{'x_pos':-350,"y_pos":300,'heading':240,'length':300,'function': mountain},
        'outer_mountain_2':{'x_pos':-225,"y_pos":270,'heading':240,'length':300,'function': mountain},
        'outer_mountain_3':{'x_pos':-135,"y_pos":310,'heading':240,'length':300,'function': mountain},
        'outer_mountain_4':{'x_pos':10,"y_pos":250,'heading':240,'length':300,'function': mountain},
        'outer_mountain_5':{'x_pos':156,"y_pos":350,'heading':240,'length':300,'function': mountain},
        'outer_mountain_6':{'x_pos':350,"y_pos":300,'heading':240,'length':300,'function': mountain},
        'the_ground':{'x_pos':-500,"y_pos":-250,'l1':1000,'l2':350,'function': portrait_ground},
        'portrait':{'l1':300,'l2':400,'function': portrait},
        'inner_mountain_1':{'x_pos':0,"y_pos":50,'heading':240,'length':150,'function': mountain},
        'inner_mountain_2':{'x_pos':-50,"y_pos":40,'heading':240,'length':150,'function': mountain},
        'inner_mountain_3':{'x_pos':50,"y_pos":40,'heading':240,'length':150,'function': mountain},
        'portrait_ground':{'x_pos':-125,"y_pos":-225,'l1':250,'l2':150,'function': portrait_ground},
        'small_sun':{'x_pos':-125,'y_pos':75,'z_pos':0,'radius':50, 'extent':90, 'length':10, 'function': inner_sun},
        'big_sun':{'x_pos':200,'y_pos':325,'z_pos':0, 'length':15, 'function': outer_sun},
        'inner_cloud':{'x_pos':90,'y_pos':40,'z_pos':0,'radius':10, 'extent':200, 'function': cloud},
        'outer_cloud_1':{'x_pos':50,'y_pos':250,'z_pos':0,'radius':15, 'extent':200, 'function': cloud},
        'outer_cloud_2':{'x_pos':-200,'y_pos':300,'z_pos':0,'radius':20, 'extent':200, 'function': cloud},
        'outer_cloud_3':{'x_pos':350,'y_pos':250,'z_pos':0,'radius':20, 'extent':200, 'function': cloud},
        'inner_tree_1':{'x_pos':-100,'y_pos':-150,'z_pos':0,'scale':1, 'function': tree},
        'inner_tree_2':{'x_pos':-10,'y_pos':-200,'z_pos':0,'scale':1, 'function': tree},
        'inner_tree_3':{'x_pos':80,'y_pos':-170,'z_pos':0,'scale':1, 'function': tree},
        'outer_tree_1':{'x_pos':-450,'y_pos':-112,'z_pos':0,'scale':2, 'function': tree},
        'outer_tree_2':{'x_pos':-250,'y_pos':-175,'z_pos':0,'scale':2, 'function': tree},
        'outer_tree_3':{'x_pos':250,'y_pos':-90,'z_pos':0,'scale':2, 'function': tree},
        'outer_tree_4':{'x_pos':400,'y_pos':-125,'z_pos':0,'scale':2, 'function': tree},
        'inner_bush_1':{'x_pos':-30,'y_pos':-200,'z_pos':0,'radius':4, 'extent':200, 'function': bush},
        'inner_bush_2':{'x_pos':70,'y_pos':-175,'z_pos':0,'radius':4, 'extent':200, 'function': bush},
        'outer_bush_1':{'x_pos':-325,'y_pos':-150,'z_pos':0,'radius':7, 'extent':200, 'function': bush},
        'outer_bush_2':{'x_pos':375,'y_pos':-100,'z_pos':0,'radius':7, 'extent':200, 'function': bush},
    }

def draw(args):
    # args = sys.argv[1:]
    if 'summer' in args:
        season_color = 1
    elif 'autumn' in args:
        season_color = 2
    else:
        season_color = user_input()
    
        
    print(args)
    t.screensize(1000,500)
    t.bgcolor("#5A5A5A")
    t.speed(0)
    t.pencolor("black")
    the_big_frame(1000,700,season_color)
    objects = get_objects()
    for key, object_info in objects.items():
        object_info['function'](season_color, *tuple(list(object_info.values())[:-1]))
    t.hideturtle()
        
if __name__ == "__main__":
    draw()