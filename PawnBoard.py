#Author: Daniel Fontenot
#Date: 5-17-20
#Description: Project 9 PawnBoard Class. Provides rules and condition checks for a 4x4 game of pawns.
# Refer to readme or descriptions below for comprehensive discussion of each method.


class PawnBoard:
    """
    Creates and coordinates a 4x4 "Pawnboard" game. Game consists of 4 pawns on an "o" team and "x" team.
    Winner is determined by reaching the opponent's starting position.
    Pawns's legal moves are those traditional to chess, minus 2 space staring jump.
    Updates the board with each user input turn.
    Checks and updates the state of the board game amongst UNFINISHED, O_WON, X_WON, DRAW.
    """

    def __init__(self):
        self._pawnboard_list = [["x","","","o"],["x","","","o"],["x","","","o"],["x","","","o"]]
        self._current_state = "UNFINISHED"

    def get_current_state(self):
        """
        Returns current_state of game: UNFINISHED, O_WON, X_WON, DRAW.
        Locks game if win or draw conditions are returned.
        """
        return self._current_state

    def get_pawnboard_list(self):
        """
        Returns the pawnboard_list.
        """
        return self._pawnboard_list

    def set_pawnboard_list(self,new_pawnboard_list):
        """
        Sets the pawnboard_list.
        Functionally not required, but good "best practice".
        """
        self._pawnboard_list = new_pawnboard_list

    def set_current_state(self):
        """
        Determines if the pawnboard game condition. X_WON, O_WON, DRAW, UNFINISHED.
        I;X_List = "outer" pawnboard_list ; pawnboard columns
        i;Y_nlist = nested pawnboard_list ; pawnboard rows
        unfinished_counter = Determines DRAW vs UNFINISHED state ; count of pawns that have at least one available move.
        """

        #Initialize variables.

        X_List = -1
        unfinished_counter = 0
        grid = (0, 1, 2, 3)
        self.get_pawnboard_list()
        pawnboard_list = self._pawnboard_list

        #Iterate through all pawnboard spaces.

        for I in pawnboard_list:
            X_List += 1
            Y_nlist = -1
            for i in I:
                Y_nlist += 1

                #Check winning team state.

                if (i == "o") and (Y_nlist == grid[0]):
                    self._current_state = "O_WON"
                    return self._current_state

                elif (i == "x") and (Y_nlist == grid[-1]):
                    self._current_state = "X_WON"
                    return self._current_state

                #Determine Draw or Unfinished state.
                #Iterate through pawnboard to determine available moves for each pawn.

                elif (i == "o"):
                    if (X_List-1) not in grid: #prevent check at -1 column, i.e., I[-1].
                        if ((pawnboard_list[X_List][Y_nlist - 1] == "") or (pawnboard_list[X_List + 1][Y_nlist - 1] == "x")):
                            unfinished_counter += 1
                    elif (X_List+1) not in grid: #prevent check at non-existent 5th column, i.e., I[4].
                        if ((pawnboard_list[X_List][Y_nlist - 1] == "") or (pawnboard_list[X_List - 1][Y_nlist - 1] == "x")):
                            unfinished_counter += 1
                    else: #check all three movement options.
                        if ((pawnboard_list[X_List][Y_nlist - 1] == "") or (pawnboard_list[X_List + 1][Y_nlist - 1] == "x") or (pawnboard_list[X_List - 1][Y_nlist - 1] == "x")):
                            unfinished_counter += 1

                elif (i == "x"):
                    if (X_List-1) not in grid: #prevent check at -1 column, i.e., I[-1].
                        if ((pawnboard_list[X_List][Y_nlist + 1] == "") or (pawnboard_list[X_List + 1][Y_nlist + 1] == "o")):
                            unfinished_counter += 1
                    elif (X_List+1) not in grid: #prevent check at non-existent 5th column, i.e., I[4].
                        if ((pawnboard_list[X_List][Y_nlist + 1] == "") or (pawnboard_list[X_List - 1][Y_nlist + 1] == "o")):
                            unfinished_counter += 1
                    else: #check all three movement options.
                        if ((pawnboard_list[X_List][Y_nlist + 1] == "") or (pawnboard_list[X_List + 1][Y_nlist + 1] == "o") or (pawnboard_list[X_List - 1][Y_nlist - 1] == "o")):
                            unfinished_counter += 1

        #Tally unfinished_counter to determine DRAW or UNFINISHED state.

        if unfinished_counter == 0:
            self._current_state = "DRAW"
            return self._current_state
        else:
            self._current_state = "UNFINISHED"
            return self._current_state

    def make_move(self, Y1, X1, Y2, X2):
        """
        User provides two coordinates for a single pawn: starting location and destination.
        Checks and prevents illegal moves and confirms game is still UNFINISHED prior to executing pawn move.
        """

        # Get pawnboard and game state; Prevent pawn movement if game state is WON or DRAW.

        self.get_pawnboard_list()
        pawnboard_list = self._pawnboard_list
        self.get_current_state()
        if self._current_state != "UNFINISHED":
            return False

        #Prevent input coordinates not on PawnBoard_list, (i.e., input < 0; input > 3)

        grid = (0, 1, 2, 3)
        if (X1 not in grid) or (Y1 not in grid) or (X2 not in grid) or (Y2 not in grid):
            return False

        #Define variables.

        empty = ""
        Y_move = Y2 - Y1
        X_move = X2 - X1
        ini_pos = (pawnboard_list[X1][Y1]) #Initial Position of Pawn. Index to pull pawn or empty space.
        des_pos = (pawnboard_list[X2][Y2]) #Destination Position of Pawn. Index to pull another pawn or empty space.

        # Check Vertical-Y-Row movement == -1 for team "o"; +1 for team "x"
        # Check Horizontal-X-Col movement == 0(base move) or -1/1(attack move)

        if (abs(Y_move) != 1) or (X_move < -1) or (X_move > 1):
            return False

        # Execute team "o" pawn move.

        if (ini_pos == "o") and (Y_move == -1):
            # base move
            if (X_move == 0) and (des_pos == empty):
                (pawnboard_list[X2][Y2]) = (pawnboard_list[X1][Y1])
                (pawnboard_list[X1][Y1]) = empty
            # attack move
            elif ((X_move == -1) or (X_move == 1)) and ((des_pos == "x")):
                (pawnboard_list[X2][Y2]) = (pawnboard_list[X1][Y1])
                (pawnboard_list[X1][Y1]) = empty
            else:  # 'o' Pawn forward motion blocked, or 'x' Pawn not at destination for attack.
                return False

        # Execute team "x" pawn move.

        elif (ini_pos == "x") and (Y_move == 1):
            # base move
            if (X_move == 0) and (des_pos == empty):
                (pawnboard_list[X2][Y2]) = (pawnboard_list[X1][Y1])
                (pawnboard_list[X1][Y1]) = empty
            # attack move
            elif ((X_move == -1) or (X_move == 1)) and ((des_pos == "o")):
                (pawnboard_list[X2][Y2]) = (pawnboard_list[X1][Y1])
                (pawnboard_list[X1][Y1]) = empty
            else:  # 'x' Pawn forward motion blocked, or 'o' Pawn not at destination for attack.
                return False
        else: # Pawn cannot move backwards.
            return False

        self.set_pawnboard_list(pawnboard_list)
        self.set_current_state()

        return True

"""
pawnboard_list
matrix of pawnboard
draw condition example
print_pawnboard_set

#pawnboard_list = [["x","","","o"],["x","","","o"],["x","","","o"],["x","","","o"]] #starting list

# 03 #13 #23 #33     o team
# 02 #12 #22 #32
# 01 #11 #21 #31
# 00 #10 #20 #30     x team

#Draw Condition
game = PawnBoard()
game.make_move(0,0,1,0)
game.make_move(0,2,1,2)
game.make_move(3,1,1,2)
game.make_move(3,3,2,2)
game.make_move(3,0,4,0)
game.make_move(3,0,2,0)
game.make_move(3,1,3,1)
game.make_move(3,1,2,1)
game.make_move(2,1,1,1)
game.make_move(3,2,2,2)
game.make_move(0,3,1,3)
game.make_move(1,3,2,3)
print(game.get_current_state())
game2 = PawnBoard()
game2.make_move(3,1,0,1)
game2.make_move(0,3,1,1)
game2.make_move(0,1,1,1)
game2.make_move(0,0,0,1)
game2.make_move(3,1,2,0)
game2.make_move(0,3,2,2)
game2.make_move(0,4,3,1)
game2.make_move(0,3,1,3)
game2.make_move(3,2,2,2)
game2.make_move(2,2,3,1)
game2.make_move(2,2,1,3)
game2.make_move(1,3,0,2)
game2.make_move(3,2,2,2)
game2.make_move(3,0,2,0)
print(game2.get_current_state())
# (Y1, X1, Y2, X2)

Print Pawn_Board
print("_ |  0 |  1 |  2 |  3 ")
print("3 |",pawnboard_list[0][3]," | ",pawnboard_list[1][3]," | ",pawnboard_list[2][3]," | ",pawnboard_list[3][3])
print("2 |",pawnboard_list[0][2]," | ",pawnboard_list[1][2]," | ",pawnboard_list[2][2]," | ",pawnboard_list[3][2])
print("1 |",pawnboard_list[0][1]," | ",pawnboard_list[1][1]," | ",pawnboard_list[2][1]," | ",pawnboard_list[3][1])
print("0 |",pawnboard_list[0][0]," | ",pawnboard_list[1][0]," | ",pawnboard_list[2][0]," | ",pawnboard_list[3][0])
"""