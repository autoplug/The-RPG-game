class Pokemon(object):
    def __init__(self, name, type, effectiveAgainst):
        self.name = name
        self.type = type
        self.effectiveAgainst = effectiveAgainst

    def isEffectiveAgainst(self, anotherPokemon):
        return self.effectiveAgainst == anotherPokemon.type


def initializePokemons():
    pokemon = []

    pokemon.append(Pokemon("Bulbasaur", "grass", "water"))
    pokemon.append(Pokemon("Pikachu", "electric", "water"))
    pokemon.append(Pokemon("Charizard", "fire", "grass"))
    pokemon.append(Pokemon("Pidgeot", "flying", "fighting"))
    pokemon.append(Pokemon("Kingler", "water", "fire"))

    return pokemon


pokemon = initializePokemons()

# Every pokemon has a name and a type.
# Certain types are effective against others, e.g. water is effective against fire.

# Ash has a few pokemon.
# A wild pokemon appeared!

wildPokemon = Pokemon("Oddish", "grass", "water")

for x in pokemon:
    if x.isEffectiveAgainst(wildPokemon):
        # if wildPokemon.isEffectiveAgainst(x):
        print(x.name)

# Which pokemon should Ash use?

print("I choose you, ")
