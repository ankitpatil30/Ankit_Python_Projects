# TASK FIVE
# FILE HANDLING AND EXCEPTION HANDLING
# 4.Create a login page backend to ask users to enter the username and password.
# Make sure toask for a Re-Type Password and if the password is incorrect give chance
# to enter it again but itshould not be more than 3 times.
#
try:
    a = 0
    print("User Login Page")
    un = input("Username: ")
    pwd1 = input("Password: ")

    while(un != "ankitpatil" and pwd1 != "Nagato"):
        print("User Login Page")
        un = input("Username: ")
        pwd1 = input("Password: ")
        a += 1
        if a == 2:
            raise ValueError
            break
    print("Login Successful")
except ValueError:
    print("you've exceeded the limit of attempts")

