SHAPE_POINTS = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

OUTCOME_POINTS = {
    'AX': 3,
    'AY': 6,
    'AZ': 0,
    'BX': 0,
    'BY': 3,
    'BZ': 6,
    'CX': 6,
    'CY': 0,
    'CZ': 3
}


def strategy_guide_sum():
    """
    A Rock X Rock (1 point)
    B Paper Y Paper (2 points)
    C Scissors Z Scissors (3 points)

    Lost = 0
    Draw = 3
    Won = 6

    game_score = shape_points +  outcome_points
    """
    total_score = 0

    with open('./input.txt') as input_file:
        for line in input_file:
            game = line.strip().replace(' ', '')
            shape_points = SHAPE_POINTS[game[1]]
            outcome_points = OUTCOME_POINTS[game]
            total_score += (shape_points + outcome_points)

    print(total_score)


OUTCOME_POINTS_EXPECTED = {
    'X': 0,
    'Y': 3,
    'Z': 6
}


def get_shape_points_given_outcome(opponent_play, desired_outcome):
    for (key, value) in OUTCOME_POINTS.items():
        if opponent_play in key and value == desired_outcome:
            return SHAPE_POINTS[key[1]]


def strategy_guide_sum_part_2():
    """
    A Rock X Rock (1 point)
    B Paper Y Paper (2 points)
    C Scissors Z Scissors (3 points)

    Lost = 0
    Draw = 3
    Won = 6

    game_score = shape_points +  outcome_points
    X - Lose
    Y - Draw
    Z - Win

    Example
    CY - draw
    game_score = ? + 3

    """
    total_score = 0

    with open('./input.txt') as input_file:
        for line in input_file:
            game = line.strip().replace(' ', '')
            outcome_points = OUTCOME_POINTS_EXPECTED[game[1]]
            shape_points = get_shape_points_given_outcome(game[0], outcome_points)
            total_score += (shape_points + outcome_points)

    print(total_score)


if __name__ == '__main__':
    strategy_guide_sum()
    strategy_guide_sum_part_2()
