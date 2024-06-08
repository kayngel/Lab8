Лабораторна робота №9: Regular expressions
___
Мета роботи: 

We search and perform operations with strings based on certain rules and conditions, which are specified using metacharacters and special constructions

___
Опис завдання:
```Python
1.	Write a def(task1) regular expression that matches a string containing only lowercase letters and digits. Input: "hello123" Output: True
2.	Write a def(task2) regular expression that matches a string containing at least one uppercase letter. Input: "Hello" Output: True
3.	Write a def(task3) regular expression that matches a string containing a valid IPv4 address. Input: "192.168.1.1" Output: True
4.	Write a def(task4) regular expression that matches a string containing a valid time in the format of "HH:MM:SS". Input: "12:34:56" Output: True
5.	Write a def(task5) regular expression that matches a string containing a valid US postal code in the format of "NNNNN" or "NNNNN-NNNN". Input: "12345" or "12345-6789" Output: True
6.	Write a def(task6) regular expression that matches a string containing a valid username, with the following criteria: only contains lowercase letters, numbers, underscores, and hyphens, and is between 6 and 12 characters long. Input: "john_doe-123" Output: True
7.	Write a def(task7) regular expression that matches a string containing a valid credit card number (either 15 or 16 digits, starting with either 4, 5, or 6). Input: "4512-3456-7890-1234" Output: True
8.	Write a def(task8) regular expression that matches a string containing a valid social security number (in the format of ###-##-####). Input: "123-45-6789" Output: True
9.	Write a def(task9) regular expression that matches a string containing a valid password, with the following criteria: at least one uppercase letter, one lowercase letter, one digit, one special character (@, #, $, or %), and at least 8 characters long. Input: "Passw0rd#" Output: True
10.	Write a def(task10) regular expression that matches a string containing a valid IPv6 address. Input: "2001:0db8:85a3:0000:0000:8a2e:0370:7334" Output: True.

```
___
Виконання роботи:
```Python
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


```
___
Результати:
```Python
Task 1: Input: test123, Matches: True
Task 2: Input: Test, Contains uppercase: True
Task 3: Input: 192.168.1.1, Valid IP: True
Task 4: Input: 23:59:59, Valid time: True
Task 5: Input: 12345-6789, Valid zip code: True
Task 6: Input: user_12, Valid username: True
Task 7: Input: 4123-4567-8912-3456, Valid credit card: True
Task 8: Input: 123-45-6789, Valid SSN: True
Task 9: Input: Password@123, Strong password: True
Task 10: Input: 2001:0db8:85a3:0000:0000:8a2e:0370:7334, Valid IPv6: True


```
___
Висновки:
The provided Python code includes ten tasks that use regular expressions (re module) to validate different types of input strings. Each task function checks for a specific pattern in the input string, prints the result, and returns a boolean indicating whether the input matches the expected pattern. 

___