def main():
    # Prompt user inputs
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Use match case to handle priority
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an unknown priority"

    # Modify reminder based on time sensitivity
    if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
    if priority == "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    else:
        print(f"Reminder: '{task}' is a {priority} priority task.")

    # Print final message
    print(reminder_message)


if __name__ == "__main__":
    main()
