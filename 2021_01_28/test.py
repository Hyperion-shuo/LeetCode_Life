sample = []
result = []
n = 3

def generate(sample):
    if len(sample) == 2 * n:
        if valid(sample):
            result.append(''.join(sample))
    else:
        sample.append('(')
        generate(sample)
        sample.pop()
        sample.append(')')
        generate(sample)
        sample.pop()

def valid(sample):
    balance = 0
    for char in sample:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return False
    return balance == 0

generate(sample)
print(result)

