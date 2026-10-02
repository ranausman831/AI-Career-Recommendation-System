
import tensorflow as tf
import json
import numpy as np


# Saved model load karo
model = tf.keras.models.load_model(
    "model/career_model.keras"
)


# Career labels load karo
with open("model/career_labels.json", "r") as f:
    career_labels = json.load(f)


def predict_career(profile):

    # 10 features ko correct order mein arrange karo
    features = [
        profile["python"],
        profile["machine_learning"],
        profile["deep_learning"],
        profile["web_development"],
        profile["data_analysis"],
        profile["automation"],
        profile["ai"],
        profile["problem_solving"],
        profile["research"],
        profile["building_products"]
    ]

    # Model prediction
    prediction = model.predict(
        np.array([features]),
        verbose=0
    )

    predicted_index = np.argmax(prediction)

    career = career_labels[predicted_index]

    confidence = float(prediction[0][predicted_index])

    return career, confidence