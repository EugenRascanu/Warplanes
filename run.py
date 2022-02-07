print ""
print """Welcome to Battleship!
Have fun and good luck!"""
print""

from random import randint

board = []

for x in range(0,6):
    board.append(["0"] * 6)

    def print_board(board):
        for i in range(1,6):
            for j in range(1,6):
                print board[i][j],
                print ""

print_board(board)

def random_row(board):
    return randint(1, len(board) - 1)

    def random_col(board):
        return randint(1, len(board[0] -1)

        ship_row = random_row(board)
        ship_col = random_col(board)

        def game_play():
            play_again="YES"
            while play_again.lower()=="yes":
                for turn in range (4):
                    print ""
                    print "Turn", turn + 1
                    guess_col = input("Guess Col: ")
                    guess_row = input("Guess Row: ")

                    if guess_row == ship_row and guess_col == ship_col:
                        print ""
                        print "Congratulations! You sank my battleship!"
                        print ""
                        break
                    
                    else:
                        if guess_row not in range(1,6) or \
                            guess_col not in range(1,6):
                            print ""
                            print "Erm, that's not even in the ocean!"
                            print ""

                        elif board[guess_row][guess_col] == "X":
                            print ""
                            print "You've already guess that one!"
                            print ""

                            else:
                                print ""
                                print "You missed!"
                                print ""
                                board[guess_row][guess_col] = "X"
                                print_board(board)

                                if (turn == 3):
                                    print ""
                                    print "GAME OVER"
                                    print ""

                                play_again = raw_input ("Do you want to play again(Yes/No):" )
                                print ""
                                print "Thanks for playing!".upper()

                                game_play()