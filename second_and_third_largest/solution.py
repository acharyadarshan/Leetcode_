nums = [3,5,7,1,9]    

def second_largest(nums): 
    seond = first =  float('-inf')
    for num in nums: 
        if num > first: 
            second = first
            first = num
        elif second < num < first: 
            second = num
    return second
            
def second_and_third(nums): 
    third = second = first = float('-inf')
    for num in nums: 
        if num > first: 
            third = second
            second = first
            first = num   
        elif second < num < first: 
            third = second 
            second = num 
        elif third < num < second: 
            third = num
        
    return second, third

print( second_and_third(nums))


# the most clean way
def another_way(nums): 
    third = second = first = float('-inf')
    seen = set()
    for num in nums: 
        if num in seen: 
            continue
        seen.add(num)
        if num > first: 
            second = first
            first = num 
        elif num > second: 
            third = second
            second = num 
        elif num > third: 
            third = num
    return second,  third