# class Employee:
#     language = "Py" # this is a class attribute
#     salery = 1200000

# def __init__(self):
#     print("I am creating an object")


# def getInfo(self):
#     print(f"The language is {self.language}. The salery is {self.salery}")

#     @staticmethod
#     def greet():
#         print("Good morning!")

# suman = Employee()
# suman.name= "suman" # this is an object attribute
# print(suman.name, suman.salery)


class Employee:
    language = "Py"       # class attribute
    salary = 1200000      # fixed spelling

    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod  
    def greet():
        print("Good morning!")

suman = Employee("suman", 2000000,"java")
suman.name = "suman"     # object attribute
print(suman.name, suman.salary)
