def grade_easy(state, action):
    reward = 0.0

    # Check weak subject priority
    if action.get(state["weak_subject"], 0) >= 2:
        reward += 0.5

    # Check total hours match
    if sum(action.values()) == state["hours_available"]:
        reward += 0.5

    return reward


def grade_medium(state, action):
    reward = 0.0

    # Stronger focus on weak subject
    if action.get(state["weak_subject"], 0) >= 3:
        reward += 0.5

    # Adjust based on low previous score
    if state.get("previous_score", 1) < 0.5:
        if action.get(state["weak_subject"], 0) >= 3:
            reward += 0.3

    # Balanced plan
    if sum(action.values()) == state["hours_available"]:
        reward += 0.2

    return reward


def grade_hard(state, action):
    reward = 0.0

    history = state.get("history", [])

    # Check improvement trend
    if len(history) > 0 and sum(history)/len(history) < 0.6:
        if action.get(state["weak_subject"], 0) >= 3:
            reward += 0.4

    # Smart distribution
    if sum(action.values()) == state["hours_available"]:
        reward += 0.3

    # Consistency
    if all(h < 0.7 for h in history):
        reward += 0.3

    return reward