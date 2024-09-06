weather = input("Is it raining? (yes/no): ").strip().lower()

if weather == "yes":
    print("You should take an umbrella.")
else:
    print("No need to take an umbrella.")

mood = input("Are you feeling productive? (yes/no): ").strip().lower()

if mood == "yes":
    print("You should study!")
else:
    print("You can play a game, but don't forget to study later!")
