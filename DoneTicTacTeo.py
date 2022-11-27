"""
Author:   Siphamandla Malaza
Date:     November 2022

Description: Tic-Tac-Toe game iplemtation using pygame graphics library. The game applies the minimax algorithm to create a smart AI. 
"""


import pygame
from pygame.locals import *
import math


def main():
  
    """ GUI variable initialization"""
    pygame.init()
    clock = pygame.time.Clock()
    block_size = 60
    off_set = block_size/2
    board_line_color = (20, 108, 164)
    screen = pygame.display.set_mode((60*6, 60*6))
    background = (4, 124, 140)
    time_passed = clock.tick(60) / 1000
    
    """ Logic  variable initialization"""


    pieceX = 'X'
    pieceO = 'O'
    empty_space = '*'
        
    running, playerXWin, playerOWin, Draw, board, turn = initializeGame()

    while(running):
      
        drawBoardOnScreen(screen,  board_line_color, block_size, background, board, empty_space)
        pygame.display.flip()
      
        print(printBoard(board))

        if turn == -1:
            position = getAIMove(board, empty_space, pieceX, pieceO)
            play(position, board ,pieceX)
            drawBoardOnScreen(screen,  board_line_color, block_size, background, board, empty_space)
                
            if checkWin(board, pieceX) == True:
                print("Player X wins")
                playerXWin = True

                displayEndgameText(screen, playerXWin, playerOWin, Draw)
                listenToEvent()
                running, playerXWin, playerOWin, Draw, board, turn = initializeGame()   
                drawBoardOnScreen(screen,  board_line_color, block_size, background, board, empty_space)
                pygame.display.flip()
          
        if turn ==  1:
            position = () 
            while True:        
                position = getPlayerInputFromBoard(pygame, block_size)
                print(position)
                if ((isValidInput(position[0], position[1]) == False) or (board[position[0]][position[1]] != empty_space)):
                    print("Select block")  
                else:
                    break
  
            play(position, board ,pieceO)
            drawBoardOnScreen(screen,  board_line_color, block_size, background, board, empty_space)            
          
            if checkWin(board, pieceO) == True:
                print("Player O wins")
                playerOWin =  True

                displayEndgameText(screen, playerXWin, playerOWin, Draw)
                listenToEvent()
                running, playerXWin, playerOWin, Draw, board, turn = initializeGame()  
                drawBoardOnScreen(screen,  board_line_color, block_size, background, board, empty_space)
                pygame.display.flip()


        turn *= -1

        if (isBoardFull(board, empty_space) ==  True):
            print("Tie")
            Draw =  True
            drawBoardOnScreen(screen,  board_line_color, block_size, background, board, empty_space)
            displayEndgameText(screen, playerXWin, playerOWin, Draw)
            pygame.display.flip()
            listenToEvent()
            running, playerXWin, playerOWin, Draw, board, turn = initializeGame()   
     
    return

def getInputPosition():
    row = int(input("Enter row position: "))
    column = int(input("Enter column position: "))
    return (row, column)


def displayEndgameText(screen, playerXWin, playerOWin, Draw):
    if playerXWin == True:
        placeText(screen, "Player X Wins", 'freesansbold.ttf', 20, (90, 105), (0, 255, 0))
    if playerOWin ==  True:
        placeText(screen, "Player O Wins", 'freesansbold.ttf', 20, (90, 105), (0, 255, 0))
    if Draw == True:
        placeText(screen, "Draw", 'freesansbold.ttf', 20, (90, 105), (0, 255, 0))  
    placeText(screen, "Press Enter To Play Again!", 'freesansbold.ttf', 20, (150, 330), (0, 255, 0))      
    pygame.display.flip()
    return 

def listenToEvent():
    while True:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()
      
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RETURN:            
                    print("Restarting game.")
                    return 
    return


def isBoardFull(board, empty_space):
    number_of_rows = len(board)
    number_of_columns = len(board[0])
    for i in range(0, number_of_rows):
        for j in range(0, number_of_columns):
            if board[i][j] == empty_space:
                return False
    return True

def initializeGame():
    running =  True
    playerXWin = False
    playerOWin = False
    draw = False    
    board = generateBoard(3)
    turn =  1
    return (running, playerXWin, playerOWin, draw, board, turn)

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
      
def isValidInput(row, column):
  if (row <=  2) and (row >=  0) and (column <=  2) and (column >= 0):
      return True
  else:
      return False            
  
      
def generateBoard(board_size):
    board = [['*' for i in range(1, board_size + 1)] for i in range(1, board_size + 1)]
    return board

def play(position, board ,piece):
    board[position[0]][position[1]] = piece
    return   
  
def getAIMove(board, empty_space, pieceX, pieceO):
    best_score = -800
    best_move = (0, 0)
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == empty_space:
                board[i][j] = pieceX
                score = minimax(board, False, pieceX, pieceO, empty_space)
                board[i][j] = empty_space
                if score > best_score:
                    best_score = score 
                    best_move = (i, j)
    return best_move
  
def getPlayerMove(board, empty_space):
    position = ()
    while True:
        (row, column) = getInputPosition()
        position = (row, column)
        
        
        
        if isValidInput(row, column) ==  False:
            print("Input out of range")
        elif isEmpty(board, position, empty_space) == False:
            print("Block occupied, please play again")
        else:
            break
    return position
  
def maximize(board, pieceX, pieceO,  empty_space):
        best_score = -800 
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if board[i][j] == empty_space:
                    board[i][j] = pieceX
                    score = minimax(board, False, pieceX, pieceO, empty_space) 
                    board[i][j] = empty_space
                    if score > best_score:
                        best_score = score
        return best_score
      
def minimize(board, pieceX, pieceO, empty_space):
        best_score = 800 
        for i in range(0, len(board)):
            for  j in range(0, len(board)):
                if board[i][j] == empty_space:
                    board[i][j] = pieceO
                    score = minimax(board, True, pieceX, pieceO, empty_space)
                    board[i][j] = empty_space
                    if score < best_score:
                        best_score = score 
        return best_score

def minimax(board, isMaximizing, pieceX, pieceO, empty_space):
    if checkWin(board, pieceX):
        return 1  
    if checkWin(board, pieceO):
        return -1  
    if isBoardFull(board, empty_space):
        return 0
    
    if isMaximizing == True:
        return maximize(board, pieceX, pieceO, empty_space)
    else:
        return minimize(board, pieceX, pieceO, empty_space)
    
    return 0


def placePiece(screen, piece, font_type, font_size, color ,position, block_size, off_set):
    font = pygame.font.Font(font_type, font_size)
    X_text = font.render(piece, True ,color)
    textRect = X_text.get_rect()
    textRect.center = (block_size*position[1] + 2*block_size + off_set, block_size*position[0] + 2*block_size + off_set)
    screen.blit(X_text, textRect) 
    return 

def placeText(screen, text, font_type, font_size, position, color):
    font = pygame.font.Font(font_type, font_size)
    title = font.render(text, True ,color)
    textRect = title.get_rect()
    textRect.center = position
    screen.blit(title, textRect)
    return

def drawBoard(screen, board_line_color, block_size):
    pygame.draw.rect(screen, (80, 80, 80), pygame.Rect(0, 0, 6*block_size, 6*block_size), 5)
    pygame.draw.rect(screen, (80, 80, 80), pygame.Rect(2*block_size, 2*block_size, 3*block_size, 3*block_size))
  
    for i in range(2, 5):
        for j in range(2, 5):
            pygame.draw.rect(screen, board_line_color, pygame.Rect(j*60, i*60, block_size, block_size), 2)
    return


def determineCordinates(x, y, block_size):
    x_cor_offset, y_cor_offset = (math.floor(x/block_size), math.floor(y/block_size))
    x_cor, y_cor = (x_cor_offset - 2, y_cor_offset - 2)
    return (x_cor, y_cor)

def drawText(text, font, position, size):
    font = pygame.font.Font(font, size)
    score_text = font.render(text, True ,(255, 255, 255))
    textRect = score_text.get_rect()
    textRect.center = position
    screen.blit(score_text, textRect)
    return


def drawBoardOnScreen(screen,  board_line_color, block_size, background, board, empty_space):
  
    screen.fill(background)
    drawBoard(screen, board_line_color, block_size)
        
    placeText(screen, "Tic-Tac-Toe", 'freesansbold.ttf', 30, (180, 30), (255, 255, 0))
    # placeText(screen, "Score:     X: 0 ,     O: 0", 'freesansbold.ttf', 20, (120, 80), (255, 255, 255))
    # placeText(screen, "Games played: ", 'freesansbold.ttf', 20, (90, 105), (0, 255, 0))
  
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            piece = board[i][j]
            if piece == empty_space:
              piece = ""
            position = (i, j)
            off_set = block_size/2
            
            placePiece(screen, piece, 'freesansbold.ttf', 40, (255, 255, 255) ,position, block_size, off_set)
    return

def getPlayerInputFromBoard(pygame, block_size):
    played = False
    position = ()
    while played == False:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                xc, yc = determineCordinates(x, y, block_size)
                position = (yc, xc) 
                played = True
                break
    return position


if __name__ == "__main__":
    main()