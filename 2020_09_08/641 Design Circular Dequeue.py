class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self._num = 0
        self._len = k
        self._elem = [0] * k
        self._head = 0
        self._tail = k - 1

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self._num < self._len:
            self._num += 1
            self._head = (self._head - 1) % self._len
            self._elem[self._head] = value
            return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self._num < self._len:
            self._num += 1
            self._tail = (self._tail + 1) % self._len
            self._elem[self._tail] = value
            return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self._num > 0:
            self._num -= 1
            self._head = (self._head + 1) % self._len
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self._num > 0:
            self._num -= 1
            self._tail = (self._tail - 1) % self._len
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self._num == 0:
            return -1
        else:
            return self._elem[self._head]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self._num == 0:
            return -1
        else:
            return self._elem[self._tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self._num == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self._num == self._len