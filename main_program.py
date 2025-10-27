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


