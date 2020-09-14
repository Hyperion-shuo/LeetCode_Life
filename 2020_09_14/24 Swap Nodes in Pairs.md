# 24 Swap Nodes in Pairs

[链接](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)
这道题的题意为，两两交换链表数组的顺序，不能直接赋值，只能操作指针

递归地处理前两个元素即可，当只剩最后一个或者None时返回

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            next_node = head.next
            tmp = next_node.next
            next_node.next = head
            head.next = self.swapPairs(tmp)
            return next_node
        else:
            return head
```

