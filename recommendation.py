def main():
    difficulty = input("Enter difficulty level (Easy, Medium, Hard): ").strip().lower()
    if not (difficulty in ["easy", "medium", "hard"]):
      print("Invalid difficulty level. Please choose from Easy, Medium, or Hard.")
      return

    players = input("Single-player or Multiplayer? (S/M): ").strip().lower()
    if players not in ["s", "m"]:
        print("Invalid choice. Please enter 'S'for Single-player or 'M' for Multiplayer. ")
        return

    if difficulty == "easy":
        if players == "s":
            recommend("Stardew Valley")
        else:
            recommend("Among Us")

    elif difficulty == "medium":
        if players == "s":
            recommend("Hollow Knight")
        else:
            recommend("Team Fortress 2")

    elif difficulty == "hard":
        if players == "s":
            recommend("Dark souls III")
        else:
            recommend("Call of Duty: Warzone")
        

def recommend(game):
    print("Based on your choices, we recommend you play", game)

main()