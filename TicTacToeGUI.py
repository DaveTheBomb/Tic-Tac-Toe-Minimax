import pygame
from pygame.locals import *
import math

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
    
def main():
  
    pygame.init()
    clock = pygame.time.Clock()
    block_size = 60
    off_set = block_size/2
    board_line_color = (20, 108, 164)
    screen = pygame.display.set_mode((60*6, 60*6))
    background = (4, 124, 140)
    time_passed = clock.tick(60) / 1000
  
    while True:
        for event in pygame.event.get():
          if event.type == QUIT: 
            pygame.quit()
            exit()
  
          if event.type == KEYDOWN:
            x, y = pygame.mouse.get_pos()
            xc, yc = determineCordinates(x, y, block_size)
            ## for debugging
            print(yc, xc) 
            
        screen.fill(background)
        drawBoard(screen, board_line_color, block_size) 
        
        placeText(screen, "Tic-Tac-Toe", 'freesansbold.ttf', 30, (180, 30), (255, 255, 0))
        placeText(screen, "Score:     X: 0 ,     O: 0", 'freesansbold.ttf', 20, (120, 80), (255, 255, 255))
        placeText(screen, "Games played: ", 'freesansbold.ttf', 20, (90, 105), (0, 255, 0))
        
        position = (1,0)
        piece = 'X'
        placePiece(screen , piece, 'freesansbold.ttf', 40, (255, 255, 255) ,position, block_size, off_set)
      
        position = (1,1)
        piece = 'O'
        placePiece(screen, piece, 'freesansbold.ttf', 40, (255, 255, 255) ,position, block_size, off_set)
        
        pygame.display.flip()
  

  
    return 
      





if __name__ == "__main__":
    main()