from TicTacToelogic import *


game_on = True

original = ['0','1','2','3','4','5','6','7','8']
counter = 0
print("Welcome to TIC TAC TOE")
while game_on:
    #clears anything on screen and shows the board layout
    #clear_output()
    board_layout(original)
    # tells user to choose X or Y
    #user_select()
    # tells user you have to pick a number on the keyboard
    #user_choice()
    #replaces board with x or y
    user_replace(original,user_choice())
    board_layout(original)
    print('\n'*100)
    #clear_output()
    COUNTER = 0
    #board_layout(original)
    #THIS IS THE LOGIC FOR ACCROSS ROW 1
    if (original[0] == 'X') and (original[1] == 'X') and (original[2] == 'X'):
        print("player X has won")
        break
        game_on = False
    elif (original[0] == 'Y') and (original[1] == 'Y') and (original[2] == 'Y'):
        print("player Y has won")
        break
        game_on = False
    elif (original[3] == 'Y') and (original[4] == 'Y') and (original[5] == 'Y'):
        print("player Y has won")
        break
        game_on = False
    elif (original[3] == 'X') and (original[4] == 'X') and (original[5] == 'X'):
        print("player X has won")
        break
        game_on = False
    elif (original[6] == 'Y') and (original[7] == 'Y') and (original[8] == 'Y'):
        print("player Y has won")
        break
        game_on = False
    elif (original[6] == 'X') and (original[7] == 'X') and (original[8] == 'X'):
        print("player X has won")
        break
        game_on = False
    elif (original[0] == 'Y') and (original[3] == 'Y') and (original[6] == 'Y'):
        print("player Y has won")
        break
        game_on = False
    elif (original[0] == 'X') and (original[3] == 'X') and (original[6] == 'X'):
        print("player X has won")
        break
        game_on = False
    elif (original[1] == 'Y') and (original[4] == 'Y') and (original[7] == 'Y'):
        print("player Y has won")
        break
        game_on = False
    elif (original[1] == 'X') and (original[4] == 'X') and (original[7] == 'X'):
        print("player X has won")
        break
        game_on = False
    elif (original[2] == 'Y') and (original[5] == 'Y') and (original[8] == 'Y'):
        print("player Y has won")
        break
        game_on = False
    elif (original[2] == 'X') and (original[5] == 'X') and (original[8] == 'X'):
        print("player X has won")
        break
        game_on = False
    elif (original[0] == 'Y') and (original[4] == 'Y') and (original[8] == 'Y'):
        print("player Y has won")
        break
        game_on = False
    elif (original[0] == 'X') and (original[4] == 'X') and (original[8] == 'X'):
        print("player Y has won")
        break
        game_on = False
    elif (original[2] == 'Y') and (original[4] == 'Y') and (original[6] == 'Y'):
        print("player Y has won")
        break
        game_on = False
    elif (original[2] == 'X') and (original[4] == 'X') and (original[6] == 'X'):
        print("player Y has won")
        break
        game_on = False
    #LOGIC FOR IF THERE ARE NO WINNERS BOARD RESETS 
    counter += 1
    if counter % 9 == 0:
        print("No one has been Board is being reset")
        original = ['0','1','2','3','4','5','6','7','8']
game_con()
