def safe_reward(r):
    eps = 1e-6
    r = float(r)

    # squash strictly into (0,1)
    r = max(eps, min(r, 1 - eps))

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
