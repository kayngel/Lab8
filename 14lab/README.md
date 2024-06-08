Лабораторна робота №14: Boolean Expressions and Conditional Statements
___
Мета роботи:
Write a script to analyze Boolean expressions and use
conditional statements to solve various problems. Each task will require you to
manipulate and evaluate Boolean conditions in different contexts.
___
Опис завдання:
```Python

Task 1: Basic Boolean Operations
Write a function check_truth that takes three boolean parameters ( a , b , c )
and returns the result of the expression (a and b) or c .
Example of function usage:
Task 2: Logical Equivalence
Write a function logical_equivalence that takes two boolean parameters and
returns True if they are logically equivalent, otherwise False .
Example of function usage:
Task 3: Exclusive Or (XOR)
Write a function xor that takes two boolean arguments and returns True if
exactly one of the arguments is True .
Example of function usage:
print(check_truth(True, False, True)) # True
print(logical_equivalence(True, True)) # True
print(logical_equivalence(True, False)) # False
Task 4: Conditional Greeting
Write a function greet that takes a boolean value. If True , the function should
return "Hello, World!", otherwise it should return "Goodbye, World!".
Example of function usage:
Task 5: Nested Conditions
Write a function nested_condition that takes three integers ( x , y , z ). The
function should return "All same" if all three are equal, "All different" if they are all
different, and "Neither" otherwise.
Example of function usage:
Task 6: Conditional Counting
Write a function count_true that accepts a list of boolean values and returns the
count of how many are True .
Example of function usage:
print(xor(True, False)) # True
print(xor(True, True)) # False
print(greet(True)) # Hello, World!
print(greet(False)) # Goodbye, World!
print(nested_condition(3, 3, 3)) # All same
print(nested_condition(3, 4, 5)) # All different
Task 7: Boolean Parity
Write a function parity that accepts an integer and returns True if the number
of 1 s in the binary representation of the number is even, otherwise False .
Example of function usage:
Task 8: Majority Vote
Write a function majority_vote that takes three boolean inputs and returns
True if more than half of them are True , otherwise False .
Example of function usage:
Task 9: Boolean Switch
Write a function switch that takes a boolean value and returns its opposite.
Example of function usage:
Task 10: Ternary Operator Simulation
Write a function ternary_check that simulates a ternary operator. It takes three
parameters: a boolean condition, a result if true, and a result if false. It returns the
print(count_true([True, False, True, False, True])) # 3
print(parity(3)) # False (binary 11)
print(majority_vote(True, True, False)) # True
print(switch(True)) # False
corresponding result based on the condition.
Example of function usage:
Task 11: Validate Combination
Write a function validate that takes three booleans ( x , y , z ) and returns
True if x is True or both y and z are True , otherwise False .
Example of function usage:
Task 12: Condition Chain
Write a function chain_check that evaluates a sequence of conditions. It takes
three integers and returns "Increasing" if they are in strictly increasing order,
"Decreasing" if in strictly decreasing order, or "Neither" otherwise.
Example of function usage:
Task 13: Boolean Filter
Write a function filter_true that takes a list of boolean values and returns a
new list containing only the True values.
Example of function usage:
print(ternary_check(True, "Yes", "No")) # Yes
print(validate(True, False, True)) # True
print(chain_check(1, 2, 3)) # Increasing
print(chain_check(3, 2, 1)) # Decreasing
Task 14: Conditional Multiplexer
Write a function multiplexer that takes four parameters: three boolean inputs
and one integer. If the first boolean is True , return double the integer. If the
second is True , return triple the integer. If the third is True , return the integer
minus five. If none are True , return the integer unchanged.
Example of function usage:
print
(filter_true([True, False, True, False])) # [True, True]
print(multiplexer(False, False, True, 10)) # 5
```
___
Виконання роботи:
```Python
#task1
def check_truth(a, b, c):
    return (a and b) or c

#example
print(check_truth(True, False, True))

#task2
def logical_equivalence(a, b):
    return a==b

#example
print(logical_equivalence(True, True))
print(logical_equivalence(True, False))

#task3
def xor(a, b):
    return(a or b) and not (a and b)

#example
print(xor(True, False))
print(xor(True, True))


#task4
def greet(is_hello):
    if is_hello:
        return "Hello, world!"
    else:
        return  "goodbye, world!"

#example
print(greet(True))
print(greet(False))


#task5
def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y and x != z and y != z:
        return "all different"
    else:
        return "neither"

#example
print(nested_condition(3, 3, 3))
print(nested_condition(3, 4, 5))


#task6
def count_true(bool_list):
    count = 0
    for value in bool_list:
        if value:
            count +=1
    return count

#example
print(count_true([True, False, True, False, True]))


#task7
def parity(num):
    binary_representation = bin(num)[2:]
    count_ones = binary_representation.count('1')
    return count_ones % 2 == 0

#exampel
print(parity(9))


#task8
def majority_vote(a, b, c):
    return (a + b + c) > 1.5

#example
print(majority_vote(True, True, False))


#task9
def switch(boolean_value):
    return not boolean_value

#example
print(switch(True))


#task10
def ternary_check(condition, result_true, result_false):
    return result_true if condition else result_false

#example
print(ternary_check(True, "yes", "no"))


#task11
def validate(x, y, z):
    return x or (y and z)

#example
print(validate(True, False, True))


#task12
def chain_check(a, b, c):
    if a < b < c:
        return "increasing"
    elif a > b > c:
        return "decreasing"
    else:
        return "neither"

#example
print(chain_check(1, 2, 3))
print(chain_check(3, 2, 1))


#task13
def filter_true(bool_list):
    return [value for value in bool_list if value]

#example
print(filter_true([True, False, True, False]))


#tasl14
def multiplexer(bool1, bool2, bool3, num):
    if bool1:
        return num * 2
    elif bool2:
        return num * 3
    elif bool3:
        return num -5
    else:
        return num

#example
print(multiplexer(False, False, True, 10))



```
___
Результати:
```Python
Hello, world!
goodbye, world!
All same
all different
3
True
True
False
yes
True
increasing
decreasing
[True, True]
5

```
___
Висновки:
Task 1: Check Truth

Returns the result of the logical expression (a and b) or c.
Task 2: Logical Equivalence

Returns True if a is equal to b, otherwise returns False.
Task 3: XOR Function

Returns the result of the exclusive OR operation between a and b.
Task 4: Greet Function

Returns a greeting message based on the value of is_hello.
Task 5: Nested Condition

Compares three values x, y, and z, and returns different messages based on their equality.
Task 6: Count True

Counts the number of True values in a boolean list.
Task 7: Parity Check

Checks if the number of ones in the binary representation of num is even.
Task 8: Majority Vote

Returns True if the sum of a, b, and c is greater than 1.5, otherwise returns False.
Task 9: Switch Function

Returns the opposite boolean value of boolean_value.
Task 10: Ternary Check

Returns result_true if condition is True, otherwise returns result_false.
Task 11: Validate Function

Returns True if x is True, or if both y and z are True, otherwise returns False.
Task 12: Chain Check

Determines if three values a, b, and c form an increasing, decreasing, or neither chain.
Task 13: Filter True

Filters and returns a list of only True values from bool_list.
Task 14: Multiplexer

Returns different operations on num based on the values of bool1, bool2, and bool3.
___