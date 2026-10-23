# 3-Digit Code Guessing Game

A Python game where the computer makes a secret 3-digit code (from 100 to 999) and you try to crack it. After every guess, the game tells you which digits are in the correct position.

## Features
- Position hints: "First position is correct", "Second position is correct", "Third position is correct". If two or three digits are right, you see all of those hints.
- Counts your guesses and tells you how many it took
- Only accepts exactly 3 digits, so wrong input does not crash the game
- After 20 guesses it asks if you want to give up, and then shows the code. It asks again every 5 guesses.
- Play again with a new secret code

## How to run
You need Python 3. In a terminal:

```
python guess_3_digit_number.py
```

## Sample run
In this round the secret code is 983.

```
Let's Play
Enter 3 digit number: 12
Please enter exactly 3 digits.
Enter 3 digit number: 500
Try again
Enter 3 digit number: 910
First position is correct
Enter 3 digit number: 983
You won in 3 guesses!
Do you want to play again? (yes/no): no
Thanks for playing
```

## Concepts used
- `random.randint()` to make the code
- Strings: indexing and comparing characters
- `while` loops and functions
- Lists and input checking
