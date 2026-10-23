import random

POSITIONS = ["First", "Second", "Third"]
GIVE_UP_AFTER = 20  # start offering "give up" after this many guesses


def play():
    """Play one round. A new secret code is chosen every round."""
    code = str(random.randint(100, 999))
    print("Let's Play")

    attempts = 0

    while True:
        num = input("Enter 3 digit number: ").strip()

        # exactly 3 digits are needed (this also stops the crash on short input)
        if len(num) != 3 or not num.isascii() or not num.isdigit():
            print("Please enter exactly 3 digits.")
            continue

        attempts += 1

        if num == code:
            print(f"You won in {attempts} guesses!")
            return

        # show a hint for every digit that is in the correct position
        hints = [f"{POSITIONS[i]} position is correct" for i in range(3) if num[i] == code[i]]
        if hints:
            for hint in hints:
                print(hint)
        else:
            print("Try again")

        # after 20 guesses, offer to give up (and again every 5 guesses)
        if attempts >= GIVE_UP_AFTER and (attempts - GIVE_UP_AFTER) % 5 == 0:
            tried = input("You wanna give up? (yes/no): ").strip().lower()
            if tried == "yes":
                print("The code was:", code)
                return


while True:
    play()

    again = input("Do you want to play again? (yes/no): ").strip().lower()
    while again not in ("yes", "no"):
        again = input("Please type yes or no: ").strip().lower()

    if again == "no":
        print("Thanks for playing")
        break
