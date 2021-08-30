from board_solver import is_valid, find_empty_space
import random

def assign_board(board):
  empty_coor = find_empty_space(board)
  if not empty_coor:
    return True #no empty coordinates were found, therefore the board must be a complete board (we will have checked that is a valid board as well)
  x, y = empty_coor
  arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  random.shuffle(arr)
  for i in range(len(arr)):
    if is_valid(board, x, y, arr[i]):
      board[x][y] = arr[i]

      if assign_board(board):
        return True
      
      board[x][y] = 0
  
  return False

def sudoku_board(board):
  clues_potentially_removed = random.randint(1, 64)
  arr_len = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  arr_width = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  random.shuffle(arr_len)
  random.shuffle(arr_width)

  for i in range(len(arr_len)):
    for j in range(len(arr_width)):
      removing_bool = random.randint(0,1)
      if clues_potentially_removed > 0 and removing_bool == 1:
        board[arr_len[i]][arr_width[j]] = 0
  
  return board

def print_board(board):
  for i in range(len(board)):
    if i % 3 == 0 and i != 0:
      print("- - - - - - - - - - - - - - -")
    for j in range(len(board)):
      if j % 3 == 0 and j != 0:
        print("| ", end="")
      if j == 8:
        print(board[i][j])
      else:
        print(board[i][j], " ", end="")


