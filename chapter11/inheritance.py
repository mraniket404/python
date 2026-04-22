 # Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"
    
    def eat(self):
        return f"{self.name} is eating"

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent class constructor
        self.breed = breed
    
    # Override parent method
    def speak(self):
        return f"{self.name} says Woof! Woof!"
    
    # Child-specific method
    def wag_tail(self):
        return f"{self.name} is wagging tail"

# Usage
dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())        # Buddy says Woof! Woof!
print(dog.eat())          # Buddy is eating
print(dog.wag_tail())     # Buddy is wagging tail