import numpy

options = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def alternator(player):
    """
    Switches the player
    :param player: current player
    :return: the next player
    """
    if player in 'X':
        return 'O'
    else:
        return 'X'


def is_number(value):
    """
    Convert value into a number or throw error
    :param value: value to convert
    :return: the value
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def win(player):
    """
    Win print and exit code
    :param player: the current player that won
    :return: None
    """
    print('Winner is player ' + player)
    exit()


def display_field(field_array):
    """
    Format and print the current plays and board
    :param field_array: the field data array
    :return: None
    """
    print('\n   -------------')
    for row in field_array:
        row_str = '   | '
        for item in row:
            row_str = row_str + str(item) + ' | '
        print(row_str)
        print('   -------------')


def in_bounds(field_array, coord):
    """
    Check if the coordinate is in or out of the field_array's boundaries
    :param field_array: the field data array
    :param coord: coordinate to check
    :return: True if it is in bounds, False otherwise
    """
    return True if 0 <= coord[0] <= 2 and 0 <= coord[1] <= 2 else False


def player_in_coord(field_array, coord, player):
    """
    Check the player contained in the given coordinate
    :param field_array: the field data array
    :param coord: coordinate to check
    :param player: player to check
    :return: True if the player is in the coord, False otherwise
    """
    return True if 0 <= coord[0] <= 2 and 0 <= coord[1] <= 2 and player in field_array[coord[0]][coord[1]] else False


def check_next(field_array, orig, found, player):
    """
    Analyze the current plays based on the coordinate to determine if there was a win
    :param field_array: the field data array
    :param orig: the original coordinate that was played last turn
    :param found: the coordinate that we are currently checking to see how it fits in
    :param player: the current player
    :return: None, or errors
    """
    try:
        if player_in_coord(field_array, found, player):  # only analyze coordinates that are owned by current player
            new = numpy.subtract(found, orig)
            check_1 = numpy.add(found, new)
            check_2 = numpy.subtract(orig, new)
            if player_in_coord(field_array, check_1, player):
                win(player)
            if player_in_coord(field_array, check_2, player):
                win(player)
    except TypeError:
        return


def win_conditions(field_array, coord, player):
    """
    Start win condition checking. Generates coordinates around the origin coord
    :param field_array: the array that stores the history of where players have played
    :param coord: the current coordinate that was play this turn
    :param player: the current player
    :return:
    """
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            ncoord = (coord[0] + dx, coord[1] + dy)
            if 0 <= ncoord[0] <= 2 and 0 <= ncoord[1] <= 2 and ncoord != coord:
                check_next(field_array, coord, ncoord, player)


def play(player, field_array):
    """
    Manage the plays and call helper methods like displaying the board and checking for wins
    :param player: current player
    :param field_array: the array that stores the history of where players have played
    :return:  the next player
    """
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

    display_field(field_array)
    win_conditions(field_array, coord, player)
    return alternator(player)


def main():
    """
    Manage and run all methods
    :return: None
    """
    field_array = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]

    player = 'X'
    display_field(field_array)
    while True:
        player = play(player, field_array)


if __name__ == '__main__':
    main()
