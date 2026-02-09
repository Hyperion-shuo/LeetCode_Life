import random
import copy
import sys

# ==========================================
# 1. 单侧扫描版本
# ==========================================

def partition_Lomuto(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1],  arr[high] = arr[high], arr[i + 1]
    return i + 1
    
def quick_sort_recursive_Lomuto(arr, low, high):
    if low < high:
        pivot = partition_Lomuto(arr, low, high)
    
        quick_sort_recursive_Lomuto(arr, low, pivot - 1)
        quick_sort_recursive_Lomuto(arr, pivot + 1, high)

# 改为 my_quick_sort 进行测试
def my_quick_sort_Lomuto(arr):
    """
    这是对外的包装函数，方便测试脚本调用。
    不需要修改这里，除非你的入口函数名不一样。
    """
    if len(arr) <= 1:
        return arr
    # 注意：这里假设你写的是原地排序
    # 如果你写的是非原地排序（返回新列表），请修改这里为 return quick_sort_recursive(...)
    quick_sort_recursive_Lomuto(arr, 0, len(arr) - 1)
    return arr

# ==========================================
# 2. 双侧扫描版本
# ==========================================

def partition_Hoare(arr, low, high):
    i = low - 1
    j = high + 1
    # 如果设置pivot = arr[low]，就必须return j
    # 因为最坏情况是第一次j就等于i等low
    pivot = arr[low]
    
    while True:
        
        while True:
            j -= 1
            if arr[j] <= pivot:
                break    
            
        while True:
            i += 1
            # 不需要检查 i是否大于high
            # 因为如果是第一次交换，i必定等于low
            # 如果是后续交换，i至少会是上一交换的old_j的位置
            if arr[i] >= pivot:
                break   
        
        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]
        
    # arr[i + 1], arr[pivot] = arr[pivot],  arr[i + 1]
    # return i + 1

def quick_sort_recursive_Hoare(arr, low, high):
    if low < high:
        pivot = partition_Hoare(arr, low, high)
        # 注意这里不能写pivot - 1，因为pivot只是一个分割点，保证左侧的值都小于右侧，但不是初始时设置的哨兵arr[low]的真实位置
        quick_sort_recursive_Hoare(arr, low, pivot)
        quick_sort_recursive_Hoare(arr, pivot + 1, high)

# 改为 my_quick_sort 进行测试
def my_quick_sort_Hoare(arr):
    """
    这是对外的包装函数，方便测试脚本调用。
    不需要修改这里，除非你的入口函数名不一样。
    """
    if len(arr) <= 1:
        return arr
    # 注意：这里假设你写的是原地排序
    # 如果你写的是非原地排序（返回新列表），请修改这里为 return quick_sort_recursive(...)
    quick_sort_recursive_Hoare(arr, 0, len(arr) - 1)
    return arr
# ==========================================
# 3. 三中值版本
# ==========================================

# def partition(arr, low, high):
#     pass

# def quick_sort_recursive(arr, low, high):
#     pass

# def my_quick_sort(arr):
#     """
#     这是对外的包装函数，方便测试脚本调用。
#     不需要修改这里，除非你的入口函数名不一样。
#     """
#     if len(arr) <= 1:
#         return arr
#     # 注意：这里假设你写的是原地排序
#     # 如果你写的是非原地排序（返回新列表），请修改这里为 return quick_sort_recursive(...)
#     quick_sort_recursive(arr, 0, len(arr) - 1)
#     return arr


# ==========================================
# 2. 测试用例集
# ==========================================

def get_test_cases():
    return [
        {
            "name": "基础乱序",
            "input": [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        },
        {
            "name": "空数组",
            "input": []
        },
        {
            "name": "单元素数组",
            "input": [42]
        },
        {
            "name": "双元素 (正序)",
            "input": [1, 2]
        },
        {
            "name": "双元素 (逆序)",
            "input": [2, 1]
        },
        {
            "name": "完全有序",
            "input": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        },
        {
            "name": "完全逆序",
            "input": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        },
        {
            "name": "包含重复元素",
            "input": [4, 2, 2, 8, 3, 3, 1]
        },
        {
            "name": "全部元素相同",
            "input": [5, 5, 5, 5, 5]
        },
        {
            "name": "包含负数",
            "input": [-5, 10, -3, 0, 2, -1]
        },
        {
            "name": "大规模随机数据 (1000个)",
            "input": [random.randint(-1000, 1000) for _ in range(1000)]
        }
    ]

# ==========================================
# 3. 测试运行逻辑
# ==========================================

def run_tests():
    cases = get_test_cases()
    passed_count = 0
    total_count = len(cases)

    print(f"{'='*20} 开始测试 {'='*20}")

    for case in cases:
        name = case["name"]
        original_input = case["input"]
        
        # 1. 准备数据：深拷贝一份，防止原数据被修改影响对比
        # 这里的 arr_to_sort 是给你排序用的
        arr_to_sort = copy.deepcopy(original_input)
        
        # 2. 获取标准答案 (Python 内置 sort 作为真理)
        expected = sorted(original_input)
        
        try:
            # 3. 运行你的排序
            # 如果你的函数是原地排序，它会修改 arr_to_sort
            # 如果你的函数返回新列表，result 会接收到
            result = my_quick_sort(arr_to_sort)
            
            # 兼容处理：如果你是原地排序，result 可能是 None，此时检查 arr_to_sort
            if result is None:
                actual = arr_to_sort
            else:
                actual = result

            # 4. 验证结果
            if actual == expected:
                print(f"✅ [通过] {name}")
                passed_count += 1
            else:
                print(f"❌ [失败] {name}")
                print(f"   输入: {original_input[:10]} {'...' if len(original_input)>10 else ''}")
                print(f"   预期: {expected[:10]} {'...' if len(expected)>10 else ''}")
                print(f"   实际: {actual[:10]} {'...' if len(actual)>10 else ''}")

        except Exception as e:
            print(f"❌ [报错] {name}")
            print(f"   错误信息: {e}")
            # 如果是递归深度错误，提示一下
            if "recursion" in str(e).lower():
                print("   提示: 可能是遇到了最坏情况导致栈溢出，或者递归终止条件没写对。")

    print(f"\n{'='*20} 测试总结 {'='*20}")
    print(f"通过率: {passed_count}/{total_count}")
    
    if passed_count == total_count:
        print("🎉 恭喜！所有测试用例全部通过！")
    else:
        print("💪 加油，还有 bug 需要修复。")

if __name__ == "__main__":
    # 设置递归深度，防止大规模逆序测试时 Python 默认的 1000 层不够用
    sys.setrecursionlimit(2000)
    run_tests()