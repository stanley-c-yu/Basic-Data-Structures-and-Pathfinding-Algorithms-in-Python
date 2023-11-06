class Stack: 
    # Stacks are a LIFO (last-in, first out) object.  Think of them like accessing a stack of books.  
    def __init__(self): 
        self.items = [] 

    def is_empty(self):
        #return len(self.items) == 0 
        return not self.items # empty lists evaluate as false.  This syntax is more Pythonic.  
    
    def push(self, item): 
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self): 
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self): 
        #__str__ enables us to use the print statement to inspect our stack
        return str(self.items)
    
#  Defining __str__() at the end of the class allows us to print out our stack object 
# and examine it.  If not, we'll just get a reference to the object and its location in 
# memory.  The if statement below basically says we should only run the following code
# if it is called in our main file (ie, the one where the stack class was defined.)
if __name__ == "__main__": 
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(3)
    print(s)
    s.push(7)
    s.push(5)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s.size())