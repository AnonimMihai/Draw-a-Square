import turtle
import time

def perimeterCLI():
    global side
    try:
        side = int(input("What is the length of one side of the square? (px)\n"))
    except:
        print("Sorry but you entered something wrong.\nExit code: 534")
        time.sleep(3)
        exit()
    print(f"The perimeter of your square is: {side*4} px.")
    drawSquare()


def drawSquare():
    canvas = turtle.Turtle()
    canvas.penup()
    canvas.setposition(x=-360, y=0)
    canvas.pendown()
    for i in range(0, 4):
        canvas.forward(side)
        canvas.left(90)
    turtle.done()
