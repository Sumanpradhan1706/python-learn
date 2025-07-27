class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        

p = programmer("suman", 2000000 , 245001)
print(p.name, p.salary , p.company, p.pin)


s = programmer("papan", 5000000 , 245089)
print(s.name, s.salary , s.company, s.pin)