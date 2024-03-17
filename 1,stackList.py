class stack:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        Values = self.list.reverse()
        Values = [str(x) for x in self.list]
        return '\n'.join(Values)
    
    def isEmpty(self):
        if self.list ==[]:
            return True
        else:
            return False
        
    def push(self, value):
        self.list.append(value)
        return "the element has been successfully inserted"
    
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
        
        

customStack = stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack.pop())