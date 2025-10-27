def save_message(message):
    try:
        with open("user_message.txt", "w") as file:
            file.write(message)
        print("Message saved successfully.")
    except Exception as e:
        print(f"Error saving message: {e}")

def read_message():
    try:
        with open("user_message.txt", "r") as file:
            content = file.read()
            print("Reading saved message:")
            print(content)
    except FileNotFoundError:
        print("No saved message found.")
    except Exception as e:
        print(f"Error reading message: {e}")
