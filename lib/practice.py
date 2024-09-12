##Dictonaries -
#Dictionaries are best used when there is a fixed name or value that we want to associate with a piece of data.
#An excellent analogy for a Python dictionary is...a dictionary!

states_cities = {
    "New_York": "Brooklyn",
    "Washington": "Seattle",
}

print(states_cities["New_York"])

#Dictionaries can also be used to store many types of data that would describe the dictionary object itself.
fruits_by_colors = {
    "red": ["cherries", "strawberries", "apples"],
    "purple": ["purple grapes", "plum"],
    "green": ["green apple", "kiwi", "green grape"]
}
print(fruits_by_colors["green"])