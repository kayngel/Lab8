#task1
def number_generator(numbers):
    for number in numbers:
        yield number

# Example usage:
#gen = number_generator([1, 2, 3, 4, 5])
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 3
#print(next(gen))  # Output: 4
#print(next(gen))  # Output: 5

#task2
def even_number_generator(start, end):
    if start % 2 != 0:
        start += 1
    for number in range(start, end + 1, 2):
        yield number

# Example usage:
#gen = even_number_generator(1, 10)
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 4
#print(next(gen))  # Output: 6
#print(next(gen))  # Output: 8
#print(next(gen))  # Output: 10

#task3
def odd_number_generator(start, end):
    if start % 2 == 0:
        start += 1
    for number in range(start, end + 1, 2):
        yield number

# Example usage:
#gen = odd_number_generator(1, 10)
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 3
#print(next(gen))  # Output: 5
#print(next(gen))  # Output: 7
#print(next(gen))  # Output: 9

#task4
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage:
#gen = fibonacci_generator()
#print(next(gen))  # Output: 0
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 3
#print(next(gen))  # Output: 5
#print(next(gen))  # Output: 8

#task5
def prime_number_generator(limit):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for number in range(2, limit + 1):
        if is_prime(number):
            yield number

# Example usage:
#gen = prime_number_generator(30)
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 3
#print(next(gen))  # Output: 5
#print(next(gen))  # Output: 7
#print(next(gen))  # Output: 11
#print(next(gen))  # Output: 13
#print(next(gen))  # Output: 17
#print(next(gen))  # Output: 19
#print(next(gen))  # Output: 23
#print(next(gen))  # Output: 29

#task6
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order_traversal(root):
    if root:
        yield root.value
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)

# Example usage:


#root = TreeNode(1)
#root.left = TreeNode(2)
#root.right = TreeNode(3)
#root.left.left = TreeNode(4)
#root.left.right = TreeNode(5)

#gen = pre_order_traversal(root)
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 4
#print(next(gen))  # Output: 5
#print(next(gen))  # Output: 3

#task7
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.value
        yield from in_order_traversal(root.right)

# Example usage:

#root = TreeNode(1)
#root.left = TreeNode(2)
#root.right = TreeNode(3)
#root.left.left = TreeNode(4)
#root.left.right = TreeNode(5)

#gen = in_order_traversal(root)
#print(next(gen))  # Output: 4
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 5
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 3

#task8
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.value

# Example usage:

#root = TreeNode(1)
#root.left = TreeNode(2)
#root.right = TreeNode(3)
#root.left.left = TreeNode(4)
#root.left.right = TreeNode(5)

#gen = post_order_traversal(root)
#print(next(gen))  # Output: 4
#print(next(gen))  # Output: 5
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 3
#print(next(gen))  # Output: 1

#task9
def dfs_traversal(graph, start_node):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            yield node
            visited.add(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Example usage:

graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: []
}

#gen = dfs_traversal(graph, 1)
#print(next(gen))
#print(next(gen))

#task10
from collections import deque

def bfs_traversal(adj_list, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            yield node
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage:

graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: []
}

#gen = bfs_traversal(graph, 1)
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 3
#print(next(gen))  # Output: 4
#print(next(gen))  # Output: 5

#task11
def dict_keys_generator(dictionary):
    for key in dictionary:
        yield key

# Example usage:
#gen = dict_keys_generator({'a': 1, 'b': 2, 'c': 3})
#print(next(gen))  # Output: 'a'
#print(next(gen))  # Output: 'b'
#print(next(gen))  # Output: 'c'

#task12
def dict_values_generator(dictionary):
    for value in dictionary.values():
        yield value

# Example usage:
#gen = dict_values_generator({'a': 1, 'b': 2, 'c': 3})
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 3

#task13
def dict_items_generator(dictionary):
    for item in dictionary.items():
        yield item

# Example usage:
#gen = dict_items_generator({'a': 1, 'b': 2, 'c': 3})
#print(next(gen))  # Output: ('a', 1)
#print(next(gen))  # Output: ('b', 2)
#print(next(gen))  # Output: ('c', 3)

#task14
def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.rstrip('\n')

# Example usage:
#gen = file_lines_generator('example.txt')
#print(next(gen))  # Output: 'First line'
#print(next(gen))  # Output: 'Second line'

#task15
import re

def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line)
            for word in words:
                yield word

# Example usage:
#gen = file_words_generator('example.txt')
#print(next(gen))  # Output: 'First'
#print(next(gen))  # Output: 'line'

#task16
def string_chars_generator(input_string):
    for char in input_string:
        yield char

# Example usage:
#gen = string_chars_generator('Hello')
#print(next(gen))  # Output: 'H'
#print(next(gen))  # Output: 'e'
#print(next(gen))  # Output: 'l'
#print(next(gen))  # Output: 'l'
#print(next(gen))  # Output: 'o'

#task17
def unique_elements_generator(input_list):
    seen = set()
    for element in input_list:
        if element not in seen:
            seen.add(element)
            yield element

# Example usage:
#gen = unique_elements_generator([1, 2, 2, 3, 3, 3])
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 3

#task18
def reverse_list_generator(input_list):
    for i in range(len(input_list) - 1, -1, -1):
        yield input_list[i]

# Example usage:
#gen = reverse_list_generator([1, 2, 3, 4, 5])
#print(next(gen))  # Output: 5
#print(next(gen))  # Output: 4
#print(next(gen))  # Output: 3
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 1

#taks19
def cartesian_product_generator(list1, list2):
    for item1 in list1:
        for item2 in list2:
            yield (item1, item2)

# Example usage:
#gen = cartesian_product_generator([1, 2], ['a', 'b'])
#print(next(gen))  # Output: (1, 'a')
#print(next(gen))  # Output: (1, 'b')
#print(next(gen))  # Output: (2, 'a')
#print(next(gen))  # Output: (2, 'b')

#task20
from itertools import permutations

def permutations_generator(input_list):
    for perm in permutations(input_list):
        yield perm

# Example usage:
#gen = permutations_generator([1, 2, 3])
#print(next(gen))  # Output: (1, 2, 3)
#print(next(gen))  # Output: (1, 3, 2)
#print(next(gen))  # Output: (2, 1, 3)
#print(next(gen))  # Output: (2, 3, 1)
#print(next(gen))  # Output: (3, 1, 2)
#print(next(gen))  # Output: (3, 2, 1)

#task21
from itertools import combinations

def combinations_generator(input_list):
    for r in range(1, len(input_list) + 1):
        for comb in combinations(input_list, r):
            yield comb

# Example usage:
#gen = combinations_generator([1, 2, 3])
#print(next(gen))  # Output: (1,)
#print(next(gen))  # Output: (2,)
#print(next(gen))  # Output: (3,)
#print(next(gen))  # Output: (1, 2)
#print(next(gen))  # Output: (1, 3)
#print(next(gen))  # Output: (2, 3)
#print(next(gen))  # Output: (1, 2, 3)

#task22
def tuple_list_generator(tuple_list):
    for tup in tuple_list:
        yield tup

# Example usage:
#gen = tuple_list_generator([(1, 2), (3, 4), (5, 6)])
#print(next(gen))  # Output: (1, 2)
#print(next(gen))  # Output: (3, 4)
#print(next(gen))  # Output: (5, 6)

#task23
def parallel_lists_generator(*lists):
    for items in zip(*lists):
        yield items

# Example usage:
#gen = parallel_lists_generator([1, 2, 3], ['a', 'b', 'c'])
#print(next(gen))  # Output: (1, 'a')
#print(next(gen))  # Output: (2, 'b')
#print(next(gen))  # Output: (3, 'c')

#task24
def flatten_list_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list_generator(item)
        else:
            yield item

# Example usage:
#gen = flatten_list_generator([1, [2, [3, 4], 5], 6])
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 3
#print(next(gen))  # Output: 4
#print(next(gen))  # Output: 5
#print(next(gen))  # Output: 6

#task25
def nested_dict_generator(nested_dict):
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            for nested_key, nested_value in nested_dict_generator(value):
                yield (nested_key, nested_value)
        else:
            yield (key, value)

# Example usage:
#gen = nested_dict_generator({'a': {'b': 1, 'c': 2}, 'd': 3})
#print(next(gen))  # Output: ('b', 1)
#print(next(gen))  # Output: ('c', 2)
#print(next(gen))  # Output: ('d', 3)

#task26
def powers_of_two_generator(n):
    for i in range(n + 1):
        yield 2 ** i

# Example usage:
#gen = powers_of_two_generator(4)
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 4
#print(next(gen))  # Output: 8
#print(next(gen))  # Output: 16

#task27
def powers_of_base_generator(base, limit):
    power = 1
    while power <= limit:
        yield power
        power *= base

# Example usage:
#gen = powers_of_base_generator(3, 81)
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 3
#print(next(gen))  # Output: 9
#print(next(gen))  # Output: 27
#print(next(gen))  # Output: 81

#task28
def squares_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 2

# Example usage:
#gen = squares_generator(1, 5)
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 4
#print(next(gen))  # Output: 9
#print(next(gen))  # Output: 16
#print(next(gen))  # Output: 25

#task29
def cubes_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 3

# Example usage:
#gen = cubes_generator(1, 4)
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 8
#print(next(gen))  # Output: 27
#print(next(gen))  # Output: 64

#task30
def factorials_generator(n):
    factorial = 1
    for i in range(n + 1):
        if i > 0:
            factorial *= i
        yield factorial

# Example usage:
#gen = factorials_generator(4)
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 6
#print(next(gen))  # Output: 24

#task31
def collatz_sequence_generator(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield n

# Example usage:
#gen = collatz_sequence_generator(6)
#print(next(gen))  # Output: 6
#print(next(gen))  # Output: 3
#print(next(gen))  # Output: 10
#print(next(gen))  # Output: 5
#print(next(gen))  # Output: 16
#print(next(gen))  # Output: 8
#print(next(gen))  # Output: 4
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 1

#task32
def geometric_progression_generator(initial_term, common_ratio, limit):
    term = initial_term
    while term <= limit:
        yield term
        term *= common_ratio

# Example usage:
#gen = geometric_progression_generator(2, 3, 20)
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 6
#print(next(gen))  # Output: 18

#task33
def arithmetic_progression_generator(initial_term, common_difference, limit):
    term = initial_term
    while term <= limit:
        yield term
        term += common_difference

# Example usage:
#gen = arithmetic_progression_generator(2, 3, 20)
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 5
#print(next(gen))  # Output: 8
#print(next(gen))  # Output: 11
#print(next(gen))  # Output: 14
#print(next(gen))  # Output: 17
#print(next(gen))  # Output: 20

#task34
def running_sum_generator(numbers):
    running_sum = 0
    for number in numbers:
        running_sum += number
        yield running_sum

# Example usage:
#gen = running_sum_generator([1, 2, 3, 4])
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 3
#print(next(gen))  # Output: 6
#print(next(gen))  # Output: 10

#task35
def running_product_generator(numbers):
    running_product = 1
    for number in numbers:
        running_product *= number
        yield running_product

# Example usage:
#gen = running_product_generator([1, 2, 3, 4])
#print(next(gen))  # Output: 1
#print(next(gen))  # Output: 2
#print(next(gen))  # Output: 6
#print(next(gen))  # Output: 24