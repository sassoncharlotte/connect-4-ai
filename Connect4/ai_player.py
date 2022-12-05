from tkinter import Grid
from player import Player
import copy


class AIPlayer(Player):
    """This player should implement a heuristic along with a min-max and alpha
    beta search to """
	
    def __init__(self):
        self.name = "Charlotte"
        self.index = 0
    
    def getColumn(self, board):

        new_board = copy.deepcopy(board)

        def minimax(index, new_board):
            print('index :' + str(index))

            if index == 0:
                actionmax=0
                vmax = -99999999999
                liste = new_board.getPossibleColumns()
                print('colonnes : ' + str(liste))
                for column in liste:
                    new_board.play(1,column)
                    v = minimax(0,new_board)[1]
                    if v > vmax:
                        vmax = v
                        actionmax = column
                return actionmax, vmax

            else:
                vmin = 99999999999
                actionmin = 0
                liste = new_board.getPossibleColumns()
                print('colonnes : ' + str(liste))
                for column in liste:
                    # print("action : ", str(action), "legal actions : ", state.getLegalActions(index))
                    new_board.play(0,column)
                    v = minimax(0,new_board)[1]
                    if v < vmin:
                        vmin = v
                        actionmin =column
                return actionmin, vmin
                
        colonne = minimax(0, new_board)[0]
        print(colonne)