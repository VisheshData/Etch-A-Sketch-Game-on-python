from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.back(10)

def clockwise():
    tim.right(10)

def anticlockwise():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



def colorchangered():
    tim.pencolor("red")

def colorchangegreen():
    tim.pencolor("green")

def colorchangeblue():
    tim.pencolor("blue")


screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(clockwise,"d")
screen.onkey(anticlockwise,"a")
screen.onkey(clear,"c")
screen.onkey(colorchangered,"r")
screen.onkey(colorchangegreen,"g")
screen.onkey(colorchangeblue,"b")
screen.listen()
screen.exitonclick()