def solve(board):
  empty_coor = find_empty_space(board)
  if not empty_coor:
    return True #no empty coordinates were found, therefore the board must be a complete board (we will have checked that is a valid board as well)
  x, y = empty_coor
  for i in range(1, 10):
    if is_valid(board, x, y, i): #if a valid solution can be produced
      board[x][y] = i

      if solve(board): #recursive element (keeps on solving board)
        return True

      board[x][y] = 0 #case in which we must backtrack
  return False


def find_empty_space(board):
  for i in range(len(board)):
    for j in range(len(board[0])):
      if board[i][j] == 0: 
        return (i,j)
  return False

def is_valid(board, x, y, value):
  #check individual square to see if it is valid
  box_init_x = (x // 3) * 3
  box_init_y = (y // 3) * 3
  for i in range(box_init_x, box_init_x + 3):
    for j in range(box_init_y, box_init_y + 3):
      if i == x and j == y:
        continue
      elif board[i][j] == value:
        return False
      else:
        continue

  #check row to see if it is valid
  for i in range(len(board)):
    if board[x][i] == value:
      return False
  #check col to see if it is valid
  for j in range(len(board[0])):
    if board[j][y] == value:
      return False
  return True
