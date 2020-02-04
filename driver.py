import random
import numpy

options = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def alternator(player):
    if player in 'X':
        return 'O'
    else:
        return 'X'


def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def display_field(field_array):
    print('\n   -------------')
    for row in field_array:
        row_str = '   | '
        for item in row:
            row_str = row_str + str(item) + ' | '
        print(row_str)
        print('   -------------')


def check_next(field_array, ocoord, coord, player):
    try:
        if player in field_array[coord[0]][coord[1]]:
            difference = numpy.subtract(coord, ocoord)
            last_spot = numpy.add(coord, difference)
            other_last_spot = numpy.subtract(coord, difference)
            print(difference)
            print(last_spot)
            if 0 <= last_spot[0] <= 2 and 0 <= last_spot[1] <= 2 and player in field_array[last_spot[0]][last_spot[1]]:
                print('Winner is player ' + player)
                exit()

    except TypeError:
        return


def win_conditions(field_array, coord, player):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            ncoord = (coord[0] + dx, coord[1] + dy)
            if 0 <= ncoord[0] <= 2 and 0 <= ncoord[1] <= 2 and ncoord != coord:
                check_next(field_array, coord, ncoord, player)


def play(player, field_array):
    # 19237486 causes error
    i = input('Player ' + player + ', enter the number in which to place your mark: ')
    if not is_number(i) or not any(int(i) in sublist for sublist in field_array):
        print('Value is not valid. Try again')
        return player
    coord = ()
    for num, ind in enumerate(field_array):
        try:
            index = ind.index(int(i))
            field_array[num][index] = player
            coord = (num, index)
        except ValueError:
            continue

    win_conditions(field_array, coord, player)
    display_field(field_array)
    return alternator(player)


def main():
    field_array = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
    player = 'X'
    display_field(field_array)
    while True:
        player = play(player, field_array)


main()
