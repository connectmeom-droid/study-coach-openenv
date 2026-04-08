def get_easy_task():
    return {
        "task_id": 1,
        "description": "Create a daily study plan for a student with 6 hours and weak subject Physics",
        "state": {
            "hours_available": 6,
            "weak_subject": "Physics"
        }
    }


def get_medium_task():
    return {
        "task_id": 2,
        "description": "Improve study plan based on previous poor performance in Physics",
        "state": {
            "hours_available": 6,
            "weak_subject": "Physics",
            "previous_score": 0.4
        }
    }


def get_hard_task():
    return {
        "task_id": 3,
        "description": "Optimize a weekly study plan based on past performance",
        "state": {
            "hours_available": 6,
            "weak_subject": "Physics",
            "history": [0.4, 0.5, 0.6]
        }
    }