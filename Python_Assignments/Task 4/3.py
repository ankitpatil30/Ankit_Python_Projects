# TASK FOUR
# TRADITIONAL FUNCTIONS,ANONYMOUS FUNCTIONS &
# HIGHER ORDER FUNCTIONS
# 3. Create a function that takes a list and returns a new list with unique elements of the first list.

def unique(list1):
    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
z = [1,1,12,3,4,5,6,7,8,9,10,20,40,30,44,44,55,110,110,220,550,9,8,7,6,5,4,3,2,1,660,880,110,440,550,220]
y = unique(z)
print(y)