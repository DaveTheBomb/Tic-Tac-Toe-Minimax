
def main():
    
    running = True
    board = generateBoard(3)
    
    pieceX = 'X'
    pieceO = 'O'
    empty_space = '*'
    
    turn = 1
    while(running):
        print(printBoard(board))
        #do while loop modelling
        position = ()
        while True:
            (row, column) = getInputPosition()
            position = (row, column)
            if isEmpty(board, position, empty_space):
              break
            else:
              print("Block occupied, please play again")
        
        if turn == 1:
            play(position, board ,pieceX)
            if checkWin(board, pieceX) == True:
                print("Player X wins")
                break
          
        if turn == -1:
            play(position, board ,pieceO)
            if checkWin(board, pieceO) == True:
                print("Player O wins")
                break

        if (isBoardFull(board, '*') ==  True):
            break  
        turn *= -1

    if (isBoardFull(board, '*') == True):
        print("Tie")
        
    print(printBoard(board))
    return
    
def getInputPosition():
    row = int(input("Enter row position: "))
    column = int(input("Enter column position: "))
    return (row, column)

def isBoardFull(board, empty_space):
    number_of_rows = len(board)
    number_of_columns = len(board[0])
    for i in range(0, number_of_rows):
        for j in range(0, number_of_columns):
            if board[i][j] == empty_space:
                return False
    return True

def printBoard(board):
    number_of_rows = len(board) 
    output = ""
    for row in board:
        output_row = ""
        for x in row:
            output_row = output_row  + "\t" + x 
        output = output + "\n" + output_row
    return output

def checkWin(board, piece):
    # diagonal check
    number_of_rows = len(board)
    number_of_columns = len(board[0])
    if((board[0][0] == piece) and (board[0][0] == board[1][1]) and (board[1][1] == board[2][2])):
        return True
    if((board[0][2] == piece) and (board[0][2] == board[1][1]) and (board[1][1] == board[2][0])):
        return True
       
    # vertical check
    for i in range(0,number_of_columns):
        if((board[0][i] == piece) and (board[0][i] == board[1][i]) and (board[1][i] == board[2][i])):
            return True
    # horizontal check
    for i in range(0,number_of_rows):
        if((board[i][0] == piece) and (board[i][0] == board[i][1]) and (board[i][1] == board[i][2])):
            return True
    
    return False
        
        
def isEmpty(board, position, empty_space):
  if board[position[0]][position[1]] == empty_space:
    return True
  return False
        
        
def generateBoard(board_size):
    board = [['*' for i in range(1, board_size + 1)] for i in range(1, board_size + 1)]
    return board

def play(position, board ,piece):
    board[position[0]][position[1]] = piece
    return   

if __name__ == "__main__":
    main()