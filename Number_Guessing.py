import random  #using random module will let us genterate random numbers
import math     #using mathh module will let us utilize math functions
def play(chances):
    guess=random.randint(1,100) #specifying range of randint function
    for i in range(chances):
        a=int(input("Enter a guess(1-100):  "))
        if guess==a:
            print("correct guess.")
            return i+1
        else:
            temp="Your guess is higher then actual."
            if guess>a:
                temp="Your guess is lesser than actual."
            print("Wrong guess")
            print("Hint :"+temp)
    return i+1
def score(name,tries,chances):
    result=str(math.ceil(((chances-tries)/chances)*100))
    print(name+"\nYour score is "+result)


print("***** WELCOME TO GUESSING THE GAME *****")
print("****INSTRUCTIONS TO PLAY THE GAME****")
print("""THE PLAYER HAVE TO GUESS A NUMBER WHICH IS IN BETWEEN 1 T0 100 
THEN CHANCES ARE GIVEN TO THE USER THEN THE USER HAVE TO GUESS A NUMBER
USING HINTS GIVEN AT WRONG GUESSES.
ONE MUST GUESS THE NUMBER IN THE GIVEN NUMBER OF CHANCES OR THE PLAYER WILL BE LOST
IF THE PLAYER IS ABLE TO GUESS THE NUMBER IN THE GIVEN RANGE OF CHANCES THEN THE SCORE IS AWARDED TO THE PLAYER
""")

choice=input("PRESS P TO START THE GAME OR PRESS Q TO QUIT THE GAME. ")
if choice=='p' or choice=='P':
    name=input("ENTER YOUR NAME: ")
    tries=play(10)  #Calculates numbers tries user took to guess the answer
    score(name,tries,10) #Calculates the score user scored
else:
    print("Game is over,see u again")
    exit()
