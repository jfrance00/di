class Game:

    def display(self):
        board_view = '''
             A B C D E F G H
        1   |_|_|_|_|_|_|_|_|
        2   |_|_|_|_|_|_|_|_|
        3   |_|_|_|_|_|_|_|_|
        4   |_|_|_|_|_|_|_|_|
        5   |_|_|_|_|_|_|_|_|
        6   |_|_|_|_|_|_|_|_|
        7   |_|_|_|_|_|_|_|_|
        8   |_|_|_|_|_|_|_|_|
        '''
        return board_view

    def board(self):
        col = 1
        row = []
        for index in range(8):
            row.append(col)
            col += 1

        board = [row] * 8
        return board


class Piece:

    def __init__(self, color):
        pass

    def populate_board(self):
        board_list = my_game.board()
        print(board_list)
        for ix, row in enumerate(board_list[: 3]):
            for num in range(4):
                checker = Piece('red')

    def move(self):
        pass

    def take_piece(self):
        pass

    def check_move(self):
        pass


class King(Piece):

    def check_move(self):
        play = "play"
        pass


my_game = Game()
# my_pieces = Piece('red')
# my_pieces.populate_board()


def main():
    colors = {"player1" : "black", "player2" : "red"}
    for player, color in colors:
        if check_play():
            player = Piece(color)




def check_play():
    will_play = False
    while not will_play:
        response = input("play? ").lower()
        if response == "yes":
            print("playing")
            return True
        elif response == "no":
            print("Okay, you don't want to play")
            return False


print(my_game.board())
#  Tic Tac Toe Example of board
#
# the_board = {'7': ' ', '8': ' ', '9': ' ',
#                 '4': ' ', '5': ' ', '6': ' ',
#                 '1': ' ', '2': ' ', '3': ' '}
#
# def display_board(board):
#     print(board['7'] + '|' + board['8'] + '|' + board['9'])
#     print('-+-+-')
#     print(board['4'] + '|' + board['5'] + '|' + board['6'])
#     print('-+-+-')
#     print(board['1'] + '|' + board['2'] + '|' + board['3'])






