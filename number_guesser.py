import random

def main():
    print ("Hello World")
    number = random.randint(1, 100)
    guesses = 0
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        guesses += 1
        try:
            if guess < 1 or guess > 100:
                raise ValueError("Guess has to be between 1 and 100")
            elif guess < number:
                print ("Try again! Your guess was too low.")
            elif guess > number:
                print ("Try again! Your guess was too high.")
            else:
                print ("Congratulations! You guessed the number in %d tries." % guesses)
                return False
        except ValueError as e:
            print(e)
            continue

if __name__ == "__main__":
    main()