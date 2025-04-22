

# brute force , time complex

def lenOfLongestSubstring(s): 
    result = 0
    n = len(s)
    seen = set()
    for  i in range(n): 
        for j in range(i,n):
            if s[j] in seen: 
                break
            seen.add(s[j])
            result = max(result, j - i +1)
    return result

print(lenOfLongestSubstring('abcbba'))

# sliding window

def lenOfLongestSubstring(s): 
    n = len(s)
    left = 0 
    result = 0
    seen = set()
    for right in range(n-1): 
        while s[right] in seen: 
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        result = max(result, right - left +1)
    
    return result 
        
# sliding window optimized
def lenOfLongestSubstring(s): 
    char_index = {}
    left = 0
    result = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1  # jump past the last seen duplicate
        char_index[char] = right
        result = max(result, right - left + 1)

    return result


