class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """

        self._num = 0
        self._len = k
        self._elem = [0] * k
        self._head = 0
        self._tail = k - 1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self._num < self._len:
            self._num += 1
            self._tail = (self._tail + 1) % self._len
            self._elem[self._tail] = value
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self._num == 0:
            return False
        else:
            self._num -= 1
            self._head = (self._head + 1) % self._len
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self._num == 0:
            return -1
        else:
            return self._elem[self._head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self._num == 0:
            return -1
        else:
            return self._elem[self._tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self._num == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self._num == self._len
