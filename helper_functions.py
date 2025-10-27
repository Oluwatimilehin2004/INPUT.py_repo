def validate_input(user_input):
    if user_input != None and user_input.isalpha():
        print("Value cannot be empty, enter your name and age.")
        return False

def convert_to_binary(text):
    if text.isdigit():
        number = bin(int(text))[2:]  # Convert age to binary
        return number

    binary= ' '.join(format(ord(char), '08b') for char in text)  # Convert name to binary
    return binary

def create_message(name, age, name_binary, age_binary):
    sentence= f"""
    Hello {name}, you are {age} years old!
    Name in binary: {name_binary}
    Age in binary: {age_binary}
    """
    return sentence
