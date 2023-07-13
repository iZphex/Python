import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]

# Randomly select a word from the list
chosen_word = random.choice(word_list)
# Create lives var to keep track of num of lives
lives = 6
# Create an empty List called display
# For each letter in chosen word, add "_" to display
display = []
word_length = len(chosen_word)  # create variable easier to ready
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    # Ask user to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the letter is in the word
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    # If guess not a letter in word, reduce lives by 1
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    # Join all elements in list and turn into a string
    print(f"{''.join(display)}")
    # Check if user got all letters
    if "_" not in display:
        end_of_game = True
        print("You won!")
    # Print art from 'stages'
    print(stages[lives])
