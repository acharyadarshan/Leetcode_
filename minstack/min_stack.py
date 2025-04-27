

# we build two stacks, one is to track minimum at each level of other stack and
# the other is to hold values 

class min_stack: 

    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        # if minstack is empty- directly use current val, if not empty
        # then compare current minimum of stack and current value, to get minimum and append that to stack
        val = min(val, self.minStack[-1]) if self.minStack else val
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int: 
        return self.stack[-1]
    
    def getMin(self): 
        return self.minStack[-1]
    

newstack = min_stack()

newstack.push(5)
print("Current min" , newstack.getMin())

newstack.push(3)
print("Current min" , newstack.getMin())

newstack.push(-1)
print("Current min" , newstack.getMin())

    
newstack.pop()
print("Top Value", newstack.top())