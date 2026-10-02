
from user_profile import get_user_profile
from predictor import predict_career
from learning_path import get_learning_path
from progress import add_career, mark_completed, get_progress


# 1. Intern profile
profile = get_user_profile()


# 2. Career prediction using skills + interests
career, confidence = predict_career(profile)

print("\n===== Career Recommendation =====")

print("Recommended Career:", career)
print("Confidence:", round(confidence * 100, 2), "%")


# 3. Generate learning path
learning_path = get_learning_path(career, profile)

print("\n===== Personalized Learning Path =====")

for index, topic in enumerate(learning_path, start=1):
    print(f"{index}. {topic}")


# 4. Track progress
add_career(career)

print("\n===== Update Learning Progress =====")

if learning_path:
    mark_completed(learning_path[0])

print(get_progress())