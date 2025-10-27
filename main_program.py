from helper_functions import validate_input, convert_to_binary, create_message
from file_manager import save_message, read_message
from greetings import show_intro, show_exit_message

def get_user_info():
    while True:
        name = input("Enter your name: ").strip()
        if not name:
            print("Name cannot be empty. Please try again.")
            continue
        
        age = input("Enter your age: ").strip()
        if not age.isdigit():
            print("Age must be a valid number. Please try again.")
            continue

        return name, age
