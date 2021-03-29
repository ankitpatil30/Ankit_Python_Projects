# TASK SEVEN
# CLASSES AND OBJECTS
# 3. Create a class to find three elements that sum to zero from a set of n real numbers
# Input array:[-25,-10,-7,-3,2,4,8,10]
# Expected output:[[-10,2,8],[-7,-3,10]]

class zerosum:
    def sumofthree(self, arr):
        zero = []
        for i in arr:
            for j in arr:
                for k in arr:
                    if (i+j+k) == 0:
                        b = [i,j,k]
                        b.sort()
                        if b not in zero:
                            zero.append(b)
        print(zero)

x= [-25,-10,-7,-3,2,4,8,10,5,7,-5]
zerosum().sumofthree(x)


# import itertools
# stuff = [-1, 0, 1, 2, -1, -4]
# stuff.sort()
# ls = []
# for subset in itertools.combinations(stuff, 3):
#     if sum(list(subset))==0:
#         # first I have sorted the list because of grouping
#         # Ex: [-1, 0, 1] and [0, 1, -1] are build with the same element
#         # so here is avoiding this.
#         if list(subset) not in ls:
#             ls.append(list(subset))
# print(ls)

