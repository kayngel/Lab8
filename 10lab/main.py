
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

