import random
randNumber=random.randint(1,100)

userguess=None
guesses=0
while (userguess!=randNumber):
    userguess= int(input("Enter the number "))
    guesses+= 1
    if(userguess==randNumber):
       print("you guess right number")
    else:
       if(userguess>randNumber):
           print("please guess small")
       else:
           print("please guess larger")
print(f"your guess no. in {guesses} guesses")


with open ("sample.txt","r")as f:
        highscore =int(f.read())
if(guesses<highscore):
        print("you just broke the high score")
        with open ("sample.txt","w") as f:
            f.write(str(guesses))


