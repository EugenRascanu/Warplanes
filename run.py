# Legend
# X for placing plane and hit warplane
# ' ' for available space
# '-' for missed shot
# hidden_board - computers board with plane placement
# guess_board - the board that the player sees / plane placement is hidden from
# the player randit - method that returns an integer number selected element
# from the specified range board is 8x8 / row 1-8 / column A-H random generated
# planes on board = 5
#
# while row/column not in 1-8 + A-H = invalid data (player is asked to input
# correct data)
# max turns = 10
# current turn tells player how many tries he has left

from random import randint

LETTERS_TO_NUMBERS = {'A': 0, 'B': 1, 'C': 2,
                      'D': 3, 'E': 4, 'F': 5,
                      'G': 6, 'H': 7}


def print_board(board):
    print('  A B C D E F G H')
    print('  ---------------')
    row_number = 1
    for board_row in board:
        print("%d|%s|" % (row_number, "|".join(board_row)))
        row_number += 1


def create_ships(board):
    i = 0
    while i < 5:
        create_ship(board)
        i += 1


def create_ship(board):
    hidden_row, hidden_column = randint(0, 7), randint(0, 7)
    if not board[hidden_row][hidden_column] == 'X':
        board[hidden_row][hidden_column] = "X"
    else:
        create_ship(board)


def get_ship_location():
    input_row = get_row()
    input_column = get_column()
    return input_row - 1, LETTERS_TO_NUMBERS[input_column]


def get_row():
    while True:
        try:
            value = int(input('Please enter a ship row 1-8: '))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if ((value < 1) or (value > 8)):
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return value


def get_column():
    while True:
        value = input('Please enter a ship column A-H: ')
        if ((not value) or (value.upper() not in 'ABCDEFGH')):
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return value.upper()


def get_try_again():
    while True:
        value = input('Would you like to try again: (Y/N) ')
        if ((not value) or (value.upper() not in 'YN')):
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return value.upper()


def count_hit_ships(board):
    count = 0
    for board_row in board:
        for board_column in board_row:
            if board_column == 'X':
                count += 1
    return count


def generate_empty_boards():
    hidden_board = [[' '] * 8 for x in range(8)]
    guess_board = [[' '] * 8 for x in range(8)]
    return hidden_board, guess_board


def main():
    hidden_board, guess_board = generate_empty_boards()

    create_ships(hidden_board)
    current_turn = 0
    max_turns = 10
    while current_turn < max_turns:
        print('Welcome to Old School Battleship')
        print_board(guess_board)
        row, column = get_ship_location()
        if not guess_board[row][column] == ' ':
            print('You have already guessed that')
            print(
                'You still have ' +
                str(max_turns - current_turn) +
                ' turns remaining'
                )
            continue

        if hidden_board[row][column] == 'X':
            print('Congratulations, you have hit the battleship')
            guess_board[row][column] = 'X'
            current_turn += 1
        else:
            print('Sorry, you missed')
            guess_board[row][column] = '-'
            current_turn += 1

        if count_hit_ships(guess_board) == 5:
            print('Congratulations, you have sunk all the battleships')
            break

        if current_turn == max_turns:
            print('Sorry, you have no more turns. Game Over')
            try_again = get_try_again()
            if(try_again == "Y"):
                main()
            else:
                break
            break
        else:
            print('You have ' +
                  str(max_turns - current_turn) +
                  ' turns remaining')

try:
    main()
except KeyboardInterrupt:
    print('Goodbye')