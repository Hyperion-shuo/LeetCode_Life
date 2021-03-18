target = 7
result =[]
n = 4
candidates = [2, 3, 6, 7]

def dfs(target, combine, idx):
    if target <= 0:
        if target == 0:
            result.append(combine.copy())
    else:
        combine.append(candidates[idx])
        dfs(target - candidates[idx], combine, idx)
        combine.pop()
        if idx < n - 1:
            dfs(target, combine, idx + 1)


dfs(target, [], 0)
print(result)