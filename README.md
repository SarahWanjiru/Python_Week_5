# Python_Week_5
Week 5: Object-Oriented Programming (OOP)

### README.md: Object-Oriented Programming Concepts in Python

## Overview
This project demonstrates key principles of **Object-Oriented Programming (OOP)** in Python, focusing on **encapsulation**, **inheritance**, and **polymorphism**. The examples use a **Superhero** and a **Vehicle** system to showcase how OOP concepts can be applied effectively.

---

## Features

### 1. **Superhero Class System**
   - A `Superhero` class encapsulates attributes like `name`, `power`, and `strength_level`.
   - A subclass, `FlyingSuperhero`, extends `Superhero` by adding a `flight_speed` attribute.
   - Demonstrates **encapsulation** with private attributes (`__strength_level`) and getters/setters.

#### Example Usage:
```python
# Create a superhero
thor = Superhero("Thor", "Thunder", 90)
print(thor.display_info())  # Output: Thor has the power of Thunder.
print(thor.get_strength_level())  # Access private strength level: 90

# Create a flying superhero
superman = FlyingSuperhero("Superman", "Flight", 100, 500)
print(superman.display_info())  # Output: Superman has the power of Flight. They can fly at 500 mph.
```

---

### 2. **Polymorphism with Vehicles**
   - A `Vehicle` parent class with a shared `move()` method.
   - Subclasses (`Car`, `Plane`, `Boat`) override `move()` with unique implementations.
   - Demonstrates **polymorphism**, where the same method behaves differently based on the object type.

#### Example Usage:
```python
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    print(vehicle.move())
# Output:
# Driving 🚗
# Flying ✈️
# Sailing 🚤
```

---

## Concepts Highlighted

### 1. **Encapsulation**
   - Attributes like `__strength_level` are private and accessed via getters and setters, ensuring data integrity.

### 2. **Inheritance**
   - Code reusability is achieved by having `FlyingSuperhero` inherit from `Superhero`.

### 3. **Polymorphism**
   - Multiple subclasses (`Car`, `Plane`, `Boat`) override a common method to perform unique behaviors.

---

## Learning Resources
For more information on the concepts used in this project, check out the following resources:

- [Python Classes and Objects (Real Python)](https://realpython.com/python3-object-oriented-programming/)
- [Encapsulation in Python (GeeksforGeeks)](https://www.geeksforgeeks.org/encapsulation-in-python/)
- [Polymorphism in Python (W3Schools)](https://www.w3schools.com/python/python_polymorphism.asp)
- [Python Official Documentation: Classes](https://docs.python.org/3/tutorial/classes.html)

---

## Contribution
Feel free to fork this repository and extend the project by adding more functionality, such as:
- Additional subclasses for both `Superhero` and `Vehicle`.
- Integration of the `Superhero` and `Vehicle` systems into a combined storyline or game.

---

This project is a beginner-friendly way to dive into Python OOP principles. Start coding and enjoy the power of Python! 😊