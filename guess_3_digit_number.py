import random

while True:
    code = str(random.randint(100,999))
    print("Let's Play")

    f = s = t = i = 0

    while True:
        num = input("Enter 3 digit number: ")
        i += 1
        f += 1
        s += 1
        t += 1

        if num == code:
            print("You won")

            again = input("Do you want to play again? (yes/no): ")
            if again.lower() == "yes":
                break
            else:
                exit()

        elif num[0] == code[0]:
            print("First position is correct")


            if f > 20:
                tried = input("You wanna give up? (yes/no): ")
                if tried.lower() == "yes":
                    print("The code was:", code)

                    again = input("Do you want to play again? (yes/no): ")
                    if again.lower() == "yes":
                        break
                    else:
                        print("Thanks for playing")
                        exit()

        elif num[1] == code[1]:
            print("Second position is correct")


            if s > 20:
                tried = input("You wanna give up? (yes/no): ")
                if tried.lower() == "yes":
                    print("The code was:", code)

                    again = input("Do you want to play again? (yes/no): ")
                    if again.lower() == "yes":
                        break
                    else:
                        exit()

        elif num[2] == code[2]:
            print("Third position is correct")


            if t > 20:
                tried = input("You wanna give up? (yes/no): ")
                if tried.lower() == "yes":
                    print("The code was:", code)

                    again = input("Do you want to play again? (yes/no): ")
                    if again.lower() == "yes":
                        break
                    else:
                        exit()

        else:
            print("Try again")

            if i > 20:
                tried = input("You wanna give up? (yes/no): ")
                if tried.lower() == "yes":
                    print("The code was:", code)

                    again = input("Do you want to play again? (yes/no): ")
                    if again.lower() == "yes":
                        break
                    else:
                        exit()