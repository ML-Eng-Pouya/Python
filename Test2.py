import turtle
import random


def drawing_board(x=-300, y=250):
    turtle.tracer(0)
    row = turtle.Turtle()
    col = turtle.Turtle()
    row.hideturtle()
    col.hideturtle()
    row.penup()
    col.penup()
    row.setposition(x, y)
    col.setposition(x, y)
    col.right(90)
    row.speed(0)
    col.speed(0)
    row.pendown()
    col.pendown()

    for i in range(10):
        if i == 0 or i == 9:
            row.pensize(5)
            col.pensize(5)
        elif not(i % 3):
            row.pensize(3)
            col.pensize(3)
        else:
            row.pensize(1)
            col.pensize(1)
        row.forward(450)
        col.forward(450)
        row.penup()
        col.penup()
        row.goto(x, y - 50 * (i+1))
        col.goto(x + 50 * (i+1), y)
        row.pendown()
        col.pendown()
# ___________________________
    my_list = [i for i in range(1, 10)]
    random.shuffle(my_list)
    sudoku_board = list()
    for i in range(3):
        if not i:
            sudoku_board.append(my_list[:])
        else:
            sudoku_board.append(sudoku_board[i - 1][3:])
            sudoku_board[i].extend(sudoku_board[i - 1][:3])
    for i in range(3):
        sudoku_board.append(sudoku_board[i][1:])
        sudoku_board[i + 3].extend(sudoku_board[i][:1])
    for i in range(3):
        sudoku_board.append(sudoku_board[i][2:])
        sudoku_board[i + 6].extend(sudoku_board[i][:2])
    turtle.tracer(0)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x+25, y-50)
    turtle.pendown()
    counter = 1
    for element in sudoku_board:
        counter += 1
        while len(element):
            turtle.write(element[0], move=False, align='center', font=('Arial', 25, 'normal'))
            element.pop(0)
            turtle.penup()
            turtle.forward(50)
            turtle.pendown()
        else:
            turtle.penup()
            turtle.goto(x+25, y - 50 * counter)
            turtle.pendown()
    turtle.exitonclick()


# def fill_the_board(x=-300, y=250):
#     my_list = [i for i in range(1, 10)]
#     random.shuffle(my_list)
#     sudoku_board = list()
#     for i in range(3):
#         if not i:
#             sudoku_board.append(my_list[:])
#         else:
#             sudoku_board.append(sudoku_board[i - 1][3:])
#             sudoku_board[i].extend(sudoku_board[i - 1][:3])
#     for i in range(3):
#         sudoku_board.append(sudoku_board[i][1:])
#         sudoku_board[i + 3].extend(sudoku_board[i][:1])
#     for i in range(3):
#         sudoku_board.append(sudoku_board[i][2:])
#         sudoku_board[i + 6].extend(sudoku_board[i][:2])
#     turtle.speed(0)
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     counter = 0
#     for element in sudoku_board:
#         counter += 1
#         while len(element):
#             turtle.write(element[0], move=False, align='center', font=('Arial', 20, 'normal'))
#             element.pop(0)
#             turtle.penup()
#             turtle.forward(50)
#             turtle.pendown()
#         else:
#             turtle.penup()
#             turtle.goto(x, y - 50 * counter)
#             turtle.pendown()


def empty_cells():
    pass

def solve():
    pass



if __name__ == '__main__':
    drawing_board()
