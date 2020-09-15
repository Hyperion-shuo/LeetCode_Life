# 141 Linked List Cycle
这道题的题意为 给定一个循环链表，用常数空间判断该链表是否循环
[链接](https://leetcode-cn.com/problems/linked-list-cycle/solution/)

##1. 集合或哈希表
用集合或者字典存储每个指针，当终止或遇到重复的指针时结束
时间复杂读On  空间复杂度On
需要额外空间
```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        a = set() 
        while head:
            
            if head in a:
                return True

            a.add(head)
            head = head.next
        return False
```

##2.  快慢指针
若快指针没到终止状态就追上慢指针了，则说明他经过了一个循环，
若遇到终止状态，则说明数组不循环
```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if (not head or head.next == None) :
            return False
        
        # 错开避免第一次就被判断重复
        fast = head.next
        slow = head

        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False

```