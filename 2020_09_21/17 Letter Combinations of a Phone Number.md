# 17 Letter Combinations of a Phone Number

[链接](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

这道题的题意为,有一个电话键盘，给定一串数字，返回这串数组在电话键盘下所有可能的组合

思路为使用回溯，回溯的过程中维护一个所有的组合，不过这个组合是不完整的，
每次取数字串的下一个位置，从字典中取出这个数字所有对应的字母，拼接现有组合后面，
然后再取下一个数字，直到digits长度为0，即数字串被遍历完了



```python

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        phone = {'2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']}

        res = []
        def combine(combination, nextdigits):
            if len(nextdigits) == 0:
                res.append(combination)
            else:
                for letter in phone[nextdigits[0]]:
                    combine(combination + letter, nextdigits[1:])
        
        combine('', digits)

        return res
```