from word_game import ExtendedWordGame
from file_io import load_words

def run_game(game):
    #Run game, and prompt a guess
    print("Welcome to the Word guessing game!")
    while True:
        guess = input("Enter your guess: ")
        if game.guess_word(guess):
            print(f"Congractulations! You have guesses the word '{game.current_word}' in {game.attempt} attempts.")
            break
        else:
            print("Incorrect guess. Try again.")
            print(game.provide_hint())

if __name__ == "__main__":
    words = load_words('words.txt')
    game = ExtendedWordGame(words)
    run_game(game)
    