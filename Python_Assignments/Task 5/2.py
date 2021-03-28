# TASK FIVE
# FILE HANDLING AND EXCEPTION HANDLING
# 2. Write a program in Python to allow the user to open a file by using the argv module.
# If the entered name is incorrect throw an exception and ask them to enter the name again.
# Make sure to use read only mode.



# a = open("nagato.txt", 'w')
# a.write("Justice comes from vengeance but that justice only breeds more vengeance - Nagato Uzumaki")
# b.close()
#
# b = open("Jiraiya.txt", 'w')
# b.write("The True Measure Of A Shinobi Is Not How He Lives, But How He Dies.")
# b.close()

from sys import argv
try:
    while True:
        pythonFile, nagato = argv
        print("Python File - ", pythonFile)
        print("Nagato's speech - ", nagato)
        a = open(nagato, 'r')
        speech = a.read()
        print(speech)
        a.close()
        break
except:
    print("Wrong filename, Enter the name again.")


