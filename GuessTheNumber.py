import random

print("Number Guessing Game!")
num = random.randint(1,9) 
chances = 0
while chances < 5:
    gnum = int(input("Guess a number between 1 and 9 : "))
    if(gnum == num):
        print("Yay! you won!")
        break 
    elif(gnum < num):
        print("Too Low!")
        chances += 1
    else:
        print("Too High!")
        chances += 1
    
if not chances <5:
    print("You lose! the number is "+str(num))
    