# 19 Remove Nth Node From End of List
(链接)[https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/]

这道题的题意为，给定一个链表和数n，删除这个链表的倒数第n个元素
**要求只能一次遍历**

**注意头节点的情况，要么加哑节点，要么单独判断**


##方法一：双指针
- 看似只循环一次，实际上查询了 l + n - 2 次指针
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 添加一个哑节点，用来处理删除头节点的特殊情况
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy
        for i in range(n):
            first = first.next
        
        while first.next:
            first = first.next
            second = second.next
        
        second.next = second.next.next

        return dummy.next
```

## 方法二：回溯
- 真正地只遍历一次

```python

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        def travel(node):
            if not node.next:
                return 1
            # 回朔，记录这是倒数第几个
            nth = travel(node.next) + 1
            # 对于倒数第n，个让倒数n+1 指向倒数n-1
            # 如果倒数第n个是头节点则无效
            if nth == n + 1:
                node.next = node.next.next
            return nth
        
        # 单独判断头节点是否是倒数第n个
        # 是的话则删除头节点
        if travel(head) == n:
            head = head.next
        
        return head
```