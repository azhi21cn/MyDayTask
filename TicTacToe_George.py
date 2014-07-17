__author__ = 'George'
__email__ = "shiguizhi_day@hotmail.com"
__status__ = "interview task"
__create_date__ = "21:20 17/07/2014"

"""
This is simple function for Tic Tac Toe game!
"""
class TicTacToe:
    def __init__(self):
        print """Welcome to Tic Tac Toe! Here is play board!Input the index of where you wish to place your mark at your turn."""
        self.board = [[' ' for x in xrange(3)] for x in xrange(3)]
        self.print_board()
        self.player1 = False
        self.player2 = False
        self.turn = ""
    #place mark function: input:symbol (String), row(Int), column(int), return:None
    def placerMarker(self, symbol=None,row=None,column=None):
        #check current user
        if self.player1:
            print "player1 is your turn! "
            self.turn = "player1"
        elif self.player2:
            print "player2 is your turn!"
            self.turn = "player2"
        # this game only has 9 round, also check is correct user playing
        current_value = self.board[row][column]
        #check cell has been taken by another player or not.
        if current_value == ' ':
            self.board[row][column] = symbol
        else:
            print 'This place:row:',row,', column:',column,' is already taken! '
        # print board after place a mark
        self.print_board()
        win_check = self.win_check(self.board)
        # check is win or not
        if win_check == 1:
           self.on("finished",self.callback(symbol))
        elif win_check == -1:
          self.on("finished",self.callback("draw"))
        else:
            pass


    def on(self,event, fun):
        if event == "finished":
           print "Game is finished"


    def print_function(self):
        print 'a'

    def print_board(self):
        print """
                +----+---+---+---+
                |    | 1 | 2 | 3 |
                +----+---+---+---+
             row| 0  | {0} | {1} | {2} |
                +----+---+---+---+
             row| 1  | {3} | {4} | {5} |
                +----+---+---+---+
             row| 2  | {6} | {7} | {8} |
                +----+---+---+---+""".format(self.board[0][0],self.board[0][1],self.board[0][2],self.board[1][0],
                                                    self.board[1][1],self.board[1][2],self.board[2][0],self.board[2][1],
                                                    self.board[2][2])
    #win check function input: board(Array) return: 1:win,0 not win yet, -1:draw
    def win_check(self, board):
        for i in range(0,3):
            if board[i][0] == board[i][1] == board[i][2] != " " or board[0][i] == board[1][i] == board[2][i] != " ":
                return 1

        if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
            return 1

        if " " not in board[0] and " " not in board[1] and " " not in board[2]:
            return -1
        return 0

    def callback(self, reason=None):
        if reason == "draw":
            print "It's a draw!"
        elif reason == "o":
            print "The winner is:",self.turn ,":",reason
        elif reason == "x":
            print "The winner is:",self.turn ,":",reason

#for bonus question
class player(TicTacToe):
    def __init__(self,player1=False,player2=False,ttt=None):
        self.ttt = ttt
        ttt.player1 = player1
        ttt.player2 = player2


# no user select
ttt=TicTacToe()
ttt.placerMarker('x', 0, 0);

ttt.placerMarker('o', 0, 0);

ttt.placerMarker('o', 1, 0);

ttt.placerMarker('x', 0, 1);

ttt.placerMarker('o', 2, 0);

ttt.placerMarker('x', 0, 2)

#user select for bonus question
ttt=TicTacToe()
player1 = player(player1=True,ttt=ttt)
player2 = player(player2=True,ttt=ttt)

player1.ttt.placerMarker('x', 0, 0);
player2.ttt.placerMarker('o', 0, 0);

player1.ttt.placerMarker('o', 1, 0);

player2.ttt.placerMarker('x', 0, 1);

player1.ttt.placerMarker('o', 2, 0);

player2.ttt.placerMarker('x', 0, 2)
"""
There are many way could do it.
I create a Player class in the script, and you can get TicTacToe object and then pass to two players object before you 'play'
another solution could be create two dictionary variables for two players such as player1={'symbol':''} player2 = {'symbol':''},
it will be easliy set value when the user first time call placerMarker() function.

Besides, for this script  I do checked:player can't place mark at same place or the place has been marked.
I did't do check round, it should be only 9 round, but it ease to create a function increase a variable by each time placemarker function is called.
and it should have player check, which means it shouldn't allow same player continue placed  twice.

Cheers
George
"""