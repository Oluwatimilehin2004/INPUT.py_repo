Welcome! This is a simple Python program that collects your name and age, converts them into **binary, saves the information to a file, and reads it back. It’s interactive, fun, and a little geeky.

---

## Features 

- Friendly intro and exit messages to make the program welcoming.
- Input validation for name and age:
  - Name cannot be empty.
  - Age must be a number.
- Converts your name and age into binary.
- Saves your binary message into a file (user_message.txt) and reads it back.
- Handles file errors gracefully.

---

## Files 

- main.py → The main program that runs everything.  
- greetings.py → Displays friendly introduction and exit messages.  
- file_manager.py → Handles saving and reading messages to/from a file.  
- convert_to_binary.py (or inside main) → Converts strings and numbers to binary.

---

## How to Use 

1. Run main.py:

bash
python main.py
2. Follow the prompts:
 -Enter your name.
 -Enter your age.

3. See your binary information displayed on the screen.
4. Your message will also be saved to user_message.txt.
5. The program reads back the saved message for you.
6. Exit gracefully with a friendly goodbye message.

Example Run 
==============================
 Welcome to the User Info Program 
==============================

Enter your name: Ayomide
Enter your age: 18

bash
Binary Name: 01000001 01111001 01101111 01101101 01101001 01100100 01100101
Binary Age: 10010
 Message has been saved successfully.

Reading saved message from file:
 Saved message:
Binary Name: 01000001 01111001 01101111 01101101 01101001 01100100 01100101
Binary Age: 10010

Thank you for using the program. Goodbye!
```
Why This is Fun 

Not only does it teach basic Python concepts like loops, functions, and file handling, it also gives a sneak peek into how computers "see" text and numbers in binary. Plus, it's interactive; you're part of the program!

Enjoy & Experiment

Try typing different names and ages.

Modify the program to append messages instead of overwriting.

Explore more binary fun, maybe even convert messages back to text!