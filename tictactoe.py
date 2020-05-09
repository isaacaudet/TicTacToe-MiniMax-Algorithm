import string
import random
import math


class TicTacToe:
    board = {(1, 3): '', (2, 3): '', (3, 3): '',
             (1, 2): '', (2, 2): '', (3, 2): '',
             (1, 1): '', (2, 1): '', (3, 1): ''
             }

    def __init__(self):
        self.run, self.user, self.ai = input().split()
        if self.user == 'user':
            self.user_piece = 'X'
            self.ai_piece = 'O'
            self.turn = self.user
        elif self.user != 'user':
            self.ai = self.user
            self.user = 'user'
            self.user_piece = 'O'
            self.ai_piece = 'X'
            self.turn = self.ai
        self.user_move = tuple()
        self.moves = [i for i in self.board.keys()]
        self.ai_move = tuple()
        self.wins = ''
        self.ai_win = ''
        self.ai_block = ''
        self.score = int

    def ai_easy(self):
        print('Making move level "easy"')
        random_move = random.choice(self.moves)
        self.moves.remove(random_move)
        self.board[random_move] = self.ai_piece

    def print_winner(self):
        if self.wins is not '':
            print(self.wins + ' wins')

    def game_state(self, board):
        # check all 8 winning positions
        self.score = 0
        if board[(1, 3)] != '':
            if board[(1, 3)] == board[(2, 3)] == board[(3, 3)]:
                self.wins = board[(1, 3)]
                if self.wins == self.ai_piece:
                    self.score = 10
                else:
                    self.score = -10
                self.run = 'stop'
        if board[(1, 2)] != '':
            if board[(1, 2)] == board[(2, 2)] == board[(3, 2)]:
                self.wins = board[(1, 2)]
                if self.wins == self.ai_piece:
                    self.score = 10
                else:
                    self.score = -10
                self.run = 'stop'
        if board[(1, 1)] != '':
            if board[(1, 1)] == board[(2, 1)] == board[(3, 1)]:
                self.wins = board[(1, 1)]
                if self.wins == self.ai_piece:
                    self.score = 10
                else:
                    self.score = -10
                self.run = 'stop'
        if board[(1, 3)] != '':
            if board[(1, 3)] == board[(1, 2)] == board[(1, 1)]:
                self.wins = board[(1, 3)]
                if self.wins == self.ai_piece:
                    self.score = 10
                else:
                    self.score = -10
                self.run = 'stop'
        if board[(2, 3)] != '':
            if board[(2, 3)] == board[(2, 2)] == board[(2, 1)]:
                self.wins = board[(2, 3)]
                if self.wins == self.ai_piece:
                    self.score = 10
                else:
                    self.score = -10
                self.run = 'stop'
        if board[(3, 3)] != '':
            if board[(3, 3)] == board[(3, 2)] == board[(3, 1)]:
                self.wins = board[(3, 3)]
                if self.wins == self.ai_piece:
                    self.score = 10
                else:
                    self.score = -10
                self.run = 'stop'
        if board[(1, 3)] != '':
            if board[(1, 3)] == board[(2, 2)] == board[(3, 1)]:
                self.wins = board[(1, 3)]
                if self.wins == self.ai_piece:
                    self.score = 10
                else:
                    self.score = -10
                self.run = 'stop'
        if board[(1, 1)] != '':
            if board[(1, 1)] == board[(2, 2)] == board[(3, 3)]:
                self.wins = board[(1, 1)]
                if self.wins == self.ai_piece:
                    self.score = 10
                else:
                    self.score = -10
                self.run = 'stop'

        if '' not in board.values():
            if self.wins == '':
                # print("Draw")
                self.score = 0
                self.run = 'stop'

    def print_board(self, empty=False):
        print('---------')
        if empty:
            for i in range(3):
                print('|       |')
        else:
            for k, v in self.board.items():
                if k in ((1, 3), (1, 2), (1, 1)):
                    print('| ', end='')
                if v is not '':
                    print(v + ' ', end='')
                else:
                    print('  ', end='')
                if k in ((3, 3), (3, 2), (3, 1)):
                    print('|')
        print('---------')

    # noinspection PyTypeChecker
    def next_move(self):
        while True:
            if self.user_move in self.board.keys():
                if self.board[self.user_move] == '':
                    self.board[self.user_move] = self.user_piece
                    self.moves.remove(self.user_move)
                    break
                if self.board[self.user_move] in ('X', 'O'):
                    print("This cell is occupied! Choose another one!")
                    self.user_input()
            else:
                print("Coordinates should be from 1 to 3!")
                self.user_input()

    def user_input(self):
        try:
            self.user_move = tuple(map(int, input('Enter the coordinates: ').split()))
        except ValueError:
            self.run = False
            print('Bad parameters')

    def winning_move(self):
        for i in self.moves:
            self.board[i] = self.ai_piece
            self.game_state(self.board)
            self.run = 'start'
            if self.wins is self.ai_piece:
                self.ai_win = i
                self.board[i] = ''
                self.ai_block = ''
                break
            self.board[i] = self.user_piece
            self.game_state(self.board)
            self.run = 'start'
            if self.wins is self.user_piece:
                self.ai_block = i
                self.board[i] = ''
                self.ai_win = ''
                break
            self.board[i] = ''

    # noinspection PyTypeChecker
    def ai_medium(self):
        print('Making move level "medium"')
        if self.ai_win is not '':
            self.moves.remove(self.ai_win)
            self.board[self.ai_win] = self.ai_piece
            self.ai_win = ''
            return
        elif self.ai_block is not '':
            self.moves.remove(self.ai_block)
            self.board[self.ai_block] = self.ai_piece
            self.wins = ''
        else:
            random_move = random.choice(self.moves)
            self.moves.remove(random_move)
            self.board[random_move] = self.ai_piece

    def minimax(self, board, depth, player):
        if player == self.ai:
            best = [tuple(), -1000]
        else:
            best = [tuple(), 1000]

        self.game_state(board)

        if depth == 0 or self.wins != '':
            score = self.score
            self.wins = ''
            self.run = 'start'
            return [tuple(), score]

        for i in [k for k, v in board.items() if v == '']:
            move = i
            board[move] = self.ai_piece if player == self.ai else self.user_piece
            if player == self.ai:
                self.turn = self.user
            else:
                self.turn = self.ai
            score = self.minimax(board, depth - 1, self.turn)
            board[move] = ''
            score[0] = move

            if player == self.ai:
                if score[1] > best[1]:
                    best = score
            else:
                if score[1] < best[1]:
                    best = score
        return best

    def ai_hard(self):
        depth = len(self.moves)
        if depth == 0 or self.wins != '':
            return

        if depth == 9:
            print('Making move level "hard"')
            random_move = random.choice(self.moves)
            self.moves.remove(random_move)
            self.board[random_move] = self.ai_piece
        else:
            self.turn = self.ai
            move = self.minimax(self.board, depth, self.turn)
            print('Making move level "hard"')
            self.ai_move = move[0]
            self.moves.remove(self.ai_move)
            self.board[self.ai_move] = self.ai_piece


if __name__ == '__main__':
    game = TicTacToe()
    game.print_board(empty=True)

    if game.ai_piece == 'X':
        if game.ai == 'easy':
            game.ai_easy()
            game.print_board()
        if game.ai == 'medium':
            game.winning_move()
            game.ai_medium()
            game.print_board()
        if game.ai == 'hard':
            game.ai_hard()
            game.print_board()
    while True:
        game.user_input()
        if not game.run:
            break
        game.next_move()

        if game.run == 'stop':
            break

        game.print_board()
        game.game_state(game.board)
        game.print_winner()

        if game.run == 'stop':
            break

        if game.ai == 'easy':
            game.ai_easy()
        if game.ai == 'medium':
            game.winning_move()
            game.ai_medium()

        if game.ai == 'hard':
            game.ai_hard()

        game.print_board()
        game.game_state(game.board)
        game.print_winner()

        if game.run == 'stop':
            break
