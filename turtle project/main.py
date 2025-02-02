import turtle
turtle.Screen().bgcolor("pink")
sc = turtle.Screen()
sc.setup(400,300)
turtle.title("welcome to turtle window")
board = turtle.Turtle()
for i in range(3):
    board.forward(100)
    board.left(120)
sc.mainloop()
