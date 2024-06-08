#task1
def interpolate_missing(lst):
    interpolated = []
    i = 0
    while i < len(lst):
        if lst[i] is None:
            left = i - 1
            right = i + 1
            while left >= 0 and lst[left] is None:
                left -= 1
            while right < len(lst) and lst[right] is None:
                right += 1
            if left >= 0 and right < len(lst):
                interpolated.append((lst[left] + lst[right]) / 2)
            elif left >= 0:
                interpolated.append(lst[left])
            elif right < len(lst):
                interpolated.append(lst[right])
        else:
            interpolated.append(lst[i])
        i += 1
    return interpolated

#print(interpolate_missing([1, None, None, 4]))

#task2
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Example usage:
#for num in fibonacci(5):
    #print(num, end=", ")

#task3
def process_batches(lst, batch_size):
    max_values = []
    for i in range(0, len(lst), batch_size):
        batch = lst[i:i+batch_size]
        max_values.append(max(batch))
    return max_values

#print(process_batches([1, 2, 3, 4, 5, 6], 2))


#task4
def encode_string(s):
    encoded = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded += str(count) + s[i - 1]
            count = 1
    encoded += str(count) + s[-1]
    return encoded

def decode_string(s):
    decoded = ""
    i = 0
    while i < len(s):
        count = int(s[i])
        decoded += s[i + 1] * count
        i += 2
    return decoded

# Example usage:
#encoded = encode_string("aaabbc")
#print(encoded)  # Output: "3a2bc"
#print(decode_string(encoded))  # Output: "aaabbc"


#task5
def rotate_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix


# Example usage:
#matrix = [
    #[1, 2],
    #[3, 4]
#]

#print(rotate_matrix(matrix))  # Output: [[3, 1], [4, 2]]


#task6
import re

def regex_search(strings, pattern):
    matches = []
    for string in strings:
        if re.search(pattern, string):
            matches.append(string)
    return matches

# Example usage:
#print(regex_search(["test", "test123", "none"], "test\d+"))


#task7
def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


# Example usage:
#print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]


#task8
import math

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage:
#print(is_prime(11))  # Output: True


#task9
def group_by_key(data, key):
    grouped = {}
    for entry in data:
        group_key = entry[key]
        if group_key in grouped:
            grouped[group_key].append(entry['value'])
        else:
            grouped[group_key] = [entry['value']]
    return grouped

# Example usage:
#data = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}, {'key': 'a', 'value': 3}]
#print(group_by_key(data, 'key'))  # Output: {'a': [1, 3], 'b': [2]}


#task10
import statistics

def remove_outliers(lst):
    mean = statistics.mean(lst)
    std_dev = statistics.stdev(lst)
    lower_bound = mean - 2 * std_dev
    upper_bound = mean + 2 * std_dev
    return [x for x in lst if lower_bound <= x <= upper_bound]

# Example usage:
#print(remove_outliers([10, 100, 200, 300, 400, 500, 600]))  # Output: [100, 200, 300, 400, 500]



