# list board created to store which letter is assigned at particlar position,
# we have taken size till 10, because in board 0 is not included in board
board = [' ' for x in range(10)]


# funtion designed to take the input from the player,(the position ofy the box) ----------------------------------
def insertLetter(letter, pos):
    if isBoardFull(board): # if the board is full, them we return the message that, "None of you won!"
        return "The game is Draw!"
    else:
        board[pos] = letter


# funciton to check if there is free space at position pos, to enter the value ----------------------------------
def spaceIsFree(pos):
    return board[pos] == ' '


# function defined for printing the look of board after each move --------------------------------------------
def printBoard(board):
    # print('-------------------------')
    print('       |       |       ')
    print('   ' + board[1] + '   |   ' + board[2] + '   |   ' + board[3] + '   ')
    print('       |       |       ')
    print('-------------------------')
    print('       |       |       ')
    print('   ' + board[4] + '   |   ' + board[5] + '   |   ' + board[6] + '   ')
    print('       |       |       ')
    print('-------------------------')
    print('       |       |       ')
    print('   ' + board[7] + '   |   ' + board[8] + '   |   ' + board[9] + '   ')
    print('       |       |       ')
    # print('-------------------------')


# function to check if board is full, or not -----------------------------------------------------------
def isBoardFull(board):
    if board.count(' ') > 1: # for checking we just count the empty string , then there is some space present
        return False
    else:
        return True


# function defined to check who is the winner, wither player or computer -----------------------------------------
def IsWinner(board,letter): # here we check all the cases
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[3] == letter and board[5] == letter and board[7] == letter))


# function defined for player move ----------------------------------------------------------------------
def playerMove():
    run = True
    while run:
        move = input("Please select a position to enter the X between 1 to 9 : ") # taken input from player
        try:
            move = int(move) # type casting the imput into integer
            if move > 0 and move < 10:
                if spaceIsFree(move): # if input is valid, then add input at that positoon
                    run = False
                    insertLetter('X' , move)
                else:
                    print('Sorry, this space is occupied.')
            else:
                print('Please type a number between 1 and 9.')

        except:
            print('Please type a number.') # when try code is not run, then this message will be displayed


# function defined for computer move ----------------------------------------------------------------------
def computerMove():
    # first we get list of positon where computer can entered it's letter
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0 ]
    move = 0

    for let in ['O', 'X']: # we just loop through all possible values and checks for the correct/optimal position for computer
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move

    # checking all the corner values
    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]: # 4 corners are at position 1,3,7,9, sowe check for all position
            cornersOpen.append(i)
    if len(cornersOpen) > 0: # if conditon satisfied, we take any random position from corner position we got
        move = selectRandom(cornersOpen)
        return move

    # checking for center position that is 5
    if 5 in possibleMoves:
        move = 5
        return move

    # checking ofr edge postion , that are 2,4,6,8
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:# if conditon satisfied, we take any random position from edge position we got
        move = selectRandom(edgesOpen)
        return move


# function defined to select random position for the list that is passed as parameter --------------------------
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


# function defined for the main logic of the game -----------------------------------------------------------------
def main():
    print("Welcome to the game!") # printing the starting message
    printBoard(board)

    while not(isBoardFull(board)):
        if not(IsWinner(board , 'O')):
            playerMove()
            printBoard(board) # printing the updated board
        else:
            print("Sorry you loose!")
            break

        if not(IsWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move)
                print('Computer placed an O on position ' , move , ':')
                printBoard(board) # printing the updated board
        else:
            print("You won!")
            break

    if isBoardFull(board): # is board is full, so we tie the game, as no one won and board become full
        print("The game tied.")


# running the while loop for playing game till player wants -------------
while True:
    x = input("Do you want to play again? (y/n) : ")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('-----------------------------')
        main()
    else: # if player entered n, just break through loop
        break