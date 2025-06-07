

def bubble_sort(arr): 
    n = len(arr)
    for i in range(n -1):
        for j in range(n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([1,4,5,3,2]))


def selection_sort(arr):
    n = len(arr)
    for i in range(n-1): 
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([1,4,5,3,2]))


def merge_sort(arr):

    if len(arr) <= 1: 
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right): 
    i = j = 0
    result = []

    while i < len(left) and j< len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else: 
            result.append(right[j])
            j += 1

    while i < len(left): 
        result.append(left[i])
        i += 1

    while j< len(right): 
        result.append(right[j])
        j += 1

    return result   
    

print(merge_sort([1,4,5,3,2]))


nums = [1,3,4,6,9,0, 10, 20,30 ]

#res = [x**2 if x%2 == 0 else x for x in nums]

#if branching in nested if else

res = [ x**2 if x%10 == 0 else x**1 if x%2 == 0 else x for x in nums]

print(res)

def quick_sort(arr): 
    if len(arr) <= 1: 
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x<= pivot]
    right = [x for x in arr[1:] if x > pivot]
    # alternate, middle = [ x for x in arr if x == pivot]
    # others list comprehesnion same with arr
    # pivot = len(arr)//2

    return quick_sort(left) + [pivot] + quick_sort(right)



#[expression for row in matrix for item in row if condition]
# the if here is for item 



