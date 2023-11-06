import heapq

class PriorityQueue: 
    def __init__(self):
        self.elements = [] 

    def is_empty(self):
        return not self.elements 
    
    def put(self, item, priority): 
        # pushes elements into the priority queue in such a way that it 
        # preserves the required ordering of our priority queue so that we 
        # will always be able to access the minimum value 
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]
    
    def __str__(self): 
        return str(self.elements)
    
if __name__ == "__main__":
    pq = PriorityQueue()
    print(pq)
    print(pq.is_empty())

    # item, priority 
    pq.put("eat", 2)
    pq.put("code", 1)
    pq.put("sleep", 3)

    # we can always gurantee that the first value will have the highest priority, but the same 
    # can't be said for everything else necessarily.
    print(pq)

    print(pq.get())
    print(pq.get())
    print(pq.get())

    print(pq)
