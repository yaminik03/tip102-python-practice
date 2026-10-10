'''
Problem 1: New Horizons
Understand
- Create an instance of the Villager class.
- Store it in a variable named apollo.
Plan
1. Pass "Apollo", "Eagle", and "pah" to the constructor.
2. Store the object in apollo.
Implement
'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

apollo = Villager("Apollo", "Eagle", "pah")

print(apollo.name)
print(apollo.species)
print(apollo.catchphrase)
print(apollo.furniture)


'''
Problem 2: Greet Player
Understand
- Add a greet_player() method to the class.
- Create a bones object and print a personalized greeting.
Plan
1. Define greet_player(self, player_name) inside the class.
2. Return a formatted string using the villager's attributes.
3. Instantiate bones and call the method.
Implement
'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

apollo = Villager("Apollo", "Eagle", "pah")
bones = Villager("Bones", "Dog", "yip yip")

print(bones.greet_player("Sam"))


'''
Problem 3: Update Catchphrase
Understand
- Change the catchphrase attribute of bones.
- The updated catchphrase should appear when the villager greets the player.
Plan
1. Assign "ruff it up" to bones.catchphrase.
2. Call greet_player() to display the updated greeting.
Implement
'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

apollo = Villager("Apollo", "Eagle", "pah")
bones = Villager("Bones", "Dog", "yip yip")

bones.catchphrase = "ruff it up"

print(bones.greet_player("Samia"))


'''
Problem 4: Set Character
Understand
- Create a setter method called set_catchphrase().
- A valid catchphrase must contain fewer than 20 characters and only alphabetic characters or whitespace.
- Update the attribute only when the catchphrase is valid.
Plan
1. Use len() to check the string length.
2. Use isalpha() on each character to check for letters, while allowing whitespace with isspace().
3. If both conditions are satisfied, update the attribute and print the success message.
4. Otherwise, print the error message without changing the existing catchphrase.
Implement
'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchphrase):
        if (len(new_catchphrase) < 20 and
            all(char.isalpha() or char.isspace() for char in new_catchphrase)):
            self.catchphrase = new_catchphrase
            print("Catchphrase updated")
        else:
            print("Invalid catchphrase")

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)

alice.set_catchphrase("#?!")
print(alice.catchphrase)


'''
Problem 5: Add Furniture
Understand
- Add an add_item() method to the Villager class.
- Only five specific furniture items are valid.
- Valid items are added to the furniture list; invalid items are ignored.
Plan
1. Create a list containing the allowed furniture items.
2. Check whether item_name is in that list.
3. If valid, append it to self.furniture.
Implement
'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchphrase):
        if (len(new_catchphrase) < 20 and
            all(char.isalpha() or char.isspace() for char in new_catchphrase)):
            self.catchphrase = new_catchphrase
            print("Catchphrase updated")
        else:
            print("Invalid catchphrase")

    def add_item(self, item_name):
        valid_items = [
            "acoustic guitar",
            "ironwood kitchenette",
            "rattan armchair",
            "kotatsu",
            "cacao tree"
        ]

        if item_name in valid_items:
            self.furniture.append(item_name)

alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)