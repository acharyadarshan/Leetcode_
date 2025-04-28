# The problem is given a set of numbers 1 to n, where the constraint for n could be up to 10^9
# we are trying to find the missing positive number and return it 
# For example, [3,-1,1,4] , return 2 , -1 is invalid and 2 is missing to make it 1,2,3,4

# O(n) run time, O(n) space 
# The logic is increment from 1 to n, lets say if you increment to 2 and cant find 3 in set, that means 3 is missing

def smallest_positive(nums)->int: 
    nums= set(nums) # gives 0(1) lookkup
    smallest = 1
    while smallest in nums:
        smallest += 1
    return smallest

print(smallest_positive([3,-1,1,4]))

# Now lets do with 0(1) space, 
# The logic is for a number 4, its index should be at 3 in a list, so for number n , its index is at n-1 
# We will basically swap the position of number 4 to it's index 3, so that way
# every number will be at its true index, 4 at 3, 2 at 1 and so on
# Then, we will check if nums[i] = i+1, say when we are at i = 3( positon 3) nums[3] should be 
# equal to 4, so the condition check is nums[i] = i+1

def smallest_positive( nums): 
    n = len(nums)
    for i in range(n): 
        # ignore negatives and zero and no need swapping if num already in right position, say nums[i]= 3, it should be at 2, if it is: no swap
        while 1<= nums[i] <= n and nums[nums[i] -1] != nums[i]: 
            correct_idx = nums[i] -1
            nums[i], nums[correct_idx] =  nums[correct_idx],nums[i]

    for i in range(n): 
        if nums[i] != i +1: # after swap,say nums[1] must hold 2, if 2 is missing then we should return 2
            return i+1
        
    return n+1 # if all numbers are correctly place [1,2,3] then missing is 4, n+1

print(smallest_positive([3,-1,1,4]))

    