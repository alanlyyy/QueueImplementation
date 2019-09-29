#FIFO - first in ->first out
class Empty(Exception):
    """raise an exception when the queue is empty during the dequeue operations"""
    pass
    

class Queue:
    
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        return self.queue == []
        
    def enqueue(self, data):
        self.queue.append(data)
        
    def dequeue(self):
    
        if self.isEmpty():
            raise Empty("Queue is empty")
        else:
            #store first index
            data = self.queue[0]
            
            #delete reference to first index
            del self.queue[0]
        
        return data
        
    def peek(self):
        if self.isEmpty():
            raise Empty("Queue is empty")
        return self.queue[0]
        
    def sizeQueue(self):
        return len(self.queue)
        
        
if __name__ == "__main__":
    queue = Queue()
    queue2 = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Size of queue:",queue.sizeQueue()) #3
    print("Dequeue:", queue.dequeue()) #10
    print("Dequeue:", queue.dequeue()) #20
    print("Size of queue:",queue.sizeQueue()) #1
    
    queue2.dequeue()    #should trigger an exception