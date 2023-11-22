from command_utils import *

print("Welcome to the sensitivity test program:🎉")
print("The following commands are available for use")
print("""
    START - TO START THE PROGRAM     - ▶
    QUIT - TO QUIT THE PROGRAM       - 🛑
    RESTART - TO RESTART THE PROGRAM - 🔁
""")

while True:

    new_command = input("Enter a command >>  ").strip().lower()
    if check_command_validity(new_command):
        formatted_command = new_command.upper()
        if formatted_command == "START":
            print("Start")
            start_program()
        elif formatted_command == "QUIT":
            print("Program exit...")
            break
        elif formatted_command == "RESTART":
            print("Restart")
    else:
        print("Invalid command")
