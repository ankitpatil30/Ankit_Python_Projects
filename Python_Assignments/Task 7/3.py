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

# class py_solution:
#  def threeSum(self, nums):
#         nums, result, i = sorted(nums), [], 0
#         while i < len(nums) - 2:
#             j, k = i + 1, len(nums) - 1
#             while j < k:
#                 if nums[i] + nums[j] + nums[k] < 0:
#                     j += 1
#                 elif nums[i] + nums[j] + nums[k] > 0:
#                     k -= 1
#                 else:
#                     result.append([nums[i], nums[j], nums[k]])
#                     j, k = j + 1, k - 1
#                     while j < k and nums[j] == nums[j - 1]:
#                         j += 1
#                     while j < k and nums[k] == nums[k + 1]:
#                         k -= 1
#             i += 1
#             while i < len(nums) - 2 and nums[i] == nums[i - 1]:
#                 i += 1
#         return result

# print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))
