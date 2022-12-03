
""" Minimax algorithm with a checkWin function for Tic Tac Toe Game and isBoardFull checker function
"""

from GameEngine import *

class MinimaxAlgorithm:
    def __init__(self, player_1_piece, player_2_piece, empty_space):
        self.game_engine = GameEngine()
        self.player_1_piece = player_1_piece
        self.player_2_piece = player_2_piece
        self.empty_space = empty_space
        return
    
    def maximize(self, board):
        self.game_engine.setBoard(board)
        best_score = -800
        validPlayPositions = self.game_engine.getValidPositions()
        for pos in validPlayPositions:
            board[pos[0]][pos[1]] = self.player_1_piece
            score = self.minimax(board, False, self.game_engine.isWinning, self.game_engine.isBoardFull) 
            board[pos[0]][pos[1]] = self.empty_space
            if score > best_score:
                best_score = score  
        return best_score               


    def minimize(self, board):
        self.game_engine.setBoard(board)
        best_score = 800
        validPlayPositions = self.game_engine.getValidPositions()
        for pos in validPlayPositions:
            board[pos[0]][pos[1]] = self.player_2_piece
            score = self.minimax(board, True, self.game_engine.isWinning, self.game_engine.isBoardFull) 
            board[pos[0]][pos[1]] = self.empty_space
            if score < best_score:
                best_score = score  
        return best_score               


    def minimax(self, board, isMaximizing, checkWin, checkBoardFull):
        if checkWin(self.player_1_piece):
            return 1  
        if checkWin(self.player_2_piece):
            return -1  
        if checkBoardFull():
            return 0
    
        if isMaximizing == True:
            return self.maximize(board)
        else:
            return self.minimize(board)

