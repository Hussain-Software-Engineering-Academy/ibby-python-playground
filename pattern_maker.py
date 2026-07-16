rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
character = input("What character would you like to use? ")

for row in range(rows):
    for column in range(columns):
        print(character, end="")
    print()