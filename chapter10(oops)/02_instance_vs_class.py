class Employee:
    language = "Py" # this is a class attribute
    salery = 1200000


suman = Employee()
suman.language = "JavaScript" # this is an instance attribute
print(suman.language, suman.salery)
