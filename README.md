This project allows for the user to play and check answers for sudoku boards. Each sudoku board is generated and solved using a backtracking algorithm specified below.

*solver.py*
The sudoku solver is able to solve a sudoku board using a backtracking algorithm. 
1) The solver looks to find an empty space, if an empty space is not found, the algorithm returns true.
2) In the case the empty space is found, we look to insert a valid number by means of a helper (checks the rows, cols, and cube)
3) Once we check the validity of the number, if it is valid, we then insert that number into the empty space.
4) We then recursively look to solve the board.
5) In the instance that none of the numbers (1-9) work, then we return false and recurse backwards, trying the next valid number.
6) By the end of the program, the initial board will be returned as the solved sudoku board.

*generator.py*
1) Using an empty sudoku board, we perform the solver algorithm with a twist.
2) Instead of going sequentially for the valid numbers, we will choose a random number from 1-9. 
3) By the end of this process, a valid sudoku board will have been generated.
4) The numbers are then removed randomly such that AT LEAST 17 clues remain on the board (to make this a possible game)
5) The algorithm then returns a solvable sudoku board that the GUI will then utilize. 

*gui.py*
- Using tkinter, the user is able to play sudoku off of the generated board
- The options of 'check solution', 'clear input', 'generate solution', and 'new board' exist
Check Solution: Allows the user to check their input to the solution, changing the user input values from blue to red if the input is incorrect
Clear Input: Clears any input that the user has put in
Generate Solution: Gives the solution of the sudoku board
New Board: Generates a new board that the user can play
