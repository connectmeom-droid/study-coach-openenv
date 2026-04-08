def clamp_reward(reward):
    # Ensure reward is strictly between (0, 1)
    return max(0.01, min(reward, 0.99))


def grade_easy(state, action):
    reward = 0.1  # base reward to avoid 0

    # Check weak subject priority
    if action.get(state["weak_subject"], 0) >= 2:
        reward += 0.4

    # Check total hours match
    if sum(action.values()) == state["hours_available"]:
        reward += 0.4

    return clamp_reward(reward)


def grade_medium(state, action):
    reward = 0.1  # base reward

    # Stronger focus on weak subject
    if action.get(state["weak_subject"], 0) >= 3:
        reward += 0.4

    # Adjust based on low previous score
    if state.get("previous_score", 1) < 0.5:
        if action.get(state["weak_subject"], 0) >= 3:
            reward += 0.2

    # Balanced plan
    if sum(action.values()) == state["hours_available"]:
        reward += 0.3

    return clamp_reward(reward)


def grade_hard(state, action):
    reward = 0.1  # base reward

    history = state.get("history", [])

    # Check improvement trend
    if len(history) > 0 and sum(history)/len(history) < 0.6:
        if action.get(state["weak_subject"], 0) >= 3:
            reward += 0.3

    # Smart distribution
    if sum(action.values()) == state["hours_available"]:
        reward += 0.3

    # Consistency
    if all(h < 0.7 for h in history):
        reward += 0.2

    return clamp_reward(reward)
