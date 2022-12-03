
# from MiniMaxImplemented import MinimaxAlgorithm

def rule(piece, empty_space):
    """This function implements the rules of a valid playable position. The inputs to the function are 
        the piece that is intented to be played and a charactor representing an empty_space. 
    """
    if piece == empty_space:
        return True
    else:
        return False 

# def getValidPositions(board, rule, empty_space):
#     """ This function checks and returns a dictionary of all the locations of all valid play moves. The input 
#         given the fuction are the board, the rule function that implementes the rules of what valid position 
#         is and an a charactor that represents an empty_space.
#     """
#     position_dictionary = []
#     # number of columns = number of row =  lenght of board
#     for i in range(0, len(board)):
#         for j in range(0, len(board)):
#            if rule(board[i][j], empty_space) == True:
#                position_dictionary.append([i,j])
#     return position_dictionary
                 
# def isBoardFull(board, empty_space):
#     """ This function checks if a board is full or not, given the board and charactor that represents empty space. 
#         If a board is full, this fucntion return True, and when the board is not full the function returns False
#     """
#     # number of columns = number of row =  lenght of board
#     for i in range(0, len(board)):
#         for j in range(0, len(board)):
#             if board[i][j] == empty_space:
#                 return False
#     return True


# def isDiagonalSouthEastWin(board, piece):
#     """
#         This function check if the cuurent piece wins on the south-east diagonal given as input the piece and the board
#     """
#     for i in range(0, len(board)):
#         if board[i][i] != piece:
#             return False
#     return True     

# def isDiagonalSouthWestWin(board, piece):
#     """
#         This function check if the cuurent piece wins on the south-west diagonal given as input the piece and the board
#     """
#     for i in range(0, len(board)):
#         if board[i][len(board) -1-i] != piece:
#             return False
#     return True     

# def isVerticalWin(board, piece):
#     """ 
#         This fucntion check if the current player wins on the vertical direction on three verical blocks,
#         given as inputs the board and the pieces to be checked and return True if the player win ans False otherwise
#     """
#     for i in range(0, len(board)):
#         if((board[0][i] == piece) and (board[0][i] == board[1][i]) and (board[1][i] == board[2][i])):
#             return True
#     return False   

# def isHorizontalWin(board, piece):
#     """ 
#         This fucntion check if the current player wins on the horizontal direction on three horozontal blocks, 
#         given as inputs the board and the pieces to be checked and return True if the player win ans False otherwise
#     """
#     for i in range(0, len(board)):
#         if((board[i][0] == piece) and (board[i][0] == board[i][1]) and (board[i][1] == board[i][2])):
#             return True
#     return False

# def isWinning(board, piece):
#     """ This function checks if a place of the given piece  wins the game or not. The function checks 
#         digonal, vertical and horizontal wins. The function return True for a win and False for a lose
#     """
#     # diagonal , horizonatal and vertical check    
#     if isDiagonalSouthEastWin(board, piece) or isDiagonalSouthWestWin(board, piece) or isHorizontalWin(board, piece) or isVerticalWin(board, piece):
#         return True

#     return False

# def getAIPlayPosition(board, algorithm, piece, empty_space):
#     """
#     This function simulates the AI playing, it applies the minimax algorithm on the current board state and determines the best move
#     """
#     best_score = -800
#     best_move = (0, 0)
#     validPlayPositions = getValidPositions(board, rule, empty_space)
#     for pos in validPlayPositions:
#         board[pos[0]][pos[1]] = piece
#         score = algorithm.minimax(board, False, isWinning, isBoardFull)
#         board[pos[0]][pos[1]] = empty_space
#         if score > best_score:
#             best_score = score 
#             best_move = (pos[0], pos[1]) 
#     return best_move




class GameEngine:
    def __init__(self):
        self.player_1_piece = 'X'
        self.player_2_piece = 'O'

        self.empty_space = '*'
        self.board_size =  3
        self.board = self.initilizeBoard()    
        self.current_playing_piece = self.player_1_piece

        # algorithm = MinimaxAlgorithm(game_engine.player_1_piece, game_engine.player_2_piece, game_engine.empty_space)


        return

    def initilizeBoard(self):
        """ 
           This function initialized the board with empty blocks, the function return the board and does not take any inputs.
        """
        board = [[self.empty_space for i in range(self.board_size)] for i in range(self.board_size)]
        return board 

    def isBoardFull(self):
        """ 
            This function checks if a board is full or not, given the board and charactor that represents empty space. 
            If a board is full, this fucntion return True, and when the board is not full the function returns False
        """
        # number of columns = number of row =  lenght of board
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                if self.board[i][j] == self.empty_space:
                    return False
        return True

    def rule(self, piece, empty_space):
        """
            This function implements the rules of a valid playable position. The inputs to the function are 
            the piece that is intented to be played and a charactor representing an empty_space. 
        """
        if piece == empty_space:
            return True
        else:
            return False         

    def isDiagonalSouthEastWin(self, piece):
        """
            This function check if the cuurent piece wins on the south-east diagonal given as input the piece and the board
        """
        for i in range(0, self.board_size):
            if self.board[i][i] != piece:
                return False
        return True     

    def isDiagonalSouthWestWin(self, piece):
        """
            This function check if the cuurent piece wins on the south-west diagonal given as input the piece and the board
        """
        for i in range(0, self.board_size):
            if self.board[i][self.board_size -1-i] != piece:
                return False
        return True     

    def isVerticalWin(self, piece):
        """ 
            This fucntion check if the current player wins on the vertical direction on three verical blocks,
            given as inputs the board and the pieces to be checked and return True if the player win ans False otherwise
        """
        for i in range(0, self.board_size):
            if((self.board[0][i] == piece) and (self.board[0][i] == self.board[1][i]) and (self.board[1][i] == self.board[2][i])):
                return True
        return False   

    def isHorizontalWin(self, piece):
        """ 
            This fucntion check if the current player wins on the horizontal direction on three horozontal blocks, 
            given as inputs the board and the pieces to be checked and return True if the player win ans False otherwise
        """
        for i in range(0, self.board_size):
            if((self.board[i][0] == piece) and (self.board[i][0] == self.board[i][1]) and (self.board[i][1] == self.board[i][2])):
                return True
        return False

    def isWinning(self, piece):
        """ 
            This function checks if a place of the given piece  wins the game or not. The function checks 
            digonal, vertical and horizontal wins. The function return True for a win and False for a lose
        """
        # diagonal , horizonatal and vertical check    
        if self.isDiagonalSouthEastWin(piece) or self.isDiagonalSouthWestWin(piece) or self.isHorizontalWin(piece) or self.isVerticalWin(piece):
            return True
        return False

    def getValidPositions(self):
        """ 
            This function checks and returns a dictionary of all the locations of all valid play moves. The input 
            given the fuction are the board, the rule function that implementes the rules of what valid position 
            is and an a charactor that represents an empty_space.
        """
        position_dictionary = []
        # number of columns = number of row =  lenght of board
        for i in range(0, self.board_size):
            for j in range(0, self.board_size):
                if rule(self.board[i][j], self.empty_space) == True:
                    position_dictionary.append([i,j])
        return position_dictionary

    def setBoard(self, board):
        """
            This function set the board to a new board state. The function takes in a board as input and does not return
        """
        self.board = board
        return

    def getBoard(self):
        """
            This function return the current board.
        """
        return self.board

    def getAIPlayPosition(self, algorithm, piece):
        """
        This function simulates the AI playing, it applies the minimax algorithm on the current board state and determines the best move
        """
        best_score = -800
        best_move = (0, 0)
        validPlayPositions = self.getValidPositions()
        for pos in validPlayPositions:
            self.board[pos[0]][pos[1]] = piece
            score = algorithm.minimax(self.board, False, self.isWinning, self.isBoardFull)
            self.board[pos[0]][pos[1]] = self.empty_space
            if score > best_score:
                best_score = score 
                best_move = (pos[0], pos[1]) 
        return best_move

    def isValidMove(self, position):
        currentValidPositions = self.getValidPositions()
        for valid_pos in currentValidPositions:
            if valid_pos == list(position):
                return True
        return False


    def play(self, position):
        """
        This function playes a pieces on the for if the position is valid and playable.
        """
        if self.isValidMove(position) == True:
            self.board[position[0]][position[1]] = self.current_playing_piece
            
            if self.current_playing_piece == self.player_1_piece:
                self.current_playing_piece = self.player_2_piece 
            elif self.current_playing_piece == self.player_2_piece:
                self.current_playing_piece = self.player_1_piece
                
        return
  
    def getPersonPlayerPosition(self):
        position = ()
        while True:
            (row, column) = self.getInputPosition()
            position = (row, column)
            if self.isEmpty(position) == True:
              break
            else:
              print("Block occupied, please play again")
        return 
    
    def isEmpty(self, position):
        if self.board[position[0]][position[1]] == self.empty_space:
            return True
        return False
            
    def getInputPosition(self):

        # to be overritten by GUI input

        row = int(input("Enter row position: "))
        column = int(input("Enter column position: "))
        return (row, column)

    def resetBoard(self):
        self.board = self.initilizeBoard()
        self.current_playing_piece = self.player_1_piece
        return

