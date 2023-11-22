'''
This is a collection of random functions that uses different datatypes
where each function utilizes a different data type. This also includes
python concepts such as sequential execution.
'''

def get_student_info(): # Sample Containers - Tuples
    name = "March"
    age = 7
    grade = 88.45
    return name, age, grade

print(f"Student Info: {get_student_info()}")

def add_shopping_list(item): # Sample Containers - Lists
    shoppingList = ["bread", "eggs", "milk", "flour", "baking powder", "sniffing powder",
                     "rat poison", "gin", "rum", item]
    print("The current shopping list is: ", end=" ")
    print(", ".join(shoppingList))

add_shopping_list("bananas")

def combine_sets(set1, set2): # Sample Containers - Sets
    unionSet = set1.union(set2)
    print(f"Union of the first and second set: {unionSet}")

oddSet = {1, 3, 5, 7, 9}
evenSet = {0, 2, 4, 6, 8}
print(combine_sets(oddSet, evenSet))

def get_game_developers(): # Sample Containers - Dictionaries
    gameDevelopers = {
        "Pokemon": "Game Freak", 
        "Minecraft": "Mojang",
        "Honkai: Star Rail": "Hoyoverse",
        "Animal Crossing": "Nintendo",
        "Spider-Man": "Marvel"
    }

    del gameDevelopers["Spider-Man"]
    return gameDevelopers

def pretty_print(dictionary): # Iterates the values of game_developer dictionary
    for key, value in dictionary.items():
        print(f"{key}: {value}")

print(pretty_print(get_game_developers()))

def print_order(): # Sample Control Structure - Sequential Execution
    print("This statement is printed first")
    print("This statement comes second")
    print("This gets to be printed last")

print_order()

def check_number(num): # Sample Control Structure - Conditional
    if num is None:
        return 'is None'
    elif num < 0:
        return 'is negative'
    elif num > 0:
        return 'is positive'
    else:
        return 'is zero'

number = 3
print(number, check_number(number))


def print_winters(): # Sample Control Structure - Iterative While Loop
    winter = ["December", "January", "February"]

    i = 0
    while i < len(winter):
        print(winter[i])
        i += 1

print_winters()

def find_factorial(num): # Sample Control Structure - Iterative For Loop
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

result = find_factorial(5)
print(f"The factorial of 5 is: {result}")

def cm_to_inches(cm): # Sample Functions - Converts centimeters to inches
    inches = cm / 2.54
    return inches

def converter(centimeter): # Prints the result of function cm_to_inches
    inches = cm_to_inches(centimeter)
    print(f"{centimeter} centimeter/s is equal to {inches:.2f} inch/es.")

converter(12)