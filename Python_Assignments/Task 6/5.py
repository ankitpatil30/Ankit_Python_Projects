# TASK SIX
# GENERATORS, LIST COMPREHENSION AND DECORATORS
# 5.Write an example on decorators.

def employeeDetails(emp):
    def internalDetails():
        print("Employee FirstName and LastName : ")
        emp()
        print("Employee ID: 944456 ")
    return internalDetails()
@employeeDetails
def ename():
    fname = 'ankit'
    lname = 'patil'
    print(fname,lname)

