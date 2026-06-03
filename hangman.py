# ========================================
# HANGMAN GAME
# CodeAlpha Python Internship
# Author: Syeda Mowaddat Zahra 
# ========================================

import random
import os

# ---- HANGMAN STAGES ----
HANGMAN = [
    """
       -----
       |   |
           |
           |
           |
           |
      =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
      =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
      =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
      =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
      =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
      =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
      ========="""
]

# ---- WORD LIST ----
WORDS = [
    "python",
    "hangman", 
    "coding",
    "github",
    "internship"
]

# ---- CLEAR SCREEN ----
def clear_screen():
    os.system('clear')
    
    # ---- DISPLAY BOARD ----
def display_board(wrong, guessed, word):
    clear_screen()
    print("=" * 40)
    print("   🎮  HANGMAN GAME  |  CodeAlpha")
    print("=" * 40)
    
    # Hangman figure
    print(HANGMAN[wrong])
    
    # Word progress
    print("\n  WORD: ", end="")
    for letter in word:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    
    # Wrong letters
    print(f"\n\n  Wrong Letters: {list(guessed - set(word))}")
    print(f"  Chances Left: {6 - wrong}")
    print("=" * 40)
    
    # ---- MAIN GAME ----
def play_game():
    word = random.choice(WORDS)
    guessed = set()
    wrong = 0

    print("\n  Welcome to HANGMAN!")
    print("  CodeAlpha Internship Project\n")

    while wrong < 6:
        display_board(wrong, guessed, word)

        # Player input
        guess = input("\n  Enter a letter: ").lower()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("  !! Enter one letter only !!")
            continue

        if guess in guessed:
            print("  !! Already guessed !!")
            continue

        guessed.add(guess)

        if guess in word:
            print("  Correct!")
            # Check win
            if all(l in guessed for l in word):
                display_board(wrong, guessed, word)
                print(f"\n  YOU WIN! Word was: {word}")
                return
        else:
            wrong += 1
            print("  Wrong!")

    display_board(wrong, guessed, word)
    print(f"\n  GAME OVER! Word was: {word}")
    
    # ---- MAIN FUNCTION ----
def main():
    print("\n" + "=" * 40)
    print("   HANGMAN GAME — CodeAlpha")
    print("=" * 40)
    
    while True:
        play_game()
        
        again = input("\n  Play again? (y/n): ").lower()
        if again != 'y':
            print("\n  Thanks for playing!")
            print("  CodeAlpha Internship\n")
            break

# ---- START GAME ----
main()