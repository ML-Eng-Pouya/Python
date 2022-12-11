"""
1. Design the board
2. functions that enable user to fill the board (markdown)
3. class / function to generate numbers based on sudoku rule
4. eliminate numbers so that remaining numbers illustrate a solvable puzzle
"""
# base  = 3
# side  = base*base
#
# # pattern for a baseline valid solution
# def pattern(r,c): return (base*(r%base)+r//base+c)%side
#
# # randomize rows, columns and numbers (of valid base pattern)
# from random import sample
# def shuffle(s): return sample(s,len(s))
# rBase = range(base)
# rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
# cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
# nums  = shuffle(range(1,base*base+1))
#
# # produce board using randomized baseline pattern
# board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
#
# for line in board: print(line)
# squares = side*side
# empties = squares * 3//4
# for p in sample(range(squares),empties):
#     board[p//side][p%side] = 0
#
# numSize = len(str(side))
# for line in board:
#     print(*(f"{n or '.':{numSize}} " for n in line))
#
# def shortSudokuSolve(board):
#     size    = len(board)
#     block   = int(size**0.5)
#     board   = [n for row in board for n in row ]
#     span    = { (n,p): { (g,n)  for g in (n>0)*[p//size, size+p%size, 2*size+p%size//block+p//size//block*block] }
#                 for p in range(size*size) for n in range(size+1) }
#     empties = [i for i,n in enumerate(board) if n==0 ]
#     used    = set().union(*(span[n,p] for p,n in enumerate(board) if n))
#     empty   = 0
#     while empty>=0 and empty<len(empties):
#         pos        = empties[empty]
#         used      -= span[board[pos],pos]
#         board[pos] = next((n for n in range(board[pos]+1,size+1) if not span[n,pos]&used),0)
#         used      |= span[board[pos],pos]
#         empty     += 1 if board[pos] else -1
#         if empty == len(empties):
#             solution = [board[r:r+size] for r in range(0,size*size,size)]
#             yield solution
#             empty -= 1
# shortSudokuSolve(board)
