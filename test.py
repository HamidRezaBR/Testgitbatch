from abc import ABC

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Man(Person):
    def hello():
        print("Hello")
        print("Hello again")


if __name__ == "__main__":
    d = Man()

    