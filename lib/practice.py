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
