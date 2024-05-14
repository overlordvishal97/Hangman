import random
from replit import clear
from hangman_art import stages, logo
from hangman_words import word_list

def choose_word():
    """Randomly choose a word from the word list."""
    return random.choice(word_list)

def initialize_display(word_length):
    """Create a list of underscores representing the word to guess."""
    return ['_'] * word_length

def print_game_state(display):
    """Print the current state of the guessed word display."""
    print(' '.join(display))

def game():
    chosen_word = choose_word()
    word_length = len(chosen_word)
    display = initialize_display(word_length)
    lives = 6
    end_of_game = False

    print(logo)
    print(f'Pssst, the solution is {chosen_word}.')  # Testing line to be removed in production

    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        clear()

        if guess in display:
            print(f"You have already guessed {guess}, try another letter")

        if guess in chosen_word:
            for position, letter in enumerate(chosen_word):
                if letter == guess:
                    display[position] = letter
        else:
            print(f"You have guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                print("You lose.")
                end_of_game = True

        print_game_state(display)

        if '_' not in display:
            print("You win.")
            end_of_game = True

        print(stages[lives])

if __name__ == "__main__":
    game()
