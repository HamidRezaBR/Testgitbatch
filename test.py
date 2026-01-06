from abc import ABC

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Man(Person):
    def hello():
        print("Hello")


if __name__ == "__main__":
    d = Man()

    