#TASK TWO
#OPERATORS AND DECISION MAKING STATEMENT
#11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
#the while loop so that users do not have to continue guessing after they found the number. If the user
#does not guess the number at all, print “Sorry but that was not very successful”.

counter = 2
luckyNumber = 25
while counter <= 6:
    guess = int(input("Guess the lucky number: "))
    if guess == luckyNumber:
        print("Good guess")
        break
    else:
        print("Guess", counter)
    counter += 1
    if counter == 7 and guess != luckyNumber:
        print("Sorry but that was not very successful")
        break