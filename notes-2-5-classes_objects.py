# Classes and Objects

# Big Ideas:
#   - Classes allow us to couple data and functions together
#   - Objects are the ACTUAL representation of the classes


# Create a Pokemon class; this represents a Pokemon
class Pokemon:  # use a capital letter for class name
    def __init__(self):
        """A special method (function) called the
        Constructor. Contains all the properties/variables
        that describe a Pokemon."""
        self.name = ""
        self.id = 0
        self.weight = 0
        self.height = 0
        self.type = "normal"
        self.actual_cry = "Roooar!"

        print("A new Pokémon is born!")

        def cry(self) -> str:
            """Represents the sound a Pokemon makes
            
            Returns:
            - string representing the  sound it makes"""
            return f"{self.name} says, {self.actual_cry}"



# Create two Pokemon using our class
# Make one Pokemon that is Pikachu
pokemon_one = Pokemon()

# Change some properties in pokemon_one
#   Change its name
print(pokemon_one.name)  # ""
pokemon_one.name = "Pikachu"
print(pokemon_one.name)  # "Pikachu"

pokemon_one.id = 25
pokemon_one.type = "Electric"

print(pokemon_one.id)
print(pokemon_one.type)


# Make one Pokemon of your choice
# Store it in a variable called
#    pokemon_two
#    - you can make Squirtle
#       - id -> 4
#       - type -> "Water"
pokemon_two = Pokemon()

pokemon_two.name = "Squirtle"
pokemon_two.id = 4
pokemon_two.type = "water"

print(pokemon_two.name)
print(pokemon_two.id)
print(pokemon_two.type)

print(pokemon_one.cry())
print(pokemon_two.cry())