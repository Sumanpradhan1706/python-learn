class Employee:
    language = "Py" # this is a class attribute
    salery = 1200000


suman = Employee()
suman.name = "suman" # this is an object attribute
print(suman.name ,suman.language, suman.salery)

rohan = Employee()
rohan.name = "rohan"
print( rohan.name, rohan.salery, rohan.language )


# Here name is object attribute and salery and language are class attributes. as they directly to the class.