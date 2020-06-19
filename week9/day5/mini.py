import random


class Game:
    results = []


    def user_move(self):
        move = input("choose your move ('r' for rock, 'p' for paper, 's' for scissors) ").lower()
        while move not in ['r', 'p', 's']:
            move = input("unaccepted move. Pick again ('r' for rock, 'p' for paper, 's' for scissors) ").lower()
        return move


    def computer_move(self):
        move = random.choice(['r','p','s'])
        return move


    def get_game_result(self, user, computer):
        computer_move = ['r', 'p', 's']
        index = 0
        for play in computer_move:
            if computer == play:
                if user == play:
                    return 'tie'
                elif user == computer_move[index - 1]:
                    return 'lose'
                else:
                    return 'win'
            index += 1

    def track_results(self, result):
        self.results.append(result)
        return self.results


def play():
    user_play = my_game.user_move()
    computer_play = my_game.computer_move()
    result = my_game.get_game_result(user_play, computer_play)
    print(f'you played {user_play} and the computer played {computer_play}. You {result}')
    return result


def print_results():
    win_nb = my_game.results.count('win')
    lose_nb = my_game.results.count('lose')
    tie_nb = my_game.results.count('tie')
    print(f'Fun playing, you won {win_nb} games, lost {lose_nb} games, and tied {tie_nb} games')


def main():
    will_play = input("Do you want to play? (yes or no) ").strip(' ')
    while will_play not in ['yes', 'no']:
        will_play = input("Do you want to play? (yes or no) ")     # how can you make loop cleaner? hint:
    while will_play == 'yes':                                      # set will play to true
        result = play()                                            # make want_to_play function?
        my_game.track_results(result)
        will_play = input("Do you want to play? (yes or no) ").strip(' ')
        while will_play not in ['yes', 'no']:
            will_play = input("Do you want to play? (yes or no) ")
    print_results()


my_game = Game()
main()


















