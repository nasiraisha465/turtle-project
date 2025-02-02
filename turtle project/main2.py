import turtle
turtle.Screen().bgcolor("purple")
sc = turtle.Screen()
sc.setup(400,300)
turtle.title("welcome to turtle window")
board = turtle.Turtle()
for i in range(4):
    board.forward(140)
    board.left(90)
sc.mainloop()