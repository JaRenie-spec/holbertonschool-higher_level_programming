#!/user/bin/python3

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class representing an Animal.
    This class enforces that all subclasses must implement the `sound` method.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should be implemented by all subclasses.
        This method is meant to return the sound that the specific animal makes
        """
        pass

class Dog(Animal):
    """
    A subclass of Animal representing a Dog.
    This class implements the `sound` method to return the sound a dog makes.
    """

    def sound(self):
        """
        Return the sound made by a Dog (Bark).
        """
        return "Bark"

class Cat(Animal):
    """
    A subclass of Animal representing a Cat.
    This class implements the `sound` method to return the sound a cat makes.
    """

    def sound(self):
        """
        Return the sound made by a Cat (Meow).
        """
        return "Meow"
