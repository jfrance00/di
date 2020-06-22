class Game:

    def __init__(self):
        self.game_tiles = (u"\u25FC", u'\u25FB')

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
        alpha = 'A'
        row = []
        for index in range(8):
            row.append(alpha)
            alpha = chr(ord(alpha) + 1)

        board = [row] * 8
        #board[row][column]
        return board


class Piece:

    def __init__(self):
        # self.game_tiles = (u"\u25FC", u'\u25FB')
        # self.pawn = (u"\u2659", u'\u265F')
        # self.queen = (u'\u2655', u'\u265B')

    def move(self):
        pass

    def take_piece(self):
        pass

    def check_move(self):
        pass
            for row in board[: 1]: # <- will iterate over first two lists in board -> python limit lists
                for num in range(8):
                    #create objects
class King(Piece):

    def check_move(self):
        pass


my_game = Game()

