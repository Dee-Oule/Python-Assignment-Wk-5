class Superhero:
    def __init__(self, name, power, alias):
        self.name = name
        self.power = power
        self.alias = alias

    def introduce(self):
        return f"I am {self.alias}, also known as {self.name}. My superpower is {self.power}!"

# Adding inheritance
class FlyingHero(Superhero):
    def __init__(self, name, power, alias, flight_speed):
        super().__init__(name, power, alias)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.alias} soars through the skies at {self.flight_speed} km/h!"

# Example usage:
hero1 = FlyingHero("Clark Kent", "Super Strength", "Superman", 900)
print(hero1.introduce())
print(hero1.fly())
