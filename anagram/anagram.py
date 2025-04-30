def build_counter(s): 
    counter = { }
    for char in s: 
        if char in counter: 
            counter[char] += 1
        else: 
            counter[char] = 1
    return counter
def is_anagram( s:str, t:str) -> bool: 

    if len(s) != len(t): 
        return False 
    counter_s = build_counter(s)
    counter_t = build_counter(t)

    for char in s: 
        if counter_s[char] != counter_t.get(char,0):
            return False
    return True
print(is_anagram("tea",'aie'))

# shotcut is to directly check , counter(s) == counter(t)
    

