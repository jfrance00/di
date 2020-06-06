board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

def display_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

taken_spaces = []

def check_win(player):
    winning_combos = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['1', '4', '7'], ['2', '5', '8'],
                      ['3', '6', '9'], ['1', '5', '9'], ['3', '5', '7']]
    for spaces in winning_combos:
        if all(elem in player for elem in spaces):
            return True

def player_input(player):
    move = input("Chose a spot: ")
    if (check_move(player, move) == True):
        player.append(move)
    return player


def check_move(player, move):
    accepted_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']   #'0' added to exit while loop in main function, take out later
    if (move in accepted_moves):
        if (move in taken_spaces):
            print("move taken, choose another space")
            player_input(player)                           #is it a problem to call a function that is called within that function?
        else:
            taken_spaces.append(move)
            return True
    else:
        print("invalid input")
        player_input(player)

def update_board(player, player_symbol):
    move =  player[-1]
    board[move] = player_symbol


def play():
    display_board(board)  # works
    turns = 0
    player_x = []
    player_o = []
    while turns < 9:
        if (turns % 2 == 0):
            player_input(player_x)
            update_board(player_x, 'x')
            display_board(board)
            if (check_win(player_x) == True):
                print("Player x wins!")
                return
        else:
            player_input(player_o)
            update_board(player_o, 'o')
            display_board(board)
            if (check_win(player_o) == True):
                print("Player o wins!")
                return
        turns += 1
    print("board full, tie game!")

play()
