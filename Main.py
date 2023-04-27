from Player import Player
from TicTacToe import TicTacToe


if __name__ == "__main__":
    p1 = Player('Jugador 1','O')
    p2 = Player('Jugador 2','X')
    tictactoe = TicTacToe(p1,p2)
    tictactoe.play()
    