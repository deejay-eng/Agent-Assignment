import json
import os


def summarize(messages):

    if len(messages) > 10:
        return [
            "Conversation summarized"
        ]

    return messages


def save_checkpoint(state):

    with open(
        "checkpoints/state.json",
        "w"
    ) as f:

        json.dump(
            state,
            f,
            indent=2
        )


def load_checkpoint():

    if not os.path.exists(
        "checkpoints/state.json"
    ):
        return None

    with open(
        "checkpoints/state.json",
        "r"
    ) as f:

        return json.load(f)