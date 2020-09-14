# 21 Merge Two Sorted Lists
[链接](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

这道题的题意为按序合并两个有序的数组

## 递归解法，简洁但要消耗额外栈空间
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```

## 遍历解法
```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 头节点
        dummy = ListNode(float('-inf'))
        this = dummy
        while l1 and l2:
            if l1.val > l2 .val:
                this.next = l2
                l2 = l2.next
            else:
                this.next = l1
                l1 = l1.next
            this = this.next
        
        this.next = l1 if not l2 else l2
        
        return dummy.next
```