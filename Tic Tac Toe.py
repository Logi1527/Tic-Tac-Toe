import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.create_home_page()


    def create_home_page(self):
        self.clear_window()

        self.bg_image = Image.open("d:\My work\image")  
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        
        self.canvas = tk.Canvas(self.root, width=self.bg_image.width(), height=self.bg_image.height())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        self.label = tk.Label(self.root, text="Welcome to Tic Tac Toe", font=("Helvetica", 16), bg='lightblue')
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game, font=("Helvetica", 14))


        self.canvas.create_window(self.bg_image.width() // 2, self.bg_image.height() // 3, window=self.label)
        self.canvas.create_window(self.bg_image.width() // 2, self.bg_image.height() // 2, window=self.start_button)

    def start_game(self):
        self.clear_window()
        self.create_game_board()

    def create_game_board(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.root, text=' ', font=('Helvetica', 20), height=3, width=6,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.show_winner()
            elif ' ' not in self.board:
                self.show_draw()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return False

    def show_winner(self):
        winner = self.current_player
        messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
        self.create_thank_you_page()

    def show_draw(self):
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        self.create_thank_you_page()

    def create_thank_you_page(self):
        self.clear_window()

        
        label = tk.Label(self.root, text="Thank You for Playing!", font=("Helvetica", 16))
        label.pack(pady=20)

        
        restart_button = tk.Button(self.root, text="Play Again", command=self.create_home_page, font=("Helvetica",16))

        
        restart_button.pack(pady=20)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()