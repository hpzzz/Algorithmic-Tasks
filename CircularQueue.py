class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [None] * k
        self.head = 0
        self.tail = 0
        self.maxSize = k
        self.num_elements = 0
        
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.queue[self.tail] = value
            self.tail = ((self.tail + 1) % self.maxSize)
            self.num_elements += 1
            return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.maxSize
            self.num_elements -= 1
            return True
            
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.head]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
         return self.queue[(self.tail - 1)% self.maxSize]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        # return ((self.tail + 1) % self.maxSize == self.head)
        return self.num_elements == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        # return ((self.head == self.tail + 1) or ((self.head == 0) and self.tail == self.maxSize - 1))
        return self.num_elements == self.maxSize