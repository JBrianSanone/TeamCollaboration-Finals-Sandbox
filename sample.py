# Sample Containers - Tuples
def get_student_info():
    name = "March"
    age = 7
    grade = 88.45
    return name, age, grade  # returns a tuple


print(f"Student Info: {get_student_info()}")


# Sample Containers - Lists
def add_shopping_list(item):
    shopping_list = ["bread", "eggs", "milk", item]
    print("The current shopping list is: ", end=" ")
    print(", ".join(shopping_list))


add_shopping_list("bananas")


# Sample Containers - Sets
def combine_sets(set1, set2):
    union_set = set1.union(set2)
    print(f"Union of the first and second set: {union_set}")


odd_set = {1, 3, 5, 7, 9}
even_set = {0, 2, 4, 6, 8}
print(combine_sets(odd_set, even_set))


# Sample Containers - Dictionaries
def get_game_developers():
    game_developers = {
        "Pokemon": "Game Freak",
        "Minecraft": "Mojang",
        "Honkai: Star Rail": "Hoyoverse",
        "Animal Crossing": "Nintendo",
        "Spider-Man": "Marvel"
    }

    del game_developers["Spider-Man"]
    return game_developers


def pretty_print(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")


print(pretty_print(get_game_developers()))


# Sample Control Structure - Sequential Execution
def print_order():
    print("This statement is printed first")
    print("This statement comes second")
    print("This gets to be printed last")


print_order()


# Sample Control Structure - Conditional
def check_number(num):#This checks you out hottie
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


# Sample Control Structure - Iterative While Loop
def print_winters(): #Ngayong alam mo na ang mga malalamig na months, gawin ko nang mainit buhay mo
    winter = ["December", "January", "February"]

    i = 0
    while i < len(winter):
        print(winter[i])
        i += 1


print_winters()
print(8==@ rosas)

# Sample Control Structure - Iterative For Loop
def find_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


result = find_factorial(5)
print(f"The factorial of 5 is: {result}")


# Sample Functions - Converts centimeters to inches
def cm_to_inches(cm):
    inches = cm / 2.54
    return inches


def converter(centimeter):
    inches = cm_to_inches(centimeter)
    print(f"{centimeter} centimeter/s is equal to {inches:.2f} inch/es.")


converter(12)  # calls the converter function and passes the value

