# scrabble_game.py
import random
import time

# Scrabble letter values
LETTER_VALUES = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1,
    'U': 1, 'L': 1, 'N': 1,
    'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

# Dictionary for valid word check (this is a small set for demonstration)
VALID_WORDS = {"apple", "orange", "banana",
               "grape", "cabbage", "zebra", "quiz"}

def calculate_score(word):
    """Calculate the Scrabble score for a given word."""
    word = word.upper()
    score = sum(LETTER_VALUES.get(letter, 0) for letter in word)
    return score

def is_valid_word(word):
    """Check if the word is valid (present in dictionary)."""
    return word.lower() in VALID_WORDS

def get_random_word_length():
    """Generate a random word length between 4 and 7 letters."""
    return random.randint(4, 7)

def scrabble_game():
    total_score = 0
    rounds_played = 0
    max_rounds = 10

    while rounds_played < max_rounds:
        print("\n--- Scrabble Game ---")
        word_length = get_random_word_length()
        print(f"You must enter a word of exactly {word_length} letters.")

        start_time = time.time()
        word = input("Enter a word: ").strip()

        # Check word length
        while len(word) != word_length or not word.isalpha():
            print(f"Invalid input. Please enter a word with {word_length} letters.")
            word = input("Enter a word: ").strip()

        elapsed_time = time.time() - start_time

        # Check if word is valid
        if is_valid_word(word):
            score = calculate_score(word)
            # Bonus for entering faster
            bonus = max(0, int(15 - elapsed_time))
            total_round_score = score + bonus
            total_score += total_round_score
            print(f"Word '{word}' is valid! You scored {total_round_score} points this round (bonus: {bonus}).")
        else:
            print(f"Word '{word}' is not valid.")

        rounds_played += 1
        print(f"Total score so far: {total_score}")

        if input("Do you want to quit? (yes/no): ").lower() == 'yes':
            break

    print(f"Game over! Your total score is: {total_score}")

if __name__ == "__main__":
    scrabble_game()
