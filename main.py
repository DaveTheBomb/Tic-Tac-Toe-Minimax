"""
    Author: Siphamandla Malaza
    Date:   02 December 2022
"""
from OOPTicTacToeGUI import TicTacToeGUII

from GameEngine import *


def main():

    block_size = 60
    board_line_color = (20, 108, 164)
    screen_size = (60*6, 60*6)
    background_color = (4, 124, 140)
    grid_line_color = (255, 255, 255)
    piece_color = (255, 255, 255)
    piece_font =  'freesansbold.ttf'

    GameGUI = TicTacToeGUII(screen_size, background_color, board_line_color, grid_line_color, block_size,  piece_color, piece_font) 

    Game_Engine = GameEngine()
    Game_Engine.initilizeBoard()
    computer_turn = True

    introductory_text_setting = {"text" :"Tic-Tac-Toe", "font":'freesansbold.ttf', "size": 30, "position": (130, 30), "color": (255, 255, 0)}
    win_status_text = {"text" :"", "font":'freesansbold.ttf', "size": 20, "position": (130, 70), "color": (0, 255, 0)} 
    play_again_text = {"text" :"Press Enter to play again", "font":'freesansbold.ttf', "size": 20, "position": (70, 330), "color": (255, 100, 0)} 
    

    while True:
        GameGUI.handleEvent(Game_Engine)

        if GameGUI.game_running == True:

            if Game_Engine.isWinning(Game_Engine.player_1_piece) or Game_Engine.isWinning(Game_Engine.player_2_piece) or Game_Engine.isBoardFull():
                play_again_text["text"]  = "Press Enter to play again"
                GameGUI.text_collection = []
                GameGUI.game_running = False
                
                if Game_Engine.isWinning(Game_Engine.player_1_piece):       
                    win_status_text["text"] = "Player 1 Won!"
                elif Game_Engine.isWinning(Game_Engine.player_2_piece) ==  True:
                    win_status_text["text"] = "Player 2 Won!"
                elif Game_Engine.isBoardFull() ==  True:
                    win_status_text["text"] = "Draw!"
            else:
                win_status_text["text"] = ""
                play_again_text["text"] = ""

            GameGUI.addText(introductory_text_setting['text'], introductory_text_setting['font'], introductory_text_setting['size'], introductory_text_setting['position'], introductory_text_setting['color'])                
            GameGUI.addText(win_status_text['text'], win_status_text['font'], win_status_text['size'], win_status_text['position'], win_status_text['color'])
            GameGUI.addText(play_again_text['text'], play_again_text['font'], play_again_text['size'], play_again_text['position'], play_again_text['color'])

            try:        
                GameGUI.update(Game_Engine)
            except:
                pass
            finally:
                GameGUI.render(Game_Engine.getBoard())

if __name__== "__main__":
    main()