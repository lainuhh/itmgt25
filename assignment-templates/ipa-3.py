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
    len_board = len(board[0])

    diagonals = [[board[i][i] for i in range(len(board))], [board[i][len_board - i - 1] for i in range(len_board)]]
    columns = []
    for row_num in range(len_board):
        columns.append([board[i][row_num] for i in range(len_board)])

    dimensions = [diagonals, columns, board]

    for dimension in dimensions:
        for _ in dimension:
            win_ctr = 0
            square_checker = _[0]
            for square in _:
                if square == square_checker:
                    win_ctr += 1
            if win_ctr == len_board and win_ctr != 0 and square_checker != "":
                return square_checker
    return "NO WINNER"


def eta(first_stop, second_stop, route_map):
    route = (first_stop, second_stop)
    if route in route_map:
        return route_map[route]['travel_time_mins']

    route_time = 0
    for stops in route_map.keys():
        if stops[0] == first_stop:
            next_stop = stops[1]
            route_time += route_map[stops]["travel_time_mins"]

    while next_stop != second_stop:
        for iter_stops, time in route_map.items():
            if iter_stops[0] == next_stop:
                next_stop = iter_stops[1]
                route_time += time["travel_time_mins"]
                break
    return route_time
