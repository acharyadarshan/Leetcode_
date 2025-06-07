def fizzBuzz(self, n: int) -> List[str]:
    result = []
    for i in range(1, n+1): 
        if i % 15 == 0: 
            result.append('FizzBuzz')
        elif i % 3 == 0: 
            result.append("Fizz")
        elif i % 5 == 0: 
            result.append("Buzz")
        else: 
            result.append(str(i))
            
    return result


def opimize_fizzbuzz(nums): 
    n = len(nums)
    result = []
    for i in range(1, n+1):
        output = ""
        if i % 3 == 0: 
            output += "fizz"
        if i % 5 == 0: 
            output += "buzz"
        result.append(output or str(i))


def custom_fizzbuzz( n, rules): 
    result = []
    for i in range(1, n+1): 
        output = ""
        for divisor, word in rules.items(): 
            if i % divisor == 0: 
                output += word
        result.append(output or str(i))

    return result 
