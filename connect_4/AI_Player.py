from maxConnect4Game import maxConnect4Game
import sys
from copy import deepcopy as supercopy
class AI_Player:

    def __init__ (self, depth):
        self.depth=depth
        self.ai_game=None


    def getChildren(self, game):
        # print ("get children")
        board=game.gameBoard
        children={}
        cols=[]
        for c in range(0, len(board[0])):

            if not board[0][c]:

                children[c]=game.playPiece(c)
                # children[c].printGameBoard
                # print("parent currentTurn: ", self.ai_game.currentTurn)
                # children[c].printGameBoard()
        return children

    #uses a minimax tree to determine what the next best move will be
    def getBestMove(self, b ):
        self.ai_game=maxConnect4Game(None, b, 1)
        childMoves=self.getChildren(self.ai_game)
        maxVal=float(-sys.maxsize)
        bestBoard=None
        for col, boardConfig in childMoves.items():
            # boardConfig.printGameBoard()
            minVal=self.getMinValue(boardConfig,-sys.maxsize, sys.maxsize, 1 )
            if minVal>maxVal:
                bestBoard=boardConfig.gameBoard
            maxVal=max(minVal, maxVal)

        return bestBoard


    def getMaxValue(self, game, alpha, beta, curr_depth):
        if game.isOver():
            return game.utility()
        if curr_depth==self.depth:
            return game.evaluation()
        # print ("Max current depth: ", curr_depth)
        # print ("Max ideal depth: ", self.depth)
        childMoves=self.getChildren(game)
        maxVal=float(-sys.maxsize)
        for col, gameConfig in childMoves.items():
            minVal=self.getMinValue(gameConfig, alpha, beta, curr_depth+1)
            maxVal=max(maxVal,minVal)
            #alpha beta pruning
            if maxVal >=beta:
                return maxVal
            alpha=max(alpha, maxVal)
        return maxVal

    def getMinValue(self, game, alpha, beta, curr_depth):
        if game.isOver():
            return game.utility()
        if curr_depth==self.depth:
            return game.evaluation()
        # print ("Min current depth: ", curr_depth)
        # print ("Min ideal depth: ", self.depth)

        #need to eval chidren
        childMoves=self.getChildren(game)
        minVal=float(sys.maxsize)
        for col, gameConfig in childMoves.items():
            maxVal=self.getMaxValue(gameConfig, alpha, beta, curr_depth+1)
            minVal=min(maxVal,minVal)

            #alpha beta pruning
            if minVal <=alpha:
                return minVal

            beta=min(beta, minVal)

        return minVal
