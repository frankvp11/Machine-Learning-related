import random
import time


class Board():
    def __init__(self):
        self.board = [0, 0, 0,
                      0, 0, 0,
                      0, 0, 0]
        self.game_over = False
        
    # randomly places
    def place(self, choices):
        return random.choice(choices)
    
    def check_winner(self):
        if self.board[0] == self.board[1] == self.board[2] != 0: 
            self.winner = self.board[0]
            print(self.winner)
            print("Top")
            self.game_over = True
        elif self.board[3] == self.board[4] == self.board[5] != 0:
            self.winner = self.board[3]
            print(self.winner)
            print("mid")
            self.game_over = True

        elif self.board[6] == self.board[7] == self.board[8] != 0:
            self.winner = self.board[6]
            print(self.winner)
            print("bottom")
            self.game_over = True

        elif self.board[0] == self.board[4] == self.board[8] != 0:
            self.winner = self.board[0]
            print(self.winner)
            print("diagonal")
            self.game_over = True

        elif self.board[2] == self.board[4] == self.board[6] != 0:
            self.winner = self.board[2]
            print(self.winner)
            print("diagonal")
            self.game_over = True
        
        elif self.board[0] == self.board[3] == self.board[6] != 0:
            self.winner = self.board[0]
            print(self.winner)
            print("column 1")
            self.game_over = True
        elif self.board[1] == self.board[4] == self.board[7] != 0:
            self.winner = self.board[1]
            print(self.winner)
            print("column 2")
            self.game_over = True
        
        elif self.board[2] == self.board[5] == self.board[8] != 0:
            self.winner = self.board[2]
            print(self.winner)
            print("Col 3")
            self.game_over = True

        if self.check_tie():
            self.game_over = True
            print("Tie")

        
    def check_tie(self):
        for i in range(len(self.board)):
            if self.board[i] == 0:
                return False
        return True


    def get_choices(self, state):
        choices = []
        for i in range(len(state)):
            if state[i] == 0:
                choices.append(i)
        return choices

    
    def move(self, position, player):
        self.board[position] = player


def print_board(state):
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])

if __name__ == "__main__":
    for i in range(5):
        game = Board()
        board = game.board
        current_player = 0
        while not game.game_over:
            current_player += 1
            
            
            place = game.place(game.get_choices(game.board))
            if current_player % 2 != 0:
                game.move(place, 1)
            else:
                game.move(place, 2)
            game.check_winner()    

        
        
