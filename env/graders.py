def safe_reward(r):
    r = float(r)

    if r <= 0:
        return 0.01
    if r >= 1:
        return 0.99

    if r >= 0.999:
        return 0.99
    if r <= 0.001:
        return 0.01

    return r


def grade_easy(state, action):
    reward = 0.2

    if action.get(state["weak_subject"], 0) >= 2:
        reward += 0.3

    if sum(action.values()) == state["hours_available"]:
        reward += 0.3

    return safe_reward(reward)


def grade_medium(state, action):
    reward = 0.2

    if action.get(state["weak_subject"], 0) >= 3:
        reward += 0.3

    if state.get("previous_score", 1) < 0.5:
        if action.get(state["weak_subject"], 0) >= 3:
            reward += 0.2

    if sum(action.values()) == state["hours_available"]:
        reward += 0.2

    return safe_reward(reward)


def grade_hard(state, action):
    reward = 0.2

    history = state.get("history", [])

    if len(history) > 0 and sum(history)/len(history) < 0.6:
        if action.get(state["weak_subject"], 0) >= 3:
            reward += 0.2

    if sum(action.values()) == state["hours_available"]:
        reward += 0.2

    if all(h < 0.7 for h in history):
        reward += 0.2

    return safe_reward(reward)
