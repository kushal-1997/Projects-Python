import random
randNumber = random.randint(1,100)
userGuess= None
guesses= 0

while(userGuess!= randNumber):
  userGuess = int(input("enter your guess : "))
  guesses += 1

  if(userGuess==randNumber):
    print("your guess is right")
  else:
      if(userGuess>randNumber):
       print("your guess is wrong! enter the smaller number")
      else:
       print("your guess is wrong! enter the larger number")
    
  if userGuess> 100:
    print("error 404")
      
print(f"you guessed the number in {guesses} guesses")
    
    