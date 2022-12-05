from player import Player
import copy
from board import Board
import numpy as np 
import random
import utils
​
​
def get_board_winner(board, pos):
    """ Return the winner, or None after a element to pos position."""
    tests = []
    tests.append(board.getCol(pos[0]))
    tests.append(board.getRow(pos[1]))
    tests.append(board.getDiagonal(True, pos[0] - pos[1]))
    tests.append(board.getDiagonal(False, pos[0] + pos[1]))
    for test in tests:
        color, size = utils.longest(test)
        if size >= 4:
            # print(color)
            return color
            
    return None
​
​
def heuristique2(board, num):
    matrix = []
    pointSeen = []
    for i in range(6):
        if num == -1:
            matrix.append([-x for x in board.getRow(i)])
        else:
            matrix.append(board.getRow(i))
    # print(matrix)
        
​
​
    def listPoint(matrix):
        listpoint = []
        for line in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[line][col] == 1:
                    listpoint.append((line,col))
        return listpoint
​
    def firstCheckList(point, matrix):
        checkList = []
        if point[0] - 1 >= 0 and matrix[point[0]-1][point[1]] != -1 and (point[0]-1, point[1]) not in pointSeen :
            checkList.append((point[0]-1, point[1]))
        if point[0] - 1 >= 0 and point[1] -1 >=0 and matrix[point[0]-1][point[1] - 1] != -1 and (point[0]-1, point[1] - 1) not in pointSeen :
            checkList.append((point[0]-1, point[1] - 1))
        if point[0] - 1 >= 0 and point[1] +1 <7 and matrix[point[0]-1][point[1] + 1] != -1 and (point[0]-1, point[1] + 1) not in pointSeen:
            checkList.append((point[0]-1, point[1] + 1))
        if point[0] + 1 < 6 and matrix[point[0]+1][point[1]] != -1 and (point[0]+1, point[1]) not in pointSeen:
            checkList.append((point[0]+1, point[1]))
        if point[0] + 1 <6  and point[1] - 1 >=0 and matrix[point[0]+1][point[1] - 1] != -1 and (point[0]+1, point[1] - 1) not in pointSeen:
            checkList.append((point[0]+1, point[1] - 1))
        if point[0] + 1 < 6 and point[1] + 1 < 7 and matrix[point[0]+1][point[1] + 1] != -1 and (point[0]+1, point[1] + 1) not in pointSeen:
            checkList.append((point[0]+1, point[1] + 1))
        if  point[1] + 1 <7 and matrix[point[0]][point[1] + 1] != -1 and (point[0], point[1] + 1) not in pointSeen:
            checkList.append((point[0], point[1] + 1))
        if  point[1] - 1 >=0 and matrix[point[0]][point[1] - 1] != -1 and (point[0], point[1] - 1) not in pointSeen:
            checkList.append((point[0], point[1] - 1))
        return checkList
    
​
    def secondCheckList(point,firstCheckList, matrix):
        checkList = []
        for secondPoint in firstCheckList:
            thirdPoint = (secondPoint[0]*2 - point[0] , secondPoint[1] * 2 - point[1])
            if thirdPoint[0] >= 0 and thirdPoint[1] >= 0 and thirdPoint[0] < 6 and thirdPoint[1] < 7 and matrix[thirdPoint[0]][thirdPoint[1]] != -1 and thirdPoint not in pointSeen:
                checkList.append(thirdPoint)
        return checkList
​
​
    def thirdCheckList(point,secondCheckList, matrix):
        checkList = []
        for thirdPoint in secondchecklist:
            fourthPoint = (int(thirdPoint[0] +(thirdPoint[0] - point[0])/2) , int(thirdPoint[1] +(thirdPoint[1] - point[1])/2))
            # print("point : ", point, "third point : ", thirdPoint, "fourth point : ", fourthPoint)
            if fourthPoint[0] >= 0 and fourthPoint[1] >= 0 and fourthPoint[0] < 6 and fourthPoint[1] < 7 and matrix[fourthPoint[0]][fourthPoint[1]] != -1 and fourthPoint not in pointSeen:
                checkList.append(fourthPoint)
        return checkList
​
    listpoint = listPoint(matrix)
    score = 0
​
    for point in listpoint:
        firstchecklist = firstCheckList(point,matrix)
        # print("first")
        secondchecklist = secondCheckList(point,firstchecklist, matrix)
        # print("second")
        thirdchecklist = thirdCheckList(point, secondchecklist, matrix)
        # print("third")
        listFinale = firstchecklist + secondchecklist + thirdchecklist
        # print(listFinale)
        dictAngle = { }
        for pointVoisin in listFinale:
            if pointVoisin[1] != point[1]:
                angle = ((pointVoisin[0] - point[0])/(pointVoisin[1] - point[1]))
            else:
                angle = "inf"
​
            if angle in dictAngle.keys():
                dictAngle[angle] += 1
            else:
                dictAngle[angle] = 1
​
        # print(dictAngle)
        for key in dictAngle.keys():
            score += max(0,dictAngle[key] - 2 )
​
        pointSeen.append(point)
​
    return score
    
​
# matrixTest = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,-1,0,0,0], [0,0,-1,1,1,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]
​
​
# print(heuristique2(matrixTest,1))
​
​
​
class AIPlayer(Player):
    """This player should implement a heuristic along with a min-max and alpha
    beta search to """
	
    def __init__(self, numJoueur=1):
        self.name = "Mercure"  
        self.num = numJoueur
​
    def getColumn(self, board):
        def minMax(index, board, stepMax, step, alpha, beta):
            
            if board.isFull(): return 0, 0
​
            elif step >= stepMax: 
                    return 0, heuristique2(board, self.num)
                    
            else:
                if index == self.num:
                    actionmax = 0
                    vmax = -999999999999
                    for column in board.getPossibleColumns():
                        copyBoard = copy.deepcopy(board)
                        row = copyBoard.play(self.num,column)
                        winner = get_board_winner(copyBoard, (column, row))
                        
                        if winner == self.num:
                            return column,999999999 # np.Inf if we are the first player, -np.Inf if we are the second player.
​
                        v = minMax(-self.num,copyBoard,stepMax,step, alpha, beta)[1]
                        if v > vmax:
                            vmax = v
                            actionmax = column
                        if vmax >= beta:
                            return actionmax, vmax
                        alpha = max(alpha, vmax)
                    return actionmax,vmax
​
                else:
                    step +=1
                    vmin = 9999999999999999
                    actionmin = 0
                    for column in board.getPossibleColumns():
                        copyBoard = copy.deepcopy(board)
                        row = copyBoard.play(-self.num,column)
                        winner = get_board_winner(copyBoard, (column, row))
                        
                        if winner == -self.num:
                            # print(column, row)
                            return column, 99999999 * -1 
​
​
                        v = minMax(self.num,copyBoard,stepMax,step, alpha, beta)[1]
                        if v < vmin:
                            vmin = v
                            actionmin =column
                        if vmin <= alpha: 
                            return actionmin, vmin
                        beta = min(beta, vmin)
​
                    return actionmin,vmin
​
        return minMax(self.num, board, 2, 0, -999999999999999999999999, 999999999999999999999999999)[0]