#wap to create a gussing game where the user has to guess a randomly generated number use branching, looping to manage the games flow
import random
a = random.randrange(1,100)
while True:
    x = int(input("Guess a number"))
    if x==a:
        print("YAY!! YOU WON, THE GUESS WAS : ",a)
        break
    elif x<a:
        print("GUESS A NUMBER GREATER THAN : ",x)
    elif x>a:
        print("GUESS A NUMBER SMALLER THAN : ",x)
