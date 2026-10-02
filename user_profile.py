def get_user_profile():

    print("\n===== Intern Profile =====")

    skills = [
        "python",
        "machine_learning",
        "deep_learning",
        "web_development",
        "data_analysis",
        "automation",
        "ai"
    ]

    interests = [
        "problem_solving",
        "research",
        "building_products"
    ]

    profile = {}

    print("\nEnter your skills (1 = Yes, 0 = No):")

    for skill in skills:

        while True:
            value = input(f"{skill}: ")

            if value in ["0", "1"]:
                profile[skill] = int(value)
                break

            print("Please enter only 0 or 1.")

    print("\nEnter your interests (1 = Interested, 0 = Not Interested):")

    for interest in interests:

        while True:
            value = input(f"{interest}: ")

            if value in ["0", "1"]:
                profile[interest] = int(value)
                break

            print("Please enter only 0 or 1.")

    return profile