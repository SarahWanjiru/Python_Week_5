# Parent Class
class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self.__strength_level = strength_level  # Private attribute

    # Method to display superhero details
    def display_info(self):
        return f"{self.name} has the power of {self.power}."

    # Getter for the private attribute
    def get_strength_level(self):
        return self.__strength_level

    # Setter for the private attribute
    def set_strength_level(self, level):
        if level >= 0:  # Ensure strength level is valid
            self.__strength_level = level
        else:
            print("Strength level must be positive.")

# Child Class
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength_level, flight_speed):
        super().__init__(name, power, strength_level)
        self.flight_speed = flight_speed

    # Overriding a method to include flight speed
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} They can fly at {self.flight_speed} mph."

# Create a superhero
hero = Superhero("Thor", "Thunder", 90)
print(hero.display_info())  # Output: Thor has the power of Thunder.
print(f"Strength Level: {hero.get_strength_level()}")  # Output: 90

# Create a flying superhero
flying_hero = FlyingSuperhero("Superman", "Flight", 100, 500)
print(flying_hero.display_info())  # Output: Superman has the power of Flight. They can fly at 500 mph.
