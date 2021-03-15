#TASK TWO
#OPERATORS AND DECISION MAKING STATEMENT
#10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,such as
#counter=1
#While counter <= 5:
#print(“Type in the”, counter, “number”
#counter=counter+1
#The program asks for five guesses (no matter whether the correct number was guessed or not). If the
#correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
#After the fifth guess it stops and prints “Game over!”.

counter = 2
luckyNumber = 25
while counter <= 6:
    guess = int(input("Guess the lucky number: "))
    if guess == luckyNumber:
        print("Good guess")
    else:
        print("Guess", counter)
    counter += 1
    if counter == 7:
        print("Game over")
        break
