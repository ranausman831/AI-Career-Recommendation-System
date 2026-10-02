import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import json


# Dataset load karna
data = pd.read_csv("data/career_data.csv")

print("Dataset:")
print(data)


# Features aur target alag karna
X = data.drop("career", axis=1)
y = data["career"]


# Career names ko numbers mein convert karna
encoder = LabelEncoder()
y = encoder.fit_transform(y)

print("\nCareer labels:")
print(encoder.classes_)


# Training aur testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# TensorFlow neural network
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),

    tf.keras.layers.Dense(16, activation="relu"),

    tf.keras.layers.Dense(16, activation="relu"),

    tf.keras.layers.Dense(
        len(encoder.classes_),
        activation="softmax"
    )
])


# Model compile
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


# Model training
model.fit(
    X_train,
    y_train,
    epochs=100,
    verbose=1
)


# Model test
loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print("\nTest Accuracy:", accuracy)


# Model save
model.save("model/career_model.keras")


# Career labels save
with open("model/career_labels.json", "w") as f:
    json.dump(
        encoder.classes_.tolist(),
        f
    )


print("\nModel saved successfully!")