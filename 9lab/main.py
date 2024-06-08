import re

# Task 1
def task1(s):
    result = bool(re.match("^[a-z0-9]+$", s))
    print(f"Task 1: Input: {s}, Matches: {result}")
    return result

# Task 2
def task2(s):
    result = bool(re.search("[A-Z]", s))
    print(f"Task 2: Input: {s}, Contains uppercase: {result}")
    return result

# Task 3
def task3(s):
    result = bool(re.match("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", s))
    print(f"Task 3: Input: {s}, Valid IP: {result}")
    return result

# Task 4
def task4(s):
    result = bool(re.match("^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", s))
    print(f"Task 4: Input: {s}, Valid time: {result}")
    return result

# Task 5
def task5(s):
    result = bool(re.match("^\d{5}(-\d{4})?$", s))
    print(f"Task 5: Input: {s}, Valid zip code: {result}")
    return result

# Task 6
def task6(s):
    result = bool(re.match("^[a-z0-9_-]{6,12}$", s))
    print(f"Task 6: Input: {s}, Valid username: {result}")
    return result

# Task 7
def task7(s):
    result = bool(re.match("^4|5|6\d{3}-?\d{4}-?\d{4}-?\d{4}$", s))
    print(f"Task 7: Input: {s}, Valid credit card: {result}")
    return result

# Task 8
def task8(s):
    result = bool(re.match("^\d{3}-\d{2}-\d{4}$", s))
    print(f"Task 8: Input: {s}, Valid SSN: {result}")
    return result

# Task 9
def task9(s):
    result = bool(re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$", s))
    print(f"Task 9: Input: {s}, Strong password: {result}")
    return result

# Task 10
def task10(s):
    result = bool(re.match("^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$", s))
    print(f"Task 10: Input: {s}, Valid IPv6: {result}")
    return result