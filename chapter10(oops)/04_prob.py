class calculator:
    def __init__(self, n):
         self.n =n

    def square(self):
        print(f" The square is : {self.n * self.n}")
    def cube(self):
        print(f" The square is : {self.n **3}")
    def squareroot(self):
        print(f" The square is : {self.n ** 1/2}")

        @staticmethod
        def hello():
            print("Hello there!")

a = calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()