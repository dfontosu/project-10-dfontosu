# project-9

Write a class called PawnBoard that represents the board for a two-player game played on a 4x4 square grid.  The board starts with an 'x' in each column of row zero and an 'o' in each column of row 3.  Each player is trying to get one of their pieces to the opposite side.  A piece can only move one square toward the other side of the board.  Pieces move straight unless capturing an opponent's piece, in which case they move diagonally (still only toward the other side of the board) and replace the captured piece.  As soon as any piece reaches the opposite side of the board, that player wins.

The class should have two private data members - a list of lists that represents the board, and the current state, which holds one of the four following values: "X_WON", "O_WON", "DRAW", or "UNFINISHED". It should have a get method named get_current_state, which returns the current state.

The class should have an init method that initializes the board to a list of 4 lists, with the pieces represented as 'x's and 'o's, and empty squares represented by empty strings ("").  It should also initialize the current state to "UNFINISHED".

It should have a method named make_move that takes four parameters: the row and column (in that order) of the piece being moved, and the row and column (in that order) of the square being moved to.  All rows and columns will be in the range 0-3.  **It's possible for multiple moves to be made in a row for the same player (so you don't need to enforce alternating turns).**  If there is no piece at the first row and column, or if the move is not legal, or if the game has already been won or drawn, make_move should return False.  Otherwise, it should record the move, update the current state if the move caused a win or draw, and return True.  A game is drawn when neither player has any legal moves.

It's not required, but you'll probably find it useful for testing and debugging to have a method that prints out the board.

Whether you think of the array indices as being [row][column] or [column][row] doesn't matter as long as you're consistent.

Your class only represents the board, it doesn't actually allow two players to play the game.  Other code (that you don't have to write) would use your PawnBoard class to make that happen.

For example, your class could be used as follows:
```
board = PawnBoard()
board.make_move(0, 0, 1, 0)
board.make_move(0, 2, 1, 2)
board.make_move(3, 1, 2, 1)
board.make_move(1, 2, 2, 1)
board.get_current_state()
```
Your file must be named: PawnBoard.py
