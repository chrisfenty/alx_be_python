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
        # Time-bound tasks require immediate attention
        reminder_message = f"Reminder: {reminder} that requires immediate attention today!"
    else:
        # Non-time-bound, customize for low priority
        if priority == "low":
            reminder_message = f"Note: {reminder}. Consider completing it when you have free time."
        else:
            # For medium/high not time-bound just print reminder normally
            reminder_message = f"Reminder: {reminder}."

    # Print final message
    print(reminder_message)


if __name__ == "__main__":
    main()
