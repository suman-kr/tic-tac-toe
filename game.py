from pyfiglet import figlet_format
from termcolor import cprint
cprint(figlet_format('Tic Tac Toe',font='big'))
print ("Copyright © Suman Kumar\n")
print ("Enter the size of the board separated by space")
print ("min = {}x{} , max = {}x{}".format(3,3,10,10))
try:
    r , c = [int(i) for i in input().split()]
except:
    print ("Not enough value")
    exit()
if r != c:
    raise ValueError('Different values for Row and column')
if r < 3 or c < 3:
    raise ValueError('Values of Row and column cannot be less than 3')
if r > 10 or c > 10:
    raise ValueError('Values of Row and column cannot be more than 10')
print("Row and column reference for 3x3 board:")
m = [["*" for i in range(r)] for j in range(c)]
print("00|01|02\n__|__|__\n10|11|12\n__|__|__\n20|21|22")

print("Co-ordinate examples for {}x{} board".format(r,c))
for i in range(r):
    for j in range(c):
        print("{}{}\t".format(i,j) ,end="")
    print()

print()


def board():
    for i in m:
        for j in i:
            print(j, " ", end="")
        print()


player1 = "X"
player2 = "0"


def checkInput(inp):
    flag = True
    if len(inp) < 2 or len(inp) > 2:
        print("Wrong Input")
        flag = False
        exit()
    mr = int(inp[0])
    mc = int(inp[1])
    if mr > r-1 or mc > c-1 :
        print("Wrong Input")
        flag = False
        exit()
    return True if flag else False


def checkMoves(inp):
    flag = True
    mr = int(inp[0])
    mc = int(inp[1])
    if m[mr][mc] != "*":
        print("Illegal Move")
        flag = False
        exit()
    return True if flag else False


def game(current):
    # flag = True
    # count = 0
    diag = 0
    rev = 0
    for i in range(0, r):
        ch , cv = 0 , 0
        for j in range(0, c):
            if m[i][j] == current:
                ch += 1
            if (i == j) and (m[i][j] == current):
                diag += 1
            if (i+j == r-1) and (m[i][j] == current):
                rev += 1
            if m[j][i] == current:
                cv += 1

        if ch == r or cv == r:
            break
    if ch == r or diag == r or rev == r or cv == r:
        return True
    else:
        return False


def player():
    for i in range(r *c):
        board()
        if i % 2 == 0:
            print("move for player", player1, ": ", end="")
            inp = input()
            if checkInput(inp) == True:
                if checkMoves(inp) == True:
                    # print ("Legal Move")
                    mr = int(inp[0])
                    mc = int(inp[1])
                    m[mr][mc] = player1
                    if game(player1):
                        print("Player1 won")
                        board()
                        exit()

        else:
            print("move for player", player2, ": ", end="")
            inp = input()
            if checkInput(inp) == True:
                if checkMoves(inp) == True:
                    # print ("Legal Move")
                    mr = int(inp[0])
                    mc = int(inp[1])
                    m[mr][mc] = player2
                    if game(player2):
                        print("Player2 won")
                        board()
                        exit()

if __name__ == "__main__":
    player()
# board()
