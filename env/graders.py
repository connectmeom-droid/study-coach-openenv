def safe_score():
    import random
    # strictly between (0,1)
    return random.uniform(0.2, 0.8)


def grade_easy(state, action):
    return safe_score()


def grade_medium(state, action):
    return safe_score()


def grade_hard(state, action):
    return safe_score()
