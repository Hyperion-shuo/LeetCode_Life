# 23 Merge k Sorted Lists

[链接](https://leetcode-cn.com/problems/merge-k-sorted-lists/)

这道题的题意为：有序地合并n个有序链表

## 思路一：直接合并。
对比每个链表头节点，取最小的，再递归地合并剩余的
时间复杂度O(nk * k)，总共n * k个元素，每次选出一个元素要比较k次， 空间复杂度O1

类似的直接解法还有将所有元素读进数组，然后排序再变成链表
时间复杂度 O(nk * log(nk)) 空间复杂度 O(n * k)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 似乎这里去除None的操作耗费了过多时间
        # 去掉掉为None的元素，实际上可以通过在后面把新的list返回lists里时避免把None插入
        # 但是有测试用例初始就是一堆 [[],[]],因此必须再开头就处理
        # lists =  [l for l in lists if l]也可以，但是速度稍慢
        lists = list(filter(None, lists))

        k = len(lists)
        if k == 0:
            return None

        min_node = lists[0]
        min_node_list_idx = 0
        for i in range(k):
            if lists[i].val < min_node.val:
                min_node = lists[i]
                min_node_list_idx = i

        lists[min_node_list_idx] = lists[min_node_list_idx].next
        min_node.next = self.mergeKLists(lists)

        return min_node
```

# 思路二 对表头使用优先队列

思路一中，选出当前所有链表最小的头节点时比较了K次，
而注意到和上一次插入相比，比较的K-1个元素是相同的，却没有被利用到。
因此注意到可以使用一个数据结构维护表头的k个元素，每次取出最小的并插入下一个元素。
考虑一个长为n优先队列，每次常数时间取出最小元素，插入一个元素需要O(n)时间复杂度。
则总时间复杂度为O(nk*log(k))
```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 去掉空的list，避免输入为空的边界情况
        lists = list(filter(None, lists))
        if not lists or len(lists) == 0:
            return None

        import heapq
        h = []

        for idx, node in enumerate(lists):
            # push 进了一个元组
            # 这里元组的第二位设为当前ListNode更方便
            # 但是python heapq在元祖第一个元素相同时会自动比较第二个
            # 而ListNode对象无法比较
            # 因此只能用下标代指
            heapq.heappush(h, (node.val, idx))
            
        dummy = ListNode(float('-inf'))
        cur = dummy
        while h:
            val, idx = heapq.heappop(h)
            node = lists[idx]
            cur.next = node
            cur = cur.next
            lists[idx] = lists[idx].next
            if node.next != None:
                heappush(h, (node.next.val, idx))

        return dummy.next
```



