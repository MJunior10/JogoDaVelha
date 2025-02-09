import tkinter as tk
from itertools import cycle
from typing import NamedTuple
from tkinter import font


class Player(NamedTuple): #cria a class Player contendo label posteriormente difinida com (O ou X) e a cor posteriormente definida
    label: str
    color: str

class Move(NamedTuple): #cria o metodo Move que recebe parametros de onde o movimento foi realizado
    row: int
    col: int
    label: str = ""

BOARD_SIZE = 3 #define o tamanho do tabuleiro

DEFAULT_PLAYERS = ( #Define os players e as cores de cada um
    Player(label="X", color="red"),
    Player(label="O", color="blue"),
)


class TicTacToeGame:
    def __init__(self, players=DEFAULT_PLAYERS, board_size = BOARD_SIZE):
        self._players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()

    def _setup_board(self):
        self._current_moves = [
            [Move(row,col) for col in range(self.board_size)] for row in range(self.board_size)
        ]
        self._winning_combos = self._get_winning_combos()

    def _get_winning_combos(self):

        ## Obtem as configurações para vencer o jogo, sendo eles linhas, colunas e as diagonais

        rows = [
            [(move.row, move.col) for move in row] for row in self._current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns +[first_diagonal, second_diagonal]

    def is_valid_move(self, move):
        ## Verifica se o player realizou um movimento valido, um movimento valido consiste de
        ## o jogo ainda não atingiu um vencedor e aquele movimento ainda não foi realizado antes.

        row,col = move.row, move.col
        move_was_not_played = self._current_moves[row][col].label == ""
        no_winner = not self._has_winner
        return move_was_not_played and no_winner

    def process_move(self, move): ## Verifica o movimento atual do player e verifica se esse movimento venceu a partida
        row, col = move.row, move.col
        self._current_moves[row][col] = move
        for combo in self._winning_combos:
            results = set(
                self._current_moves[n][m].label for n,m in combo
            )
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self._has_winner = True
                self.winner_combo = combo
                break
    def has_winner(self): # Retorna Verdadeiro se o jogo tem um vencedor se nao retorna falso
        return self._has_winner

    def is_tied(self): #Verifica se o jogo sofreu empate
        no_winner = not self._has_winner
        played_moves =(
            move.label for row in self._current_moves for move in row
        )
        return no_winner and all(played_moves)

    def toggle_player(self): #apos cada movimento troca o player
        self.current_player = next(self._players)

    def reset_game(self): #Reseta o game para jogar novamente
        for row, row_content in enumerate(self._current_moves):
            for col, _ in enumerate(row_content):
                row_content[col] = Move(row,col)
        self._has_winner = False
        self.winner_combo = []


class TicTacToeTabuleiro(tk.Tk):
        def __init__(self, game):
            super().__init__()
            self.title('Jogo da Velha')
            self._game = game
            self._cells = {}
            self._create_menu()
            self._desenha_tabuleiro_display()
            self._desenha_tabuleiro()

        def _desenha_tabuleiro_display(self): # Cria a Tela do jogo
            display_frame = tk.Frame(master=self)
            display_frame.pack( fill=tk.X)
            self.display = tk.Label(
                master=display_frame,
                text="Começar Jogo",
                font = font.Font(size= 28, weight='bold'),
            )
            self.display.pack()


        def _desenha_tabuleiro(self): # desenha o tabuleiro do jogo na interface
            grid_frame = tk.Frame(master=self)
            grid_frame.pack()
            for row in range(self._game.board_size):
                self.grid_rowconfigure(row, weight=1, minsize=50)
                self.grid_columnconfigure(row, weight=1, minsize=75)
                for col in range(self._game.board_size):
                    button = tk.Button(
                        master=grid_frame,
                        text= "",
                        font= font.Font(size=36, weight="bold"),
                        fg="black",
                        width = 4,
                        height = 1,
                        highlightbackground = "lightgrey",

                    )
                    self._cells[button] = (row,col)
                    button.bind("<ButtonPress-1>", self.play)
                    button.grid(row = row, column = col, padx=2, pady=2, sticky="nsew")

        def play(self, event): #Captura o movimento do player
            clicked_button = event.widget
            row, col = self._cells[clicked_button]
            move = Move(row, col, self._game.current_player.label)
            if self._game.is_valid_move(move):
                self._update_button(clicked_button)
                self._game.process_move(move)
                if self._game.is_tied():
                    self._update_display(msg="DEU VELHA", color = "black")
                elif self._game.has_winner():
                    self._highligth_cells()
                    msg = f'Player {self._game.current_player.label} Venceu!'
                    color = self._game.current_player.color
                    self._update_display(msg,color)
                else:
                    self._game.toggle_player()
                    msg = f'É a vez do player {self._game.current_player.label}'
                    self._update_display(msg)

        def _update_button(self, clicked_button): #atualiza o campo clicado pelo player
            clicked_button.config(text = self._game.current_player.label)
            clicked_button.config(fg = self._game.current_player.color)

        def _update_display(self, msg, color = "black"): #atualiza o display
            self.display["text"] = msg
            self.display["fg"] = color

        def _highligth_cells(self): #verifica se as jogadas estao em uma combinação para ganhar e muda o background para vermelho
            for button, coordinates in self._cells.items():
                if coordinates in self._game.winner_combo:
                    button.config(highlightbackground = "red")

        def _create_menu(self): # cria um menu para reiniciar o game
            menu_bar = tk.Menu(self)
            self.config(menu = menu_bar)
            file_menu = tk.Menu(master=menu_bar)
            file_menu.add_command(
                label = "Play Again",
                command = self.reset_board
            )
            file_menu.add_separator()
            file_menu.add_command(label = "Exit", command = quit)
            menu_bar.add_cascade(label = "File", menu = file_menu)

        def reset_board(self):
            self._game.reset_game()
            self._update_display(msg="COMEÇAR JOGO")
            for button in self._cells.keys():
                button.config(highlightbackground = "lightgrey")
                button.config(text="")
                button.config(fg = "black")

def main(): # cria e roda o jogo
    Jogo = TicTacToeGame()
    Tabuleiro = TicTacToeTabuleiro(Jogo)
    Tabuleiro.mainloop()

if __name__ == '__main__':
    main()
