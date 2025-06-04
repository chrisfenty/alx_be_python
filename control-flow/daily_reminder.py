def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an unknown priority"

    if time_bound == "yes":
        # Task requires immediate attention if time-bound
        reminder += " that requires immediate attention today!"
    else:
        # If not time-bound, suggest to do when free for low priority, else neutral
        if priority == "low":
            reminder = f"Note: {reminder}. Consider completing it when you have free time."
        else:
            reminder += "."

    print("\nReminder:", reminder)

if __name__ == "__main__":
    main()
