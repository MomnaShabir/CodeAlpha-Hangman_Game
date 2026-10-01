import random

words = ["scope", "career", "startup", "product", "worker"]

word = random.choice(words)
guessed_letters = set()
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman!")
print("Guess the secret word one letter at a time.")

while wrong_guesses < max_wrong_guesses:

    # Display the word with unguessed letters hidden
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", " ".join(display_word))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    # Check the guess
    if guess in word:
        print("Good guess!")

    else:
        wrong_guesses += 1
        print("Wrong guess!")

    # Check if the whole word has been guessed
    if all(letter in guessed_letters for letter in word):
        print("\nYou win!")
        print("The word was:", word)
        break

else:
    print("\nGame over!")
    print("The word was:", word)
       
        