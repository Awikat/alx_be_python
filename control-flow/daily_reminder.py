def get_user_input(prompt):
  """Gets user input for task, priority, and time sensitivity."""
  while True:
    response = input(prompt)
    if response.lower() in ("yes", "no"):
      return response.lower() == "yes"
    elif response.lower() in ("high", "medium", "low"):
      return response.lower()
    else:
      print("Invalid input. Please enter 'yes' or 'no' or 'high', 'medium', or 'low'.")

def main():
  """Prompts user for task details and provides a reminder."""
  task = input("Enter your task: ")
  priority = input("Priority (high/medium/low): ")
  time_bound = get_user_input("Is it time-bound? (yes/no): ")

  reminder = f"Reminder: '{task}' is a {priority} priority task"

  if time_bound:
    reminder += " that requires immediate attention today!"
  else:
    reminder += ". Consider completing it when you have free time."

  print(reminder)

if __name__ == "__main__":
  main()
