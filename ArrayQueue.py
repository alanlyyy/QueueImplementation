"""
FIFO Queue array implementation, with a set length feature.

Instance variables:
self._data - stores the actual list
self._size - store the size of the list
self._front - store front index

methods:
peek - return element in front of the list
dequeue - remove the first element in the list
enqueue - add element to back of the list
__len__  - returns size of list
is_empty - checks if list is empty
resize - changes the length of the list

Alan Ly 09-28-19
"""


class Empty(Exception):
    """when peek of dequeue is called and the number of elements is 0, raise an exception"""
    pass
    
class Resize(Exception):
    """raise an exception when trying to resize a list smaller than current size"""
    pass


class ArrayQueueClass:
    """FIFO queue implementation using a python list
    as underlying storage"""
    
    def __init__(self,size=10):
        
        #stores the data of the queue
        self._data = [None]*size
        
        #contains the size or number of data in the queue
        self._size = 0
        
        #stores the index of the front of the queue
        self._front = 0
        
    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size
        
    def is_empty(self):
        """Return true if the queue is empty."""
        return self._size == 0
        
    def peek(self):
        """Return 1st element at front of queue without removing"""
        if self.is_empty():
            raise Empty("Queue is empty")
            
        return self._data[self._front]
    
    def dequeue(self):
        """Remove and return the 1st element of the queue (FIFO)
        Raise empty exception when queue is empty"""
        
        if self.is_empty():
            raise Empty("Queue is empty")
            
        #store first element in the in the queue
        answer = self._data[self._front]
        
        #clear the first element in the queue
        self._data[self._front] = None
        
        #advance the first position of the queue
        self._front = (self._front + 1) %len(self._data) #ex) (0 + 1)% 8 = 1 , (2+1) % 8 = 3
        
        #decrease the size counter
        self._size -= 1
        
        return answer
        
    def enqueue(self,item):
        """Add an element to the back of the queue"""
        
        if self._size == len(self._data):
            self._resize(2* len(self.data)) #double the array size
            
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = item
        self._size += 1
        
    def _resize(self,newLength):
        """resize to a new list of newlength >= len(self._data) Assuming newLength > len(self._data)
        """ 
        
        #throw an except if resizing to smaller list
        if newLength < len(self._data):
            raise Resize('Cannot resize to a smaller list')
        
        #save old data front list
        old = self._data
        
        #clear the existing list and update with new length
        self._data = [None] * newLength
        
        #store the front of the list
        oldFront = self._front
        
        
        for newposition in range(self._size):
        
            #shift indices of old items to new list
            self._data[newposition] = old[oldFront]
            oldFront = (1 + oldFront) % len(old)
        
        self._front = 0
        

if __name__ == "__main__":
    
    queue = ArrayQueue(7)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    print("Current length of queue:" ,queue.__len__()) #7
    print("Contents of queue:", queue._data) #1234567
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print("Current length of queue:" ,queue.__len__()) #4
    print("Contents of queue:", queue._data) #4567
    print("Peek:" , queue.peek()) #4
    
    queue._resize(14)
    print("Current length of queue:" ,queue.__len__()) #4
    print("Contents of queue:", queue._data) #4567
    
    
    queue._resize(3) #throws an exception