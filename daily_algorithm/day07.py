class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = k
        self.queue = []

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return  if the operation is successful.
        """
        if len(self.queue) < self.size:
            self.queue.insert(0,value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return  if the operation is successful.
        """
        if len(self.queue)<self.size:
            self.queue.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return  if the operation is successful.
        """
        if len(self.queue) > 0:
            self.queue = self.queue[1:]
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return  if the operation is successful.
        """
        if len(self.queue)>0:
            self.queue = self.queue[:-1]
            return True
        return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.queue[0] if self.queue else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return  self.queue[-1] if self.queue else -1


    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return False  if self.queue else True


    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return True if len(self.queue) == self.size else False

if __name__ == '__main__':
    circularDeque = MyCircularDeque(3)
    print(circularDeque.insertLast(1))

    print(circularDeque.insertLast(2))

    print(circularDeque.insertFront(3))

    print(circularDeque.insertFront(4))

    print(circularDeque.getRear())

    print(circularDeque.isFull())

    print(circularDeque.deleteLast())

    print(circularDeque.insertFront(4))

    print(circularDeque.getFront())
    # a = []
    # a.insert(0,1)
    # a.insert(0,2)
    # print(a[:-1])
    # a = a[:-1]
    # print(len(a))
    # print(a)