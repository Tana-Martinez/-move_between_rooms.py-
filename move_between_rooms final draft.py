rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

# Player's starting room
current_room = "Great Hall"

# Instructions
print("Dragon Text Game")
print("Commands:")
print("  go north")
print("  go south")
print("  go east")
print("  go west")
print("  exit")

# Gameplay loop
while current_room != "Exit":
    # Player's status
    print("\nYou are in the", current_room)

    # Command from player
    command = input("Enter your move: ").lower()

    # Exit command
    if command == "exit":
        current_room = "Exit"

    # Movement command
    elif command.startswith("go "):
        direction = command[3:]

        # Check if direction is valid
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way!")

    # Invalid command
    else:
        print("Invalid command!")

print("Thanks for playing!")
