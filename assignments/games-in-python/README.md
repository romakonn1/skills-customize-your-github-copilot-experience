
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a Hangman-style word guessing game in Python while practicing string manipulation, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description

Create the game structure, choose a hidden word, and prepare the initial display state for the player.

#### Requirements
Completed program should:

- Define a list of possible words to guess
- Randomly select one word when the game starts
- Display blanks for each letter in the selected word
- Set a limited number of incorrect guesses allowed

### 🛠️ Player Input and Progress Tracking

#### Description

Allow the player to enter guesses, update the displayed word progress, and track wrong letters.

#### Requirements
Completed program should:

- Prompt the player to guess one letter at a time
- Reveal correctly guessed letters in the word display
- Record and show incorrect guesses separately
- Reduce remaining attempts for wrong guesses

### 🛠️ Win/Lose Logic

#### Description

Check the game outcome after each guess and display the appropriate end message.

#### Requirements
Completed program should:

- End the game when the word is completely guessed
- End the game when the player runs out of attempts
- Display a win message if the player guesses the word
- Display a lose message and reveal the correct word if attempts are exhausted
