
import random
randNo=random.randint(1 , 10)
print(randNo)
userGuess = None
guesses = 0

while(userGuess != randNo ):
  userGuess = int(input("enter your guess: "))
  guesses += 1
  if(userGuess==randNo):
    print("you guessed it right")
  else:
    if(userGuess>randNo):
      print("you guessed it wrong guess a smaller number")
    else:
        print("you guessed it wrong guess a higher number")
      


print("you guessed the number in {guesses} guesses")
