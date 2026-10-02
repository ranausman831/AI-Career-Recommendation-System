import json
import os

FILE = "progress.json"


def load_progress():

    if os.path.exists(FILE):

        with open(FILE, "r") as f:
            return json.load(f)

    return {
        "career": "",
        "completed": []
    }


progress = load_progress()


def add_career(career):

    progress["career"] = career

    save_progress()


def mark_completed(topic):

    if topic not in progress["completed"]:

        progress["completed"].append(topic)

        save_progress()


def get_progress():

    return progress


def save_progress():

    with open(FILE, "w") as f:
        json.dump(progress, f, indent=4)