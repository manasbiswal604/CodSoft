import tkinter as tk
import random
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=' ', font=('normal', 40), height=2, width=5,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)
        
        self.root.mainloop()

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col]['text'] = self.current_player
            self.buttons[row][col]['state'] = 'disabled'
        
            if self.check_winner(self.current_player):
                if self.current_player == 'X':
                    messagebox.showinfo("Game Over", "You win!")
                else:
                    messagebox.showinfo("Game Over", "Bot wins!")
                self.reset_game()
            elif self.is_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'X' if self.current_player == 'O' else 'O'
                if self.current_player == 'O':
                    self.make_bot_move()

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j]['text'] = ' '
                self.buttons[i][j]['state'] = 'active'
        self.current_player = 'X'

    def check_winner(self, player):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all([self.board[i][j] == player for j in range(3)]) or \
               all([self.board[j][i] == player for j in range(3)]):
                return True
        
        if all([self.board[i][i] == player for i in range(3)]) or \
           all([self.board[i][2 - i] == player for i in range(3)]):
            return True
        
        return False

    def is_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def make_bot_move(self):
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
        if available_moves:
            row, col = random.choice(available_moves)
            self.make_move(row, col)

if __name__ == "__main__":
    app = TicTacToe()
