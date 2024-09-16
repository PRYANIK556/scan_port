import random

number_to_guess = random.randint(1, 100)

while True:
    guess = int(input("Угадай число от 1 до 100: "))

    if guess == number_to_guess:
        print("Поздравляем, вы угадали число!")
        break
    elif guess < number_to_guess:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")
