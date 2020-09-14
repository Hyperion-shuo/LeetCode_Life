# 2. Add Two Numbers

这道题的题意为，给定两个链表，求他们反转之后的整数相加再反转

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

Output: 7 -> 0 -> 8

Explanation: 342 + 465 = 807.

即等于直接相加，向后进位。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = None
        now = None
        flag = 0

        while (l1 or l2 or flag):
            
            val_sum, val_l1, val_l2 = 0, 0, 0

            if l1:
                val_l1 = l1.val
                l1 = l1.next
            if l2:
                val_l2 = l2.val
                l2 = l2.next

            val_sum = val_l1 + val_l2 + flag
            if val_sum >= 10:
                flag = 1
                val_sum -= 10
            else:
                flag = 0
            
            tmp = ListNode(val_sum)
            if not l:
                l = tmp
                now = l
            else:
                now.next = tmp
                now = tmp
        
        return l
```