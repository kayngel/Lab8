#task1
def check_truth(a, b, c):
    return (a and b) or c

#example
#print(check_truth(True, False, True))

#task2
def logical_equivalence(a, b):
    return a==b

#example
#print(logical_equivalence(True, True))
#print(logical_equivalence(True, False))

#task3
def xor(a, b):
    return(a or b) and not (a and b)

#example
#print(xor(True, False))
#print(xor(True, True))


#task4
def greet(is_hello):
    if is_hello:
        return "Hello, world!"
    else:
        return  "goodbye, world!"

#example
#print(greet(True))
#print(greet(False))


#task5
def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y and x != z and y != z:
        return "all different"
    else:
        return "neither"

#example
#print(nested_condition(3, 3, 3))
#print(nested_condition(3, 4, 5))


#task6
def count_true(bool_list):
    count = 0
    for value in bool_list:
        if value:
            count +=1
    return count

#example
#print(count_true([True, False, True, False, True]))


#task7
def parity(num):
    binary_representation = bin(num)[2:]
    count_ones = binary_representation.count('1')
    return count_ones % 2 == 0

#exampel
#print(parity(9))


#task8
def majority_vote(a, b, c):
    return (a + b + c) > 1.5

#example
#print(majority_vote(True, True, False))


#task9
def switch(boolean_value):
    return not boolean_value

#example
#print(switch(True))


#task10
def ternary_check(condition, result_true, result_false):
    return result_true if condition else result_false

#example
#print(ternary_check(True, "yes", "no"))


#task11
def validate(x, y, z):
    return x or (y and z)

#example
#print(validate(True, False, True))


#task12
def chain_check(a, b, c):
    if a < b < c:
        return "increasing"
    elif a > b > c:
        return "decreasing"
    else:
        return "neither"

#example
#print(chain_check(1, 2, 3))
#print(chain_check(3, 2, 1))


#task13
def filter_true(bool_list):
    return [value for value in bool_list if value]

#example
#print(filter_true([True, False, True, False]))


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
#print(multiplexer(False, False, True, 10))


