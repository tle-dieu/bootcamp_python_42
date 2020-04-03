from random import randint

print("This is an interactive guessing game!\n"
      "You have to enter a number between 1 and 99"
      "to find out the secret number.\n"
      "Type 'exit' to end the game.\n"
      "Good luck!\n")
secret_nb = randint(1, 99)
try_nb = 1
while True:
    entry = input("What's your guess between 1 and 99?\n>> ")
    if entry.strip() == 'exit':
        exit("Goodbye!")
    try:
        if int(entry) == secret_nb:
            if secret_nb == 42:
                print("The answer to the ultimate question of life,"
                      "the universe and everything is 42.")
            if try_nb == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulations, you've got it!\n"
                      f"You won in {try_nb} attempts")
            break
        else:
            print("Too hight!" if secret_nb < int(entry) else "Too low!")
        try_nb += 1
    except ValueError:
        print("That's not a number.")
