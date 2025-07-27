class Employee:
    language = "Py" # this is a class attribute
    salery = 1200000

def getInfo(self):
    print(f"The language is {self.language}. The salery is {self.salery}")

suman = Employee()
suman.language = "javaScript" # this is an object attribute
suman.getInfo()
# Employee.getInfo(suman)
