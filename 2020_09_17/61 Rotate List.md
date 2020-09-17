# 61 Rotate List

[链接](https://leetcode-cn.com/problems/rotate-list/)

这道题的题意为给定一个链表和一个正整数k，将链表每个节点移动k个位置

思路 用快慢指针，快指针比慢指针快K，将慢指针后面部分插到头上即可

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 边界情况 表长为1或0，向右移动0位，都原封不动返回
        if not head or not head.next or not k:
            return None
        
        # 为了避免 k >> 链表长度的情况
        # 先统计链表长度在计算 k % 长度
        tmp = head
        len = 1
        while tmp.next:
            tmp = tmp.next
            len += 1
        k = k % len # 这里 k==0 也可以判断一下是否直接原样返回，我在最后判断了
    
                
        # 哑节点，防止当head变了找不到头
        dummy = ListNode(0)
        dummy.next = head
        fast = head
        slow = head
        for i in range(k):
            fast = fast.next if fast.next else head

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # 边界条件
        if fast == slow:
            return dummy.next
        else:
            dummy.next = slow.next
            slow.next = None
            fast.next = head

        return dummy.next
```