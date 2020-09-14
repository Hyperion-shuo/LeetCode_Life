#206 Reverse Linked List
[链接](https://leetcode-cn.com/problems/reverse-linked-list/)

python 版本反转链表, 递归和循环2种写法


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre ,cur = None ,head
        
        while cur != None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        return pre
```

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(pre, cur):
            if not cur:
                return pre
            else:
                cur_next = cur.next
                cur.next = pre
                pre = cur
                cur = cur_next

            return helper(pre, cur)

        return helper(None, head)
```