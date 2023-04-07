'''Implements the functionality needed for logging a fight'''

def expected_score(r_a : float, r_b : float) -> float:
    '''Calculates the expected score given the rating of oneself and the opponent'''
    elo_constant = 400
    q_a = 10 ** (r_a / elo_constant)
    q_b = 10 ** (r_b / elo_constant)
    return q_a / (q_a + q_b)


def calculate_new_winner_elo(r_a : float, r_b : float):
    ''' update the elo of the winner'''
    k : float = 40
    p_a : float = expected_score(r_a, r_b)
    new_r_a : float = r_a + k * (1 - p_a)
    return new_r_a

def calculate_new_loser_elo(r_a : float, r_b : float):
    ''' update the elo of the loser'''
    k : float = 40
    p_b : float = expected_score(r_b, r_a)
    new_r_b : float = r_b + k * (0 - p_b)
    return new_r_b

def main():
    '''main functionality'''
    # Asks for the fighters' ratings
    rating_a : float = float(input("What is the winner's rating?\n"))
    rating_b : float = float(input("What is the loser's rating?\n"))


    ### Calculates and prints probability
    expected_score_a : float = expected_score(rating_a, rating_b)

    print(F"The probability of the outcome was {100 * expected_score_a:.3f}%\n")


    ### Asks for fight result
    winner_elo = calculate_new_winner_elo(rating_a, rating_b)
    loser_elo = calculate_new_winner_elo(rating_b, rating_a)
    print(F"The new ratings are: \nWinner: {winner_elo}\nLoser: {loser_elo}\n")


    ### modifies the fighters' data

if __name__ == "__main__":
    main()
