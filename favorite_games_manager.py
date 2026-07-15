favorite_games = [
    "Minecraft",
    "FIFA 26",
    "Mortal Kombat 1"
]
while True:
    print ("===== Favorite Games =====")
    print ()

    print ("1. View Games")
    print ("2. Add Games")
    print ("3. Remove Game")
    print ("4. Replace Game")
    print ("5. Exit")
    user_choice = input ("What would you like to do? (Pick a number from 1-5) ")
    print ()
    if user_choice == "1":
        for game in favorite_games:
            print (game)
            print()
    elif user_choice == "2":
        game_add = input ("What game would you like to add? ")
        if game_add in favorite_games:
            print ("Game already added.")
            print ()
        else:
            favorite_games.append(game_add)
            print (f"Added {game_add}")
            print ()
    elif user_choice == "3":
        game_remove = input ("What game would you like to remove? ")
        if game_remove in favorite_games:
           favorite_games.remove(game_remove)
           print (f"{game_remove} removed.")
           print ()
        else:
            print ("Game not found.")
            print()
    elif user_choice == "4":
        game_to_replace = int(input("Which game number do you want to replace? "))
        game_to_replace = game_to_replace - 1

        if game_to_replace >= 0 and game_to_replace < len(favorite_games):
            game_replace = input("What should replace it? ")
            favorite_games[game_to_replace] = game_replace
            print("Game replaced.")
        else:
            print("Invalid game number.")
            print()
    elif user_choice == "5":
        print ("Goodbye!")
        print()
        break
    else:
        print ("Invalid choice. Pick a number from 1-5. ")

print ()