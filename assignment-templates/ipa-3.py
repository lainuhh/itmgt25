
def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph[from_member]['following'] and from_member in social_graph[to_member]['following']:
        return "friends"
    elif from_member in social_graph[to_member]['following']:
        return "followed by"
    elif to_member in social_graph[from_member]['following']:
        return "follower"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    len_board = len(board[0])

    diagonals = [[board[i][i] for i in range(len(board))], [board[i][len_board - i - 1] for i in range(len_board)]]
    columns = []
    for row_num in range(len_board):
        columns.append([board[i][row_num] for i in range(len_board)])
    print(columns)

    dimensions = [diagonals, columns, board]

    for dimension in dimensions:
        print(f"NEW DIMENSION")
        for _ in dimension:
            win_ctr = 0
            square_checker = _[0]
            for square in _:
                if square == square_checker:
                    win_ctr += 1
        if win_ctr == len_board:
            return square_checker
    return "NO WINNER"


def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass
