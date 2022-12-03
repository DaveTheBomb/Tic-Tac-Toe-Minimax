import pygame
from pygame.locals import *
import math
from MiniMaxImplemented import MinimaxAlgorithm

class TicTacToeGUII:

    def __init__(self, screen_size, background_color, out_border_color, grid_line_color,grid_block_size, piece_color, piece_font ):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.block_size =  grid_block_size

        self.background_color = background_color
        self.outer_border_color  = out_border_color

        self.grid_line_color = grid_line_color

        self.piece_color = piece_color
        self.piece_font = piece_font
        self.text_collection = []

        self.cursor_grid_position = None
        self.cursor_grid_position_r_c = None

        self.game_running = True
        self.played = False


        return

    def render(self, board):
        self.drawBackground()
        self.drawGameGrid()
        self.drawAllText()
        self.drawPieces(board)

        pygame.display.flip()
        return

    def update(self, game_engine):
        self.drawPieces(game_engine.getBoard())
        pass

    def drawBackground(self):
        pygame.draw.rect(self.screen, self.background_color, pygame.Rect(0, 0, 6*self.block_size, 6*self.block_size))
        pygame.draw.rect(self.screen, self.outer_border_color, pygame.Rect(0, 0, 6*self.block_size, 6*self.block_size), 5)
        return

    def drawGameGrid(self):
        for i in range(2, 5):
            for j in range(2, 5):
                pygame.draw.rect(self.screen, self.grid_line_color, pygame.Rect(j*60, i*60, self.block_size, self.block_size), 2)
        return
        
    def addText(self, text_string, font, font_size, position, color):
        self.text_collection.append([text_string, font, font_size, position, color]) 
        return

    def placeText(self, text, font_type, font_size, position, color):
        font = pygame.font.Font(font_type, font_size)
        title = font.render(text, False ,color)
        self.screen.blit(title, position)
        return

    def drawAllText(self):
        for text in self.text_collection:
           self.placeText(text[0], text[1], text[2], text[3], text[4])
        return

    def drawPieces(self, board):
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                position = (j, i)
                piece = ' '
                if board[i][j] == '*':
                    piece = ' ' 
                else:
                    piece = board[i][j]
                self.placePiece(piece, position)    
        return

    def resetGame(self):
        self.text_collection = []
        return

    def placePiece(self, piece, position):
        off_set_1 = self.block_size/4 
        off_set_2 = self.block_size/4 
        font_size = self.block_size - 20
        font = pygame.font.Font(self.piece_font, font_size)
        X_text = font.render(piece, True ,self.piece_color)
        pixel_position = (self.block_size*position[0] + 2*self.block_size + off_set_1, self.block_size*position[1] + 2*self.block_size  + off_set_2)
        self.screen.blit(X_text, pixel_position) 

        return 

    def handleEvent(self, game_engine):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_RETURN) and (self.game_running == False) :
                    game_engine.resetBoard()
                    self.game_running =  True
                    # Clear all text except for title
                    self.text_collection = []

            if (event.type == pygame.MOUSEBUTTONUP) and (self.played == False):
                if game_engine.current_playing_piece == game_engine.player_1_piece:
                
                    self.cursor_grid_position = self.getCursorCordinates()
                    self.cursor_grid_position_r_c = (self.cursor_grid_position[1], self.cursor_grid_position[0])
                    
                    # changing turns if the move is valid and position is not occuiped
                    if game_engine.isValidMove(self.cursor_grid_position_r_c) ==  True:
                        if game_engine.isEmpty(self.cursor_grid_position_r_c) ==  True:
                            game_engine.play(self.cursor_grid_position_r_c)
                            self.played = True

            if(self.played == True) and (game_engine.current_playing_piece == game_engine.player_2_piece):
                algorithm = MinimaxAlgorithm(game_engine.player_2_piece, game_engine.player_1_piece, game_engine.empty_space)
                AI_best_move = game_engine.getAIPlayPosition(algorithm, game_engine.player_2_piece)
                game_engine.play(AI_best_move)
                self.played = False

        return

    def getCursorCordinates(self):
        x, y = pygame.mouse.get_pos()
        x_cor_offset, y_cor_offset = (math.floor(x/self.block_size), math.floor(y/self.block_size))
        x_cor, y_cor = (x_cor_offset - 2, y_cor_offset - 2)
        return (x_cor, y_cor)

