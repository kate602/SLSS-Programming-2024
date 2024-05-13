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
        self.actual_cry = "Roooooooooooooar!"

        print("A new Pokémon is born!")

    def cry(self) -> str:
        """Represents the sound a Pokemon makes

        Returns:
            - string representing the sound it makes"""
        return f'{self.name} says, "{self.actual_cry}"!'

    def eat(self, food: str) -> str:
        """Represents feeding the Pokemon

        Params:
            - food: what food you feed it

        Return:
            - what it says after eating it"""
        if food.lower() == "berry":
            return f'{self.name} ate the berry and says, "YUM!"'
        elif food.lower() == "potion":
            return f"{self.name} consumed the potion and feels healthier!"
        else:
            return f"{self.name} batted the {food} away."


# Create a new child class of Pokemon
class Pikachu(Pokemon):
    def __init__(self, name="Pikachu"):
        # Call constructor of parent class
        super().__init__()

        # Assign the default values to properties
        self.name = name
        self.id = 25
        self.type = "Electric"
        self.actual_cry = "Pikachu"

    def thundershock(self, defender: Pokemon) -> str:
        """Simulate a thundershock attack against
        another Pokemon.

        Params:
            - defender: defending Pokemon

        Returns:
            str representing result of attack.
        """
        response = f"{self.name} used thundershock on {defender.name}!"

        if defender.type.lower() in ["water", "flying"]:
            response = response + " It was super effective."

        return response


# Create a new child-class of pokemon for the type of your choice
class Butterfree(Pokemon):
 def __init__(self, name="Butterfree"):
        super().__init__()

        self.name = name
        self.id = 12
        self.type = "Bug"

 def bugBuzz(self, defender: Pokemon) -> str:
        response = f"{self.name} used bug buzz on {defender.name}!"

        if defender.type.lower() in ["grass", "psychic", "dark"]:
            response = response + " It was effective."

        if defender.type.lower() in ["fighting", "flying", "poison", "ghost", "steel", "fire", "fairy"]:
            response = response + "It was not effective."

        return response

# Create two Pokemon using our class
# Make one Pokemon that is Pikachu
pokemon_one = Pokemon()
pokemon_one.name = "Pikachu"
pokemon_one.id = 25
pokemon_one.type = "Electric"
pokemon_one.actual_cry = "Pikachu"

# Make one Pokemon of your choice
pokemon_two = Pokemon()

pokemon_two.name = "Squirtle"
pokemon_two.id = 4
pokemon_two.type = "water"
pokemon_two.actual_cry = "GRRraaggrrggg"

# Test the eat method
print(pokemon_one.eat("berry"))

pikachu_one = Pikachu()
pikachu_two = Pikachu("Speedy")

# Third pokemon
pokemon_three = Pokemon()
pokemon_three.name = "Jigglypuff"
pokemon_three.id = 39
pokemon_three.type = "fairy"