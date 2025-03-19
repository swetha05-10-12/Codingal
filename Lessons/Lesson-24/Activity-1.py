print("TIC TAC TOE GAME:")
the_board = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in the_board:
    board_keys.append(key)

def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(9):
        print_board(the_board)
        print("It's your turn", turn, ". Move to which place?")
        move = input()

        if move not in the_board or the_board[move] != ' ':
            print("That spot is already filled or invalid. Try again.")
            continue

        the_board[move] = turn
        count += 1

        if count >= 5:
            if (the_board['7'] == the_board['8'] == the_board['9'] != ' ') or \
               (the_board['4'] == the_board['5'] == the_board['6'] != ' ') or \
               (the_board['1'] == the_board['2'] == the_board['3'] != ' ') or \
               (the_board['7'] == the_board['4'] == the_board['1'] != ' ') or \
               (the_board['8'] == the_board['5'] == the_board['2'] != ' ') or \
               (the_board['9'] == the_board['6'] == the_board['3'] != ' ') or \
               (the_board['1'] == the_board['5'] == the_board['9'] != ' ') or \
               (the_board['7'] == the_board['5'] == the_board['3'] != ' '):
                print_board(the_board)
                print("Game over!")
                print('****', turn, "won! ****")
                break

        if count == 9:
            print_board(the_board)
            print("Game over!")
            print("**** It's a tie! ****")
            break

        turn = 'O' if turn == 'X' else 'X'

    restart = input("Would you like to play again? (y/n): ")
    if restart.lower() == 'y':
        for key in board_keys:
            the_board[key] = ' '
        game()

if __name__ == "__main__":
    game()