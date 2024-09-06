# you should take an umbrella or not based on the weather:
weather = input("Is it raining? (yes/no): ").strip().lower()

if weather == "yes":
    print("You should take an umbrella.")
else:
    print("No need to take an umbrella.")

mood = input("Are you feeling productive? (yes/no): ").strip().lower()

# you decide whether to study or play a game:
if mood == "yes":
    print("You should study!")
else:
    print("You can play a game, but don't forget to study later!")

# whether you should say "I love you" to someone:
confidence = input("Are you sure about your feelings? (yes/no): ").strip().lower()
timing = input("Is it the right time? (yes/no): ").strip().lower()

if confidence == "yes" and timing == "yes":
    print("You should tell him 'I love you'!")
else:
    print("Maybe wait for a better moment or think more about your feelings.")
