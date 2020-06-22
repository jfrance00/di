#Tic Tac Toe

# create board
# collect and record user input
    #don't allow repeat user input
# Compare user input to winning permutations
# if board full declare game a tie

the_board = {'7': ' ', '8': ' ', '9': ' ',
                '4': ' ', '5': ' ', '6': ' ',
                '1': ' ', '2': ' ', '3': ' '}

def display_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


taken_spaces = []


def player_input(player):
    turn = input("your move")
    if (check_move(turn, taken_spaces)):
        player.append(turn)
        track_spaces(turn)
        print(player)
        return player
    else:
        player_input(player)

def track_spaces(move):
    global taken_spaces
    taken_spaces.append(move)


def check_move(move, taken_spaces):
    print("Moves taken: {}".format(taken_spaces))
    if (move in taken_spaces):
        print("move taken, choose another space")
        return False
    else:
        return True

def check_win(player):
    print("checking if someone won")
    winning_combos = [['7','8','9'], ['4','5','6'], ['1','2','3'], ['1','4','7'], ['2','5','8'], ['3','6','9'], ['1','5','9'], ['2','5','7']]
    for spaces in winning_combos:
        if (all(elem in player for elem in spaces)):
            return Trues

def play():
    display_board(the_board)
    turns = 0
    x = []
    o = []
    while turns < 9:
        if (turns % 2 == 0):
            print("player x turn: {}".format(turns))
            x = player_input(x)
        else:
            print("player o turn: {}".format(turns))
            o = player_input(o)
        if (turns > 4):
            if (check_win(0)):
                print("player won!")
        turns += 1
    print("Board full, tie game!")

play()