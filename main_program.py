<<<<<<< HEAD
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
=======
<<<<<<< HEAD
if _name_ == "_main_":
    # Show intro
    show_intro()

    # Get user input
    name, age = get_user_info()

    # Convert to binary
    name_binary = convert_to_binary(name)
    age_binary = convert_to_binary(age)

    # Create final message
    final_message = create_message(name, age, name_binary, age_binary)

    # Display and save message
    print(final_message)
    save_message(final_message)

    # Read and display saved file
    print("\nReading saved message from file:")
    read_message()

    # Show exit message
    show_exit_message()


=======
def save_message(message):
    try:
        with open("user_message.txt", "w") as file:
            file.write(message)
        print("Message saved successfully.")
    except Exception as e:
        print(f"Error saving message: {e}")

def read_message():
    try:
        print("Reading saved message...")
        with open("user_message.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("No saved message found.")
    except Exception as e:
        print(f"Error reading message: {e}")
>>>>>>> 5d4da82bbf73af157750740f66b1945592416ca2
>>>>>>> 875900d8894e52eff9e0b2c80376ab59ce4f0a3f
