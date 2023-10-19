import string

def alphabet_game():
    alphabet = list(string.ascii_lowercase)
    player_input = ""

    for letter in alphabet:
        while True:
            player_input = input(f"Enter a word that starts with the letter '{letter}': ").lower()
            if player_input.startswith(letter):
                print(f"Good job! '{player_input}' starts with '{letter}'.")
                break
            else:
                print(f"'{player_input}' doesn't start with '{letter}'. Try again.")

    print("Congratulations! You've completed the alphabet game.")

if __name__ == "__main__":
    alphabet_game()
