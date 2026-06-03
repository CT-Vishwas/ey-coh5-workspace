class Person:
    # name = "Vishwas"
    # city = "pune"
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def display(self):
        print(f"Name:{self.name}, City:{self.city}")


class User(Person):
    def __init__(self, name, city, age):
        super().__init__(name, city)
        self.age = age

    def greet(self):
        pass

p1 = Person("Vishwas", "Pune")
p2 = Person("Rani","Delhi")
p3 = User("Alice", "Pune",23)

# p1 = Person()
# p2 = Person()

p1.display()
p2.display()
p3.display()