import turtle
import random

row_set = col_set = tile_dict = dict()
for i in range(1, 10):
    row_set = col_set = tile_dict[i] = set()


def drawing(x, y, n):  # Drawing the board
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    for row in range(n):  # Draws row lines
        if not row:
            y = turtle.ycor()
        elif not row % 3:
            turtle.pensize(3)
        else:
            turtle.pensize(1)
        turtle.forward(450)
        turtle.penup()
        turtle.goto(x, y - 50*(row+1))
        turtle.pendown()
    else:
        turtle.penup()
        turtle.setpos(x, y)
        turtle.right(90)
        turtle.pendown()
    for col in range(n):  # Draws col lines
        if not col:
            x = turtle.xcor()
        elif not col % 3:
            turtle.pensize(3)
        else:
            turtle.pensize(1)
        turtle.forward(450)
        turtle.penup()
        turtle.goto(x + 50*(col+1), y)
        turtle.pendown()
    else:
        turtle.penup()
        turtle.setpos(x, y)
        turtle.left(90)
        turtle.pensize(5)
        turtle.pendown()
    for outline in range(4):  # Draws outline
        turtle.forward(450)
        turtle.right(90)
    else:
        turtle.pensize(1)


def row_check(num, row):
    if len(row_set[row]) == 9:
        row += 1
    elif num not in row_set[row]:
        row_set.add(num)


def col_check(num, col):
    if num not in col_set:
        row_set.add(num)
    pass


def tile_check(tile):
    global row_num, col_num
    temp_num = random.randint(1, 9)
    if True:  # Write the condition later
        row_check(temp_num, row_num)
        col_check(temp_num, col_num)
    pass


def filling():
    pass


def extract_num():
    pass


def clear_board():
    pass


if __name__ == '__main__':
    turtle.speed(0)
    # turtle.hideturtle()
    drawing(-300, 200, 9)
    row_num = col_num = tile_num = 1
    # temp_num = random.randint(1, 9)
    turtle.exitonclick()
