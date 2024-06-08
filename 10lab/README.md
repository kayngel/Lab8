Лабораторна робота №10: OOP in Python
___
Мета роботи:
create classes instead of functions.
___
Опис завдання:
```Python

Task 1: Class Creation
Create a Python class named “Student” with the following attributes: - name -
age - grade
Example of class usage:
student = Student(name="Ivan", age=30, grade="2")
Task 2: Create Method
Add a method named display_info() to the Student class that prints the
student’s name, age, and grade in the format “Name: [name], Age: [age],
Grade: [grade]”.
Example of class usage:
student = Student(name="Ivan", age=30, grade="2")
print(student.display_info()) # Name: Ivan, Age: 30, Grade: 2
Task 3: Inheritance
Create two classes: Animal and Dog. Animal should have attributes name
and sound. Add a make_sound() method to Animal that returns the string
“[name]: [sound]”. Dog should inherit from Animal and have an additional
attribute breed.
Example of class usage:
animal = Animal(name="Lala", sound="￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿ ￿￿￿￿")
dog = Dog(name="Lala", sound="Auuuuuuu", breed="Spitz")
print(animal.make_sound()) # Lala: ￿￿￿￿￿￿￿￿ ￿￿￿￿￿￿ ￿￿￿￿
print(dog.make_sound()) # Lala: Auuuuuuu
1
Task 4: Polymorphism
Create a class Bird with a method fly() that returns None. Then create two
subclasses: Sparrow and Penguin. Override the fly() method in Sparrow
to return the string “Sparrow flies high” and in Penguin to return the string
“Penguin cannot fly”.
Example of class usage:
bird = Bird()
sparrow = Sparrow()
penguin = Penguin()
print(bird.fly()) # None
print(sparrow.fly()) # Sparrow flies high
print(penguin.fly()) # Penguin cannot fly
Task 5: Encapsulation
Create a class Encapsulation with the following attributes:
• public
• _private
• __protected
Example of class usage:
obj = Encapsulation(1, 2, 3)
print(obj.public) # 1
print(obj._private) # 2
print(obj._Encapsulation__protected) # 3
print(obj.__protected) # AttributeError
Task 6: Rectangle
Create a Rectangle class that has width and height attributes, and a
calculate_perimeter() method that returns the perimeter of the shape.
Example of class usage:
rectangle = Rectangle(width=5, height=4)
print(rectangle.calculate_perimeter()) # 18
2
Task 7: AverageCalculator
Create an AverageCalculator class that has a numbers attribute and takes a
list of integers. The class should have a calculate_average() method that
returns the arithmetic mean of the numbers in the list.
Example of class usage:
numbers = [5, 10, 15, 20]
avg_calculator = AverageCalculator(numbers)
print(avg_calculator.calculate_average()) # Expected output: 12.5
3
```
___
Виконання роботи:
```Python

#task1,2
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

student = Student(name= "Ivan", age= 30, grade= "72")
print(student.display_info())


#task3
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name}: {self.sound}"


class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed

animal = Animal(name = "Lala", sound="         ")
dog = Dog(name ="Lala", sound="Auuuuuu", breed="Spitz")

print(animal.make_sound()) #Lala:
print(dog.make_sound()) #Lala: Auuuuuu

#task4

class Bird:
    def fly(self):
        return None

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies high"

class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly"


bird = Bird()
sparrow = Sparrow()
penguin = Penguin()

print(bird.fly())
print(sparrow.fly())
print(penguin.fly())

#task5
class Encapsulation:
    def __init__(self, public, privat, protected):
        self.public = public
        self._privat = privat
        self.__protected = protected

#example
obj = Encapsulation(1, 2, 3)

print(obj.public) #1
print(obj._privat) #2
print(obj._Encapsulation__protected) #3
try:
    print(obj.__protected)
except AttributeError:
    print("AttributeError: '__protected' attribute is not accessible")
print(obj.__protected) # AttributeError

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(width = 5, height=4)
print(rectangle.calculate_perimeter()) #18

#task7

class AverageCalc:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_avg(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

#example
numbers = [5, 10, 15, 20]
avg_calc = AverageCalc(numbers)
print(avg_calc.calculate_avg()) #12.5


```
___
Результати:
```Python
Name: Ivan, Age: 30, Grade: 72
Lala:          
Lala: Auuuuuu
None
Sparrow flies high
Penguin cannot fly
1
2
3
AttributeError: '__protected' attribute is not accessible

```
___
Висновки:
The provided Python code includes multiple tasks demonstrating various object-oriented programming (OOP) concepts, including class creation, inheritance, encapsulation, method overriding, and encapsulation. Each task showcases a specific aspect of OOP with relevant examples.
___