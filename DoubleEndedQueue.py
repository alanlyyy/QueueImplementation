"""
Double ended queue which is a comparable implementation of the collection.deque class.
DoubleEndedQueue is a subclass or extension to ArrayQueueClass.

The following instance variables are added into this class:
self._back

The following methods are added into this class:
addFront
deleteLast
peekLast
remove
rotate
count
clear

alan ly 09-28-19
"""


#ArrayQueue is a module, while ArrayQueueClass is the class we are importing from ArrayQueue.
from ArrayQueue import ArrayQueueClass

class DoubleEndedQueue(ArrayQueueClass):
    
    def __init__(self,size=10):
        
        #invoke init of parent class to inherit instance variables
        ArrayQueueClass.__init__(self,size)
        
        self._front = self._front
        self._size = self._size
        self._data = self._data
        self._back = self._front + self._size - 1 
        
        
    def addFront(self,element):
        """add an element to the front of the queue"""
        if self._size == len(self._data):
            raise Resize("Queue is full")
            
        self._size += 1
            
        #add elements to the front of the list in modulo circular shift
        self._front = (self._front - 1) % len(self._data)
        
        self._data[self._front] = element
            
    
    def deleteLast(self):
        """Delete last element from the list"""
        
        #store the index of last element
        #self._back = self._front + self._size -1 
        
        #store the last element in the queue
        temp = self._data[self._back]
        
        #clear the last element
        self._data[self._back] = None
        
        #decrease the size counter
        self._size -= 1
        
        #update the last element index
        self._back = self._front + self._size - 1
        
        return temp
        
    def peekLast(self):
        #if the last position is in the last half of the array
        if (self._front + self._size) < len(self._data):
            #return self._data[self._front + self._size-1]
            return self._data[self._back]
        #if the last position is in the first half of the array
        else:
            return self._data[self._front - self._size -1]
            
    def clear(self):
        """clear contents of array"""
        
        size_of_array = len(self._data)
        self._data = [None]*size_of_array
        
        return self._data
        
    def rotate(self,num_steps):
        """circularly shift rightwards k steps"""
        
        #update front and update back
        self._front = self._front + num_steps
        self._back = self._front + self._size - 1
        
        #circular shift right, 
        #self._data[-num_steps] = get the last num_step elements
        #self._data[:-num_steps] = get the complement of the last num_step elements
        self._data = self._data[-num_steps:] + self._data[:-num_steps] 
            
        return self._data
        
    def remove(self,e):
        """remove first element e found in the list, 
        
        incomplete 09-28-19"""
        
        
        for index in range(len(self._data)):
                
            if self._data[index] == e:
                #remove the index
                self._data[index] = None
                
                #update the size
                self._size -= 1
                
                break
        
        #if element in first index was deleted, update the first index pointer
        if self._data[self._front] == None:
            if self._front + self._size -1 < len(self._data):
                self._front += 1
            #the list is already circular shifted
            else:
                self._front = self._front - self._size
                
    def count(self,e):
        """ count number of occurences for variable e"""
        
        count = 0
        
        for index in range(len(self._data)):
                
            if self._data[index] == e:

                count +=1
                
        
        return count
            
                
            
            
        


if __name__ == "__main__":
    
    deque = DoubleEndedQueue(8)
    deque.enqueue(1)
    deque.enqueue(2)
    deque.enqueue(3)
    deque.enqueue(4)
    deque.enqueue(5)
    deque.enqueue(6)
    print(deque._data, deque.peekLast(),deque._size) #6
    print("####################################")
    deque.deleteLast() #12345
    deque.deleteLast() #1234
    print(deque._data,deque.peekLast())
    deque.dequeue() #234
    deque.dequeue() #34
    print(deque._data)
    print(deque.rotate(2),deque._front, deque._size)
    print("#################################")
    deque.addFront(1)
    deque.addFront(2)
    print(deque._data,deque._front)
    print(deque.rotate(2), deque._front, deque._size)
    print("#################################")
    deque.deleteLast()
    deque.deleteLast()
    print(deque._data)
    print(deque.peekLast(),deque._size)
    deque.addFront(3)
    deque.addFront(4)
    deque.addFront(5)
    deque.addFront(6)
    print(deque._data)
    print("Last element:", deque.peekLast())
    print("Position of 1st element: " ,deque._front)
    deque.addFront(7)
    deque.addFront(8)
    print(deque._data)
    print("Last element:", deque.peekLast())
    print("Position of first element: " ,deque._front)

    #implementing functions similar to collections.deque class
    print("First Element:" , deque._data[deque._front])
    print("Last Element:", deque._data[deque._back])
    print(deque._data)
    deque._data[3] = "Alan"
    print(deque._data)
    deque.remove("Alan")
    print(deque._data)
    print(deque._data, deque._front, deque._size)
    deque.remove(8)
    print(deque._data, deque._front, deque._size)
    deque.remove(7)
    print(deque._data, deque._front, deque._size)
    