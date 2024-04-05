class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color
    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Meow")

class Fish(Pet):
    pass


p = Pet("Tim", 19)
c = Cat("Bill", 34, "blue")
f = Fish("Joe", 1)

class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Tim")
p2 = Person("Jill")

class Math:

    @staticmethod
    def add5(x):
        return x + 5
    @staticmethod
    def add10(x):
        return x + 10
    @staticmethod
    def pr():
        print("run")

Math.pr()

b = [["0,0", "0,1", "0,2"],
     ["1,0", "1,1", "1,2"],
     ["2,0", "2,1", "2,2"]]

if 0 not in b:
    print("Draw")