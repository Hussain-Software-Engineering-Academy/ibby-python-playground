while True:
    user_input = input("Say something: ")
    if user_input.strip() == "":
        print("You didn't type anything.")
    elif user_input == "quit":
        print("Goodbye!")
        break
    else:
        print(f"You said: {user_input}")