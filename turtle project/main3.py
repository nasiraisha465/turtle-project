import turtle
turtle.Screen().bgcolor("green")
sc = turtle.Screen()
sc.setup(400,300)
turtle.title("welcome to turtle window")
board = turtle.Turtle()
for i in range(6):
    board.forward(90)
    board.left(300)
sc.mainloop()