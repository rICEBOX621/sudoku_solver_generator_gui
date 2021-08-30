from tkinter import messagebox, Tk, Canvas, Frame, Button, BOTH, TOP, LEFT
from tkinter.constants import FALSE, TRUE
from board_solver import solve, is_valid
from generate_board import assign_board, sudoku_board, print_board


WIDTH = 600
HEIGHT = 600
SIDE_WIDTH = 30
BOX_SPACING = 60

class Sudoku(Frame):

  board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
  ]

  ui_board = []
  solution = []

  def __init__(self, parent):
    Frame.__init__(self, parent)
    self.row = -1
    self.col = -1
    self.myRect = ""
    self.__startScreen()

  def __startScreen(self):
    self.pack(fill=BOTH, expand=1)
    self.canvas = Canvas(self, width=WIDTH, height=HEIGHT)
    self.canvas.pack(fill=BOTH, side=TOP)

    check_button = Button(self, text="Check Solution", command=self.check_answers)
    clear_button = Button(self, text="Clear Input", command=self.clear_answers)
    solution_button = Button(self, text="Generate Solution", command=self.generate_solution)
    new_board_button = Button(self, text="New Board", command=self.generate_new_board)

    check_button.pack(ipadx=32, side=LEFT)
    clear_button.pack(ipadx=36, side=LEFT)
    solution_button.pack(ipadx=26, side=LEFT)
    new_board_button.pack(ipadx=41, side=LEFT)
    
    self.draw_board()

    self.canvas.bind("<Button-1>", self.click)
    self.canvas.bind("<Key>", self.input_nums)
    
  def check_answers(self):
    solve(self.solution)
    print("-----------------------------------")
    print_board(self.solution)
    is_victory = TRUE
    for i in range(len(self.board)):
      for j in range(len(self.board)):
        if self.solution[i][j] != self.ui_board[i][j]:
          is_victory = FALSE
          self.canvas.itemconfigure(tagOrId=str(i) + "_" + str(j), fill="red")
    if is_victory:
      self.victory_screen()

  def victory_screen(self):
    messagebox.showinfo(title="VICTORY!", message="Congratulations! You beat the board! Press 'New Board' to generate a new board")

  def clear_answers(self):
    for i in range(len(self.board)):
      for j in range(len(self.board)):
        if self.ui_board[i][j] != self.board[i][j]:
          self.canvas.delete(str(i)+ "_" +str(j))

  def generate_solution(self):
    solve(self.solution)
    for i in range(len(self.board)):
      for j in range(len(self.board)):
        if self.solution[i][j] != self.ui_board[i][j]:
          x_coor = SIDE_WIDTH + j * BOX_SPACING + BOX_SPACING / 2
          y_coor = SIDE_WIDTH + i * BOX_SPACING + BOX_SPACING / 2
          self.canvas.create_text(x_coor, y_coor, text=self.solution[i][j], fill="black", tags="board")
    
    messagebox.showinfo(message="Press 'New Board' to generate a new board")

  def generate_new_board(self):
    self.board = [
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    self.ui_board = []
    self.solution = []
    self.canvas.delete('all')
    self.draw_board()

  def draw_board(self):
    #draws in the 9 * 9 grid of sudoku
    for i in range(10): 
      color = "black" if i % 3 == 0 else "grey"

      x0 = SIDE_WIDTH + i * BOX_SPACING
      y0 = SIDE_WIDTH
      x1 = SIDE_WIDTH + i * BOX_SPACING
      y1 = HEIGHT - SIDE_WIDTH
      self.canvas.create_line(x0, y0, x1, y1, fill=color, tags="lines")

      x0 = SIDE_WIDTH
      y0 = SIDE_WIDTH + i * BOX_SPACING
      x1 = WIDTH - SIDE_WIDTH
      y1 = SIDE_WIDTH + i * BOX_SPACING
      self.myRect = self.canvas.create_line(x0, y0, x1, y1, fill=color, tags="lines")

    assign_board(self.board)
    
    print_board(sudoku_board(self.board))
    for i in range(9):
      self.ui_board.append(list(self.board[i]))
      self.solution.append(list(self.board[i]))
    print("-----------------------------------")

    #draws the puzzle
    for i in range(9):
      for j in range(9):
        number = self.board[i][j]
        if number != 0:
          x_coor = SIDE_WIDTH + j * BOX_SPACING + BOX_SPACING / 2
          y_coor = SIDE_WIDTH + i * BOX_SPACING + BOX_SPACING / 2
          self.canvas.create_text(x_coor, y_coor, text=number, fill="black", tags="board")
  
  def click(self, event):
    #if the click is inside the sudoku board
    if SIDE_WIDTH < event.x < WIDTH - SIDE_WIDTH and SIDE_WIDTH < event.y < HEIGHT - SIDE_WIDTH:
      self.canvas.focus_set()
      row = (event.y - SIDE_WIDTH) / BOX_SPACING
      col = (event.x - SIDE_WIDTH) / BOX_SPACING

      if self.board[int(row)][int(col)] == 0:
        if self.row != -1 and self.col != -1:
          self.canvas.delete(self.myRect)
        self.row = int(row)
        self.col = int(col)
        
    else: 
      self.row = -1
      self.col = -1

    self.draw_box()

  def draw_box(self):
    if self.row != -1 and self.col != -1:
      x_coor = SIDE_WIDTH + self.col * BOX_SPACING + 1
      y_coor = SIDE_WIDTH + self.row * BOX_SPACING + 1
      x_width = SIDE_WIDTH + (self.col + 1) * BOX_SPACING - 1
      y_len = SIDE_WIDTH + (self.row + 1) * BOX_SPACING - 1
      self.myRect = self.canvas.create_rectangle(x_coor, y_coor, x_width, y_len, outline="red", tags='highlight')

  def input_nums(self, event):
    if self.row != -1 and self.col != -1 and event.char in "123456789":
      self.ui_board[self.row][self.col] = int(event.char)
      print("-----------------------------------")
      print_board(self.ui_board)
      self.draw_nums()

  def draw_nums(self):
    if self.ui_board[self.row][self.col] != self.board[self.row][self.col]:
      if self.ui_board[self.row][self.col] != 0:
        self.canvas.delete(str(self.row)+ "_" +str(self.col))
      x_coor = SIDE_WIDTH + self.col * BOX_SPACING + BOX_SPACING / 2
      y_coor = SIDE_WIDTH + self.row * BOX_SPACING + BOX_SPACING / 2
      self.canvas.create_text(x_coor, y_coor, text=self.ui_board[self.row][self.col], fill="blue", tags=str(self.row)+ "_" +str(self.col))

if __name__ == '__main__':
  root = Tk()
  root.title("Sudoku Generating and Solving Algorithm")
  sudoku = Sudoku(root)
  root.mainloop()