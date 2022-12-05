board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0],[-1, 0, 1, 0, 0, 0, 0], [-1, 1, -1, 0, 0, 0, 0]]


def evaluate_lines(board, grille, i, j):
    print('grille \n' + str(grille))
    ligne = board.getRow(i)
    #print(ligne)
    colonne = board.getCol(j)
    #print(colonne)
    diagonale_up = board.getDiagonal(True, j)
    #print(diagonale_up)
    diagonale_down = board.getDiagonal(False, j)
    #print(diagonale_down)
    return

def evaluate_board(board):
    """ Evaluate the board """
    heuristique = 0
    
    #PLAYER1
    score1=0

    #for i in range (6):
    #    ligne = grille[i]
    #    for j in range (7):
    #        if ligne[j]==1:
    #            evaluate_lines(board, grille, i, j)

        
    return heuristique