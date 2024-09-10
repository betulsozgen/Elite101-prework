# Chatbot 
def intro():
  name = input("Please type in your name: ")
  age = int(input(f"Nice to meet you, {name}! How old are you? "))
  if age < 30:
    print(f"Oh to be {age} years old! How can I help you today?")
  elif age < 55:
    print(f"Still in your prime at {age} years old! How can I help you today?")
  else:
    print(f"Must feel great to be alive at {age}! How can I help you today?")


def options():
  print("""Please choose from the following options:
  1. How to rename a file?
  2. How to delete a file?
  3. How to create a file?
  4. Exit the conversation
  """)
  choice = int(input ("Please type in the number of your choice: "))
  if choice == 1:
    print("To rename a file, please press on the '...' and select rename file. It will open a new window where you can type in the new name for the file.")
    print()
    options()
  elif choice == 2:
    print("To delete a file, please press on the '...' and select delete file. It will delete the file.")
    print()
    options()
  elif choice == 3:
    print("To create a file, loacted at the bottom right of the page there is a create new file option. Select it and a new file will be created.")
    print()
    options()
  elif choice == 4:
    print("Thank you for your time. Have a great day!")
  else:
    print("Please type in a number from 1 to 4")
    options()

print("Welcome to the Elite 101 chatbot!!!")
intro()
options()
