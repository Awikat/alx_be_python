print("Enter your task: ")
task = input()
print("High/medium/low: ")
priority = input()
print("")

print("Is it time bound: (yes/no): ")
istimebound = input()

match priority,istimebound:
    case 'high','yes':
        print(task+"is a high priority task "+
              "that requires immediate attention today!")
    case 'low','no':
        print(task+"is a low priority task. Consider"+ 
              "completing it when you have free time.")
    case 'high','no':
        print(task+"is a high priority task that "
              +"requires immediate attention today!")
    case 'low','yes':
        print(task+"is a high priority task "+
              "that requires immediate attention today!")
    case 'medium','yes':
        print(task +"is a medium priority task that requires immediate attention today!")
    case 'medium', 'no':
        print( task +"is a medium priority task. Consider completing it when you have free time" )
