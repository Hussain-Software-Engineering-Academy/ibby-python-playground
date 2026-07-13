while True:
    print("=== GAME MENU ===")
    print("1. Start Game")
    print("2. View Instructions")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        print("Starting the game...")
    elif choice == "2":
        print("Choose an option by typing 1, 2, or 3.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
    print()