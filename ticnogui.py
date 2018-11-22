class TicTacToe:
    def __init__(self,boardSize):
        self.state  = []
        self.total = 0
        self.winner = None
        self.boardSize = boardSize
        self.createBoard(boardSize)
    def createBoard(self,boardSize):
        for i in range(boardSize * boardSize):
            #0 or null
            self.state.append(0)
    def printBoard(self):
        currentIter = 0
        for i in self.state:
            print(i, end =" ")
            currentIter = currentIter + 1
            if(currentIter == self.boardSize ):
                print("\n")
                currentIter = 0
    def alterStatePlayer1(self,playerMove):
        self.state[playerMove]= 1
    def alterStatePlayer2(self,playerMove):
        self.state[playerMove]= -1
    def checkWinner(self):
        self.checkHorizontal()
        self.checkVertical()
        self.checkCross()
    def checkHorizontal(self):
        currentPosition = 0

        #start with 0 increment with boardsize
        for i in range(self.boardSize):
            self.total = 0
            for j in range(self.boardSize):

                self.total = self.state[j+currentPosition] + self.total

            if(self.total == self.boardSize):
                self.winner = True
            elif(self.total == -(self.boardSize)):
                self.winner = False
            currentPosition = currentPosition + self.boardSize

    def checkVertical(self):
        currentPosition = 0

        #start with 0 increment with boardsize
        for i in range(self.boardSize):
            self.total = 0
            currentPosition = 0
            for j in range(self.boardSize):

                self.total = self.state[i+currentPosition] + self.total
                currentPosition = currentPosition + self.boardSize

            if(self.total == self.boardSize):
                self.winner = True
            elif(self.total == -(self.boardSize)):
                self.winner = False


    def checkCross(self):
        currentPosition = 0
        self.total = 0
        # right cross
        for i in range(self.boardSize):
            self.total = self.state[currentPosition] + self.total
            if(self.total == self.boardSize):
                self.winner = True
            elif(self.total == -(self.boardSize)):
                self.winner = False
            currentPosition = currentPosition + self.boardSize + 1
        # left cross
        currentPosition = self.boardSize-1
        self.total = 0
        for i in range(self.boardSize):
            self.total = self.state[currentPosition] + self.total
            print(self.total)
            if(self.total == self.boardSize):
                self.winner = True
            elif(self.total == -(self.boardSize)):
                self.winner = False
            currentPosition = currentPosition + self.boardSize-1


userInput = int(input("Enter size of the board: 1 by 1 , 2 by 2 , 3 by 3 , 4 by 4 "))
numberOfPlays = userInput * userInput
movesNeededToCheckWin= (userInput + userInput) - 1
a = TicTacToe(userInput)
for plays in range(numberOfPlays):
    if(plays%2 >0 ):
        player1Move = input("Player 2: Please enter move (from 0 to x depend on board size) position ")
        a.alterStatePlayer1(int(player1Move))
        a.printBoard()
    else:
        player2Move = input("Player 1: Please enter move (from 0 to x depend on board size) position ")
        a.alterStatePlayer2(int(player2Move))
        a.printBoard()
    if(plays >= movesNeededToCheckWin -1):
        a.checkWinner()
        print(a.winner)
        if(a.winner == True):
            print("player 2 win")
            quit()
        elif(a.winner == False):
            print("player 1 win")
            quit()
