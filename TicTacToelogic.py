def board_layout(board):
    print(board[0] + '|'+ board[1]+ '|' + board[2])
    print('----')
    print(board[3] + '|'+ board[4]+ '|' + board[5])
    print('----')
    print(board[6] + '|'+ board[7]+ '|' + board[8])

original = ['0','1','2','3','4','5','6','7','8']

def user_select():
    dave = True 
    while dave:
        screen = input("please choose if you want to be X or Y: ").upper()
        selectors = ['X','Y']
        if screen not in selectors:
            print(" you have not selected X or Y please select them")
        if screen in selectors:
            #clear_output()
            break
    return screen

def user_choice():
    mike = True
    # user selects a number between (1-9)
    num_list = [0,1,2,3,4,5,6,7,8,9]
    while mike:
        choice = int(input("please select a number on the keyboard: "))
        if choice not in num_list:
            print("you didnt select a number in the keyboard please try again")
        if choice in num_list:
            mike = False
        
    
    return choice

def user_replace(original,position):
    user_rep = input("X or Y: ").upper()
    original[position] = user_rep
    #if position == 8
         
    return original
def game_con():
    
    john =True
    choices = ['Y','N']
    while john:
        user = input("Do you want to continue Y or N: ").upper()
        if user == 'N' or user =='n':
            print("thank you for playing !!!")
            break
            #clear_output()
        else:
            break
            john = False
    #clear_output()
    return user 
#clear_output()
