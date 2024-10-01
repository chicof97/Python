from enum import Enum
from typing import Self

# Basic class (OOP), initializer and  dunder methods


class Gender(Enum):
    Male = "male"
    Female = "female"
    Other = "other"


class Person:
    def __init__(self, name: str, age: int, gender: Gender, partner=None) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.partner = partner

    def __str__(self) -> str:
        return f"{self.name}, {self.age}, {self.gender}"

    def present_itself(self) -> None:
        print(
            "My name is",
            self.name,
            ",I've",
            self.age,
            " years old and my gender is",
            self.gender.value,
        )

    def hasAPartner(self) -> None:
        if self.partner:
            print(self.name, "has a partner, whose name is", self.partner.name + ".")
        else:
            print(self.name, "has no partner.")

    def marry(self, partner: Self) -> None:
        self.partner = partner
        partner.partner = self
        print(self.name + " married " + partner.name + "!")


joao = Person("João", 25, Gender.Male.value)
ana = Person("Ana", 32, Gender.Female.value)
antonio = Person("António", 21, Gender.Male.value)


print(joao)
print(ana)

joao.marry(ana)

joao.hasAPartner()
ana.hasAPartner()
antonio.hasAPartner()

# joao.present_itself()
