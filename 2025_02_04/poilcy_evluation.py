# n * m 格子
# 空地 0
# 陷阱 - 未知
# 财宝 + 未知
# s step 后reward 期望最大
# policy (i, j), (p1, p2, p3, p4)四个方向改率

import copy

def poilcy_evluation(n, m, table, probs, s):
    value_table = [[0 for _ in range(m)] for _ in range(n)]
    new_value_table = [[0 for _ in range(m)] for _ in range(n)]

    d_s = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for cur_s in range(s):
        for i in range(n):
            for j in range(m):
                for k in range(4):
                    d = d_s[k]
                    i_, j_ = i + d[0], j + d[1]
                    if i_ < 0 or i_ >= n:
                        continue
                    if j_ < 0 or j_ >= m:
                        continue
                    
                    new_value_table[i][j] += (value_table[i_][j_] + table[i_][j_]) * probs[k] 
                    # value_table[i][j] += table[i_][j_] * probs[k] 

        value_table = copy.copy(new_value_table)
        new_value_table = [[0 for _ in range(m)] for _ in range(n)]
    
    # return 最大坐标
    # 找到value_table 最大值坐标
    max_value = -float('inf')
    max_i, max_j = -1, -1
    for i in range(n):
        for j in range(m):
            if value_table[i][j] > max_value:
                max_value = value_table[i][j]
                max_i, max_j = i, j

    return max_i, max_j