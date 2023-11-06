'''
This class implements a data structure called a queue.  It's sort of the opposite of a stack.  

While a stack is a LIFO data structure, a queue is a FIFO, first-in first-out.  

It's basically like queueing up to check out at a grocery store.  
'''
# title is queue_ll becuase there's an existing queue module that we would accidentally override.  

# A deque is a data structure imported from collections library.  
# It's name is short for "double-ended queue".  We use this instead of a list to build a queue. 
# Unlike a list, it is optimized for insertions and deletions at either end.  
# Normal lists are only optimal for insertions and deletions at the end. 
# Deleting and inserting from standard lists in the front position in Python is inefficient. 
# This is because you would have to shift everything around to accomodate insertions and deletions. 
# This is a bigger deal if we expect our lists (aka our queues) to be massive.  
from collections import deque 

class Queue: 
    def __init__(self): 
        self.items = deque()

    def is_empty(self): 
        return not self.items 
        ## this is equivalent to: return len(self.items) == 0 

    def enqueue(self, item): 
        # adds an tiem
        self.items.append(item)
    
    def dequeue(self): 
        return self.items.popleft()
    
    def size(self):
        return len(self.items)
    
    def peek(self): 
        return self.items[0]
    
    def __str__(self): 
        # if we didn't have this method, then when we move to print the instance 
        # we would just get a reference to the object at the index where it is stored in memory.  
        # with this method, we get a more human-readable printout that helps us confirm the instance.  
        return str(self.items)


if __name__ == "__main__": 
    q = Queue() 
    print(q)
    print(q.is_empty())
    q.enqueue("A")
    q.enqueue("D")
    q.enqueue("F")
    print(q)
    print(q.dequeue())
    print(q.dequeue())
    print(q)
    print(q.size())
    print(q.peek())
    print(q)