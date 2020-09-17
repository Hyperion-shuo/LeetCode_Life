# 82 Remove Duplicates from Sorted List II

## [链接](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/)

这道题的题意为，给定一个有序链表，若有重复的元素，将他们全删除（不是删除到只剩一个，最后一个也要删除）
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(float('-inf'))
        dummy.next = head
        pre = dummy

        # 这里注意，只有一个head.next 可能会因为head为None 报错
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                head = head.next
                pre = pre.next
        
        return dummy.next
```