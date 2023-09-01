"""
Abstract class: Has methods with code that is shared between children and others that must be implemented
Interfaces: Has only methods that must be implemented by the children
"""

from abc import ABC, abstractmethod


class Parent(ABC):
    @abstractmethod
    def show(cls):
        pass

    def display(self):
        print('Display')


class Child(Parent):
    def show(self):
        print('Show Child')


c = Child()
c.show()
c.display()