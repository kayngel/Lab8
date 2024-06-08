import math  # task10

# Task 1: Sum of Squares
def task1(arr):
    result = sum(x ** 2 for x in arr)
    print(f"Task 1: Input: {arr}, Sum of squares: {result}")
    return result

# Task 2: Filter and Sum
def task2(arr):
    if not arr:
        return 0
    avg = sum(arr) / len(arr)
    result = sum(num for num in arr if num >= avg)
    print(f"Task 2: Input: {arr}, Average: {avg}, Sum of elements >= average: {result}")
    return result

# Task 3: Sort by Frequency
def task3(arr):
    if not arr:
        return []
    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    sorted_arr = sorted(arr, key=lambda x: (-frequency[x], x))
    print(f"Task 3: Input: {arr}, Sorted by frequency: {sorted_arr}")
    return sorted_arr

# Task 4: Find Missing Number
def task4(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    print(f"Task 4: Input: {arr}, Missing number: {missing_number}")
    return missing_number

# Task 5: Longest Consecutive Sequence
def task5(nums):
    if not nums:
        return 0

    nums_set = set(nums)
    longest_streak = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    print(f"Task 5: Input: {nums}, Longest consecutive sequence length: {longest_streak}")
    return longest_streak

# Task 6: Rotate Array
def task6(nums, k):
    if not nums:
        return []

    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    print(f"Task 6: Input: {nums}, Rotated by {k} steps: {nums}")
    return nums

# Task 7: Array of Products
def task7(nums):
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    result = [1] * n

    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    for i in range(n):
        result[i] = left_products[i] * right_products[i]

    print(f"Task 7: Input: {nums}, Array of products: {result}")
    return result

# Task 8: Maximum Subarray Sum
def task8(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    print(f"Task 8: Input: {nums}, Maximum subarray sum: {max_sum}")
    return max_sum

# Task 9: Spiral Order Matrix
def task9(matrix):
    if not matrix:
        return []

    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    print(f"Task 9: Input: {matrix}, Spiral order: {result}")
    return result

# Task 10: K Closest Points to Origin
def task10(points, k):
    distances = [(point, math.sqrt(point[0] ** 2 + point[1] ** 2)) for point in points]

    distances.sort(key=lambda x: x[1])
    result = [point[0] for point in distances[:k]]
    print(f"Task 10: Input: {points}, K closest points: {result}")
    return result

# Examples of using the functions with print statements:
print(task1([1, 2, 3]))  # Output: 14
print(task2([1, 2, 3, 4, 10]))  # Output: 14
print(task3([4, 6, 2, 6, 4, 4, 6]))  # Output: [4, 4, 4, 6, 6, 6, 2]
print(task4([1, 2, 4, 5]))  # Output: 3
print(task5([100, 4, 200, 1, 3, 2]))  # Output: 4
print(task6([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
print(task7([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
print(task8([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
print(task9([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(task10([(1, 2), (1, 1), (3, 4)], 2))  # Output: [(1, 1), (1, 2)]
