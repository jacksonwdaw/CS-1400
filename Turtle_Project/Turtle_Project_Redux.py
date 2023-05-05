import turtle
t = turtle



def death_rune(radius, extent, width):
    t.pencolor((220,128,8))
    t.width(width)
    t.circle(radius, extent)
    t.circle(radius, extent - 90)
    t.circle(radius, extent)
    for i in loop
    
def godrick_rune(degree, length, radius):
    t.width(7)
    t.pencolor((246, 235, 97))
    t.lt(degree)
    t.fd(length)
    t.rt(degree)
    t.circle(radius)
    
def morgott_rune(degree, length, radius):
    t.pencolor((255, 184, 28))
    t.lt(degree)
    t.fd(length)
    t.rt(degree-35)
    t.circle(radius)
    
def malenia_and_radahn(degree, radius):
    t.pencolor((187, 0, 0))
    t.lt(degree/2)
    t.circle(radius)
    t.pencolor((75, 54, 95))
    t.rt(degree)
    t.circle(radius)
    
def rune_line(degree, length, width):
    t.width(width)
    t.rt(degree)
    t.fd(length-85)
    t.pencolor((255, 184, 28))
    t.fd(length+235)
    t.pencolor((220,128,8))
    t.fd(length)
    t.backward(length-70)
    t.lt(degree)
    
def lil_rune_line(degree, length, width):
    t.lt(degree)
    t.width(width)
    t.pencolor((255, 184, 28))
    t.fd(length)
    t.rt(degree)
    
def screen_bits(color, x, y):
    t.bgcolor(color)
    t.colormode(255)
    t.speed(0)
    t.pu()
    t.goto(x,y)
    t.pd()
    
def get_dimensions():
    try:
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
    except ValueError:
        print("Please enter positive integers")
        return width, height
    if width < 0 or height < 0:
        print("Please enter positive integers")
        return width, height
    draw(width,height) 
    

def draw(width, height):
    t.screensize(width, height)
    screen_bits("black", 0, 200)
    death_rune(250, 30, 5.5)
    rune_line(90, 100, 7)
    death_rune(450, 30, 5)
    godrick_rune(90, 100, 100)
    malenia_and_radahn(70, 83)
    morgott_rune(125, 50, 94)
    death_rune(300, 30, 4.5)
    lil_rune_line(90, 90, 7)
    death_rune(210, 30, 4)
    t.hideturtle()
    
def main():
    get_dimensions()

if __name__ == "__main__":
    main()
    
    
# if __name__ == "__main__":
#     draw(width, height)