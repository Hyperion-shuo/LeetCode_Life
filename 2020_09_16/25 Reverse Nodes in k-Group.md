# 25. Reverse Nodes in k-Group

[链接](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)

这道题的题意为，给定一个链表和小于链表长度的数k，按k个一组翻转，若最后一组不到k长度，则不翻转


题目不难，就是实现的时候细节比较多
思路是k个一组翻转，但是要判断链表剩余数量是否有k个，因为最后一组少于k是不翻转的
每次先判断是否有k个再翻转要2n次遍历
而通过设置一个flag，每次查看这组翻转的是否有k个，则只要n + k次遍历。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        def reverseKList(head: ListNode) -> int:
            # 反转head的前k个元素
            # 若少于k个则flag 为1
            flag = 1
            # pre 是反序链表的头， cur是head表正在被翻转的节点， tail是反序链表的尾
            pre, cur, tail = None, head, head
            for i in range(k):
                if cur:
                    tmp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = tmp
                else:
                    flag = 0
                    break
            return (pre, cur, tail, flag)

        # 翻转链表
        def reverseList(head: ListNode) -> ListNode:
            pre ,cur = None ,head
            while cur != None:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre

        # 翻转原链表前k个，插入结果链表表头，在翻转原链表后k个直到原原链表元素不足k个
        # 插入哑节点作结果链表为开头
        dummy = ListNode(-1)
        # pre 当前被翻转的k小段的表头，cur是原链表被取掉前k个后下一次翻转的头节点
        # tail 当前被翻转的k小段的表尾， result_tail是结果链表的表尾
        pre, cur, tail, result_tail = None, head, None, dummy
        flag = 1
        while flag:
            pre, cur, tail, flag = reverseKList(cur)
            if flag:
                result_tail.next = pre
                result_tail = tail
            else:
                # 若最后一个少于k个，则翻转回来
                pre = reverseList(pre)
                result_tail.next = pre

        return dummy.next

```