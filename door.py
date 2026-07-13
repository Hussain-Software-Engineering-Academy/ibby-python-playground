print("You are standing in front of two doors.")
print()
print("1. Left")
print("2. Right")
print()
print()
choice = input("Which door do you choose? ")
if choice == "1":
    print("You found a treasure chest filled with gold!")
elif choice == "2":
    print("You woke up a sleeping red dragon!")
else:
    print("Invalid choice! Try again.")
print()