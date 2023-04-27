
from Player import Player


class TicTacToe:
    def __init__(self,player1: Player,player2: Player):
        self.__player1 = player1
        self.__player2 = player2
        self.__table = [[1,2,3],[4,5,6],[7,8,9]]
    
    def __setPlayerToken(self,token,position : int):
        if(not self.validateMove(position)):
           return False
        for i in range(len(self.__table)):
            for j in range(len(self.__table[i])):
                if(self.__table[i][j] == position):
                    self.__table[i][j] = token
                    return True
        return False
    
    def play(self):
        print("----------Bienvenido al juego de Tateti-----------")
        endGame = False
        self.__table[1][1] = 'X'
        isPlayerTurn = True
        winner = None
        total_moves = 0
        while(not endGame and total_moves < 8):
            valideMove = False
            if isPlayerTurn:
                self.display_board()
                while(not valideMove):
                    move = self.__player1.doAMove()
                    position = int(input("Ingresa tu movimiento:"))
                    valideMove = self.__setPlayerToken(move,position)
                    if(not valideMove):
                        print('Elija una posicion valida')
                endGame = self.__checkVictory(self.__player1.doAMove())
                if endGame:
                    winner = self.__player1
                isPlayerTurn = False
            else:
                while(not valideMove):
                    move = self.__player2.doAMove()
                    position = self.__player2.randomChoice()
                    valideMove = self.__setPlayerToken(move,position)
                endGame = self.__checkVictory(self.__player2.doAMove())
                if endGame:
                    winner = self.__player2
                isPlayerTurn = True
            total_moves += 1
            print(f"total de jugadas restantes => {total_moves} 👀")
        self.display_board()
        if(winner != None):
            print(f"el ganador de la partida es el {winner.getName()} 😁")
        else:
            print("No gano nadie 😫")

    def __checkVictory(self,token : str):
        if(self.__horizontalCheck(token)):
            return True
        elif(self.__verticalCheck(token)):
            return True
        elif(self.__diagonalCheck(token)):
            return True
        else:
            return False
        

    def __horizontalCheck(self,token):
        for i in range(len(self.__table)):
            victoryMoves = [x for x in self.__table[i] if x == token]
            if(len(victoryMoves) == 3):
                return True
        return False
    
    def __verticalCheck(self,token):
        for i in range(len(self.__table)):
            __count = 0
            for j in range(len(self.__table[i])):
                if(self.__table[j][i] == token):
                    __count += 1
            if( __count == 3):
                return True
        return False
    def __diagonalCheck(self,token):
        if(self.__table[0][0] == token and self.__table[1][1] == token and self.__table[2][2] == token):
            return True
        elif(self.__table[0][2] == token and self.__table[1][1] == token and self.__table[2][0] == token):
            return True
        else:
            return False
    def validateMove(self,position):
        return (position>0 and position<10)
    def display_board(self):
        print("+-------+-------+-------+")
        for row in self.__table:
            row_str = ""
            for cell in row:
                row_str += f"|   {cell}   "
            print(row_str + "|")
            print("+-------+-------+-------+")

