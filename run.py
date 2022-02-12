#Legend
# X for placing plane and hit warplane
# ' ' for available space
# '-' for missed shot
# HIDDEN_BOARD - computers board with plane placement
# GUESS_BOARD - the board that the player sees / plane placement is hidden from the player
# randit - method that returns an integer number selected element from the specified range
# board is 8x8 / row 1-8 / column A-H
# random generated planes on board = 5
# while row/column not in 1-8 + A-H = invalid data (player is asked to input correct data)
# max turns = 10
# current turn tells player how many tries he has left



from random import randint

HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
GUESS_BOARD = [[' '] * 8 for x in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2,
                      'D': 3, 'E': 4, 'F': 5,
                      'G': 6, 'H': 7}


def print_board(board):
    print('  A B C D E F G H')
    print('  ---------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    for ship in range(5):
        create_ship(board)


def create_ship(board):
    row, column = randint(0, 7), randint(0, 7)
    if not board[row][column] == 'X':
        board[row][column] = "X"
    else:
        create_ship(board)


def get_ship_location():
    row = input('Please enter a ship row 1-8: ')
    while row not in '12345678':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1-8: ')
    column = input('Please enter a ship column A-H: ').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column')
        column = input('Please enter a ship column A-H: ').upper()
    return int(row) - 1, letters_to_numbers[column]


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

create_ships(HIDDEN_BOARD)

current_turn = 0
max_turns = 10
while current_turn < max_turns:
    print('Welcome to Warplanes')
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if not GUESS_BOARD[row][column] == ' ':
        print('You have already guessed that')
        print(
            'You still have ' +
            str(max_turns - current_turn) +
            ' turns remaining'
            )
        continue

    if HIDDEN_BOARD[row][column] == 'X':
        print('Congratulations, you have a warplane')
        GUESS_BOARD[row][column] = 'X'
        current_turn += 1
    else:
        print('Sorry, you missed')
        GUESS_BOARD[row][column] = '-'
        current_turn += 1

    if count_hit_ships(GUESS_BOARD) == 5:
        print('Congratulations. The warplanes are shot down. The sky is clear')
        break

    if current_turn == max_turns:
        print('Sorry, you have no more turns. Game Over')
        break
    else:
        print('You have ' + str(max_turns - current_turn) + ' turns remaining')
