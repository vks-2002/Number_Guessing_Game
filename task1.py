import random
import sympy
#
# def is_prime(n):
#     if sympy.isprime(n):
#         result = " Guessed number is a Prime Number"
#     else:
#         result = " Guessed number is  not a Prime Number"
#     return result
#
# def even_odd(n):
#     if n % 2 == 0:
#         even_result = "Guessed number is an Even Number"
#     else:
#         even_result = "Guessed number is not an Even Number"
#     return even_result
#
# def multiples(n):
#     if n % 5 == 0:
#         result = "Guessed number is a multiple of 5"
#     else:
#         result = "Guessed number is not a multiple of 5"
#     return result


print("/***************************NUMBER GUESSING GAME******************************/")
print("You will get 10 chances to guess the correct number.")
print("Enter\n1. Starting the game.\n2. Quit.\n")
enter = int(input())
if enter == 1:
    while (True):
        guess_number = random.randint(1, 100)
        for i in range(0, 11):
            print("Enter the number you guessed: ")
            user_number = int(input())
            if guess_number == user_number:
                print("Your Guess is correct!!!!!!")
                exit()
            else:
                chances = 0
                x = random.randint(1, 3)
                if x == 1:
                    if sympy.isprime(guess_number):
                        print(" Guessed number is a Prime Number")
                        chances += 1
                        if chances > 10:
                            break
                    else:
                        print(" Guessed number is  not a Prime Number")
                        chances += 1
                        if chances > 10:
                            break
                elif x == 2:
                    if user_number > guess_number:
                        print("Number is less than your guess ")
                        chances += 1
                        if chances > 10:
                            break
                    else:
                        print("Number  is greater than your guess")
                        chances += 1
                        if chances > 10:
                            break
else:
    print("You have exited the Game.")
    exit()