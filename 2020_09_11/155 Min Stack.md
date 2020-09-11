# 155 Min Stack
这道题的题意为：设计一个栈支持常数时间的pop、push、top操作，同时可以在常数时间内
得到栈内最小值
***

hint：当一个元素a入栈时，栈内最小元素必然时他或此时栈内其他最小元素之一，记为min_a，维护这个时刻
的最小元素，则直到a出栈前，最小元素都大于min_a。
重复这个过程，下一个元素入栈再与min_比较

因此维护一个额外的数据结构记录每个元素进栈时的最小值，直到该元素出栈即可
因此维护一个进出栈顺序和原栈一模一样的最小栈即可，最小栈存储的元素时某入栈后，栈内
的最小元素

最小栈位置0可以放置一个大小为inf的哨兵，使空栈情况下新入栈的元素为最小
```angular2

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [math.inf]


    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

```

**不实用额外空间的方法，存储差值**
并非这题的重点，看看就好
```angular2
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.deq = deque()
        self.min_value = -1

    def push(self, x: int) -> None:
        if not self.deq:
            self.deq.append(0)
            self.min_value = x
        else:
            diff = x-self.min_value
            self.deq.append(diff)
            self.min_value = self.min_value if diff > 0 else x

    def pop(self) -> None:
        if self.deq:
            diff = self.deq.pop()
            if diff < 0:
                top = self.min_value - diff
                self.min_value = top
            else:
                top = self.min_value + diff
            return top

    def top(self) -> int:
        return self.min_value if self.deq[-1] < 0 else self.deq[-1] + self.min_value

    def getMin(self) -> int:
        return self.min_value if self.deq else -1
```


