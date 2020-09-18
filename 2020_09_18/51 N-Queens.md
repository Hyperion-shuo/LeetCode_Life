# 51 N-Queens

## [链接](https://leetcode-cn.com/problems/n-queens/)

经典回溯算法

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        import copy
        result = []
        
        # 单独的打印函数
        def print_queens(Q):
            for i in range(len(Q)):
                row_i = list('.' * n)
                row_i[Q[i]] = 'Q'
                row_i = ''.join(row_i)
                Q[i] = row_i
            return Q
        
        # Q[i] 是第i行的Queen在第几列
        def place_queens(Q, r):
            if r == n:
                result.append(Q)
            else:
                for j in range(n):
                    legal = True
                    for i in range(r):
                        if (Q[i] == j or Q[i] - j == r - i or Q[i] - j == i - r):
                            legal = False
                    if legal:
                        Q_next = copy.copy(Q)
                        Q_next[r] = j
                        place_queens(Q_next, r + 1)

        Q = [0] * n
        place_queens(Q, 0)
        for i in range(len(result)):
            result[i] = print_queens(result[i])

        return result
```