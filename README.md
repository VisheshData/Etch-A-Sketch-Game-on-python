# Etch-a-Sketch Game with Turtle
This project recreates the classic Etch-a-Sketch drawing game using Python's turtle module. The game allows users to move a turtle in various directions and change its color while drawing on the screen. The player can control the movement and colors using specific keys. This project demonstrates key programming concepts such as higher-order functions, event listeners, and basic Object-Oriented Programming (OOP).

## How to Play
The Etch-a-Sketch game allows you to control the turtle (representing the drawing pen) using the following keys:

W: Move forward
S: Move backward
A: Rotate counterclockwise
D: Rotate clockwise
R: Change the pen color to red
G: Change the pen color to green
B: Change the pen color to blue
C: Clear the screen and reset the turtle's position

## Concepts Used
### Object-Oriented Programming (OOP)
In this project, the Turtle object from Python's turtle module is used to represent the pen. The Turtle class provides various methods to control the turtle’s movement and appearance, such as forward(), back(), right(), left(), and pencolor().

### Higher-Order Functions
Higher-order functions are functions that can take other functions as arguments or return them as results. In this game, higher-order functions are used in conjunction with event listeners. Each movement and color change is handled by individual functions (e.g., move_forward, colorchangered), which are then passed to screen.onkey() to be triggered by specific key presses.

### Event Listeners
Event listeners allow the program to wait for and respond to user input, such as keyboard presses. The screen.onkey() function from the turtle module is used to set up event listeners that call specific functions when the user presses certain keys.

For example, when the "W" key is pressed, the move_forward() function is triggered, moving the turtle forward.

Code Explanation
Movement Functions
```python
Copy code
def move_forward():
    tim.forward(10)

def move_backward():
    tim.back(10)

def clockwise():
    tim.right(10)

def anticlockwise():
    tim.left(10)
```
These functions control the movement of the turtle.
move_forward() and move_backward() move the turtle 10 units in the current direction.
clockwise() and anticlockwise() rotate the turtle 10 degrees to the right and left, respectively.
Color Change Functions
```python

def colorchangered():
    tim.pencolor("red")

def colorchangegreen():
    tim.pencolor("green")

def colorchangeblue():
    tim.pencolor("blue")
```
These functions change the turtle's pen color. Each function calls tim.pencolor() with a specific color argument.
Pressing "R" changes the pen color to red, "G" changes it to green, and "B" changes it to blue.
Clearing the Screen
```python

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
```
The clear() function clears the screen and resets the turtle’s position to the center of the screen (home()).
It uses penup() and pendown() to ensure that the turtle doesn't draw while moving to the center.
### How to Run the Game
Clone the repository to your local machine and run it.

Use the keys W, A, S, D to move the turtle and R, G, B to change its color.

### Future Enhancements
Adding more color options.
Allowing the user to adjust the pen width.
Creating different shapes like squares, circles, etc.
