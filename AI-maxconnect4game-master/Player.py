###############################################################################
##  Name - Suyog S Swami
##  Subject: CSE5360 Artificial Intelligence 1
##  Assignement: MaxConnect4 game using Minimax and alpha beta pruning
##  Students ID: 1001119101
###############################################################################

import MaxConnect4Game as m
import time

class Player:
    def __init__(self):
        initialGameboard = m.MaxConnect4Game()
        depth_limit=0

    def setInitState(self,inputFile,gameMode,nextPlayer):
        self.initialGameboard = m.MaxConnect4Game()
        self.initialGameboard.setBoardFromFile(inputFile,gameMode,nextPlayer)
        self.initialGameboard.printGameBoard()
        return self.initialGameboard

    def minimaxDecision(self, initialGameboard):
        score = 0
        move = -1
        starttime = time.time()
        matrix = self.successor(initialGameboard)
        v = float(-100000)
        for k in matrix.iterkeys():
            temp = self.minValue(matrix[k], alpha=-100000, beta=100000, depth=1)
            if temp >= v:
                v = temp
                move = k
        endtime = time.time()
        print 'Time :', (endtime-starttime)
        isvalid, demo = initialGameboard.playPiece(move)
        return demo, move, v

    def successor(self, gameboard):
        matrix = {}
        nCol = gameboard.numberofpossibleColumns()
        for i in range(len(nCol)):
            move = nCol.pop()
            isValid, newGameboard = gameboard.playPiece(move)
            matrix[move] = newGameboard
        return matrix

    def maxValue(self,currentGameboard, alpha, beta, depth):
        v = float(-100000)
        cnt = currentGameboard.checkPieceCount()
        if cnt == 42:
            util = currentGameboard.utility()
            return util
        elif depth == self.depth_limit:
            score = currentGameboard.evaluation()
            return score
        else:
            depth = depth + 1
            matrix = self.successor(currentGameboard)
            for k in matrix.iterkeys():
                board = matrix[k]
                temp = self.minValue(board, alpha, beta, depth)
                if temp >= v:
                    v = temp
                    move = k
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v

    def minValue(self, currentGameboard, alpha, beta, depth):
        v = float(100000)
        cnt = currentGameboard.checkPieceCount()
        if cnt == 42:
            util = currentGameboard.utility()
            return util
        if depth == self.depth_limit:
            score = currentGameboard.evaluation()
            return score
        else:
            depth = depth + 1
            matrix = self.successor(currentGameboard)
            for k in matrix.iterkeys():
                board = matrix[k]
                temp = self.maxValue(board, alpha, beta, depth)
                if temp <= v:
                    v = temp
                    move = k
                if v <= alpha:
                    return  v
                beta = min(beta, v)
            return v