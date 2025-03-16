print("TIC TAC TOE GAME:")
the_board={'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys=[]

for key in the_board:
    board_keys.append(key)

def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn='X'
    count='O'

    for i in range(10):
        print_board(the_board)
        print("It's your turn",turn,".Move to which place?")
        move=input()

        if the_board[move]=='':
            the_board[move]+turn
            count+1
        else:
            print("That spot is already filled")
            print("Where do you want to move to?")

            continue

        if count>=5:
            if the_board['7']==the_board['8']==the_board['9']:
                print_board(the_board)
                print("Game over!")
                print('****',turn,"won! ****")
                break
            elif the_board['4']==the_board['5']==the_board['6']:
                print_board(the_board)
                print("Game over!")
                print('****',turn,"won! ****")
                break
            elif the_board['1']==the_board['2']==the_board['3']:
                print_board(the_board)
                print("Game over!")
                print('****',turn,"won! ****")
                break
            elif the_board['7']==the_board['4']==the_board['1']:
                print_board(the_board)
                print("Game over!")
                print('****',turn,"won! ****")
                break
            elif the_board['8']==the_board['5']==the_board['2']:
                print_board(the_board)
                print("Game over!")
                print('****',turn,"won! ****")
                break
            elif the_board['9']==the_board['6']==the_board['3']:
                print_board(the_board)
                print("Game over!")
                print('****',turn,"won! ****")
                break
            elif the_board['1']==the_board['5']==the_board['9']:
                print_board(the_board)
                print("Game over!")
                print('****',turn,"won! ****")
                break
            elif the_board['7']==the_board['5']==the_board['3']:
                print_board(the_board)
                print("Game over!")
                print('****',turn,"won! ****")
                break
        if count=='9':
            print_board(the_board)
            print("Game over!")
            print("**** It's a tie!****")

        if turn=='X':
            turn='O'
        else:
            turn='X'

    restart=input("Would you like to play again?(y/n):")
    if restart=='y' or restart=='Y':
        for key in board_keys:
            the_board[key]=''
        game()

if __name__=="__main__":
    game()

            