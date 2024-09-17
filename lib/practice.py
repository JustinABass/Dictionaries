##Dictonaries -
#Dictionaries are best used when there is a fixed name or value that we want to associate with a piece of data.
#An excellent analogy for a Python dictionary is...a dictionary!

######################################################################################
#Getting data in dictonary with bracket notation
states_cities = {
    "New_York": "Brooklyn",
    "Washington": "Seattle",
}

print(states_cities["New_York"])

#Dictionaries can also be used to store many types of data that would describe the dictionary object itself.
fruits_by_colors = {
    "red": ["cherries", "strawberries", "apples"],
    "purple": ["purple grapes", "plum"],
    "green": ["green apple", "kiwi", "green grape"],
}
print(fruits_by_colors["green"])

#Using Dictionary Mapping in replacement of switch/case statements. Python does not have switch/case statements so
#we can use if/else statements for switch/ case logic
def get_size(size):
    if size == "tall":
        size = 12
        print(size)
    elif size == "grande":
        size = 16
        print(size)
    elif size == "venti":
        size == 20
        print(size)
    else:
        print("Sorry the chosen size is unavailable")
get_size("tall")

def get_size_dict_map(size):
    size_chart = {
        "tall": 12,
        "grande": 16,
        "venti": 20,
    }
    print(size_chart[size])
get_size_dict_map("tall")

######################################################################################
#Getting data with .get() method

#Using dict.get() method which allows us to avoid KeyErrors when a given argument does not match an immutable key in our dictionary
#It also allows us to recieve a value back if the given argument does not match a key, None - or a value provided as a optional second argument
#in the dict.get(arguement1, optional argument2) method
def get_student_grade_dict_map(student):
    student_dic = {
        "Tucker": 8,
        "Leah": 1,
        "Joeseph": 11
    }
    print(student_dic.get(student, "Please enter an existing enrolled student."))
get_student_grade_dict_map('Angela')

######################################################################################
#Setting data (update/add) with bracket notation

names = {
    "name1": "Mickie",
    "name2": "Trish"
}
print(names)

#updating
names["name1"] = "Ashley"
print(names)

#adding
names["name3"] = "Torrie"
print(names)

######################################################################################
#Setting data with dict.update()

names2 = {
    "name1": "Lori",
    "name2": "Cash",
}
print(names2)

#update multiple fileds
names2.update({"name1": "Dash", "name2": "Tkor"})
print(names2)

#add multiple fields
names2.update({"name3": "Kimo", "name4": "Rubina"})
print(names2)

#add and update fields simultaneusly
names2.update({"name1": "My name changed", "name5": "My name Is John I'm new"})
print(names2)


names3 = {
    "name1": "Henry"
}
print(names3)

#passing in an arrray of arrays
names3.update([["name1", "William"], ["name2", "Elizabeth"]])
print(names3)

#passing in an array of tuples
names3.update([('name2', 'Diana'), ('name3', 'Henry')])
print(names3)

#passing in a tuple of arrays
names3.update((['name3', 'Elizabeth'], ['name4', 'George']))
print(names3)

#passing in a tuple of tuples
names3.update((('name4', 'Henry'), ('name5', 'Megan')))
print(names3)

#using the assignment operator
names3.update(name5='Kate', name6='Meghan')
print(names3)

######################################################################################
#Iterating through dictionaries

x = {
    "key1": "val1",
    "key2": "val2",
    "key3": "val3",
    "key4": "val4"
}

#looping
for key in x:
    print('loop key', key)

for value in x:
    print('loop value', x[value])

#List comprehension
y = [key for key in x]
print(y)

z = [x[key] for key in x]
print(z)

#Using dict.items() allows us to get a list of tuples with both the key and the value returned or accessing the key or value independently

#Getting a list of tuples of the key/value pais
a = [item for item in x.items()]
print(a)

#Getting only our objects keys
b = [key for key, value in x.items()]
print(b)

#Getting only our objects values
c = [value for key, value in x.items()]
print(c)
