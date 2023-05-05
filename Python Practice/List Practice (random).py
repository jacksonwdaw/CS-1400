import random

def random_colors():
    warm = ["red", "orange", "yellow", "burgundy", "pink", "rose", "pumpkin", "marigold", "gold", "citron", "amber"]
    cool = ["blue", "green", "purple", "cyan", "violet", "indigo", "azure", "teal", "mint", "lime", "emerald"]
    neutral = ["black", "white", "gray", "grey", "brown", "beige"]
    colors = ["red", "black", "pink", "beige", "dark green", "azure", "amber", "light yellow"]
    warm_count = 0
    cool_count = 0
    neutral_count = 0
    misc_count = 0
    for color in colors:
       if color in warm:
          warm_count += 1
       elif color in cool:
          cool_count += 1
       elif color in neutral:
          neutral_count += 1
       else:
         misc_count += 1
    print("The total # of colors is ", len(colors))
    print("There are ", warm_count, " warm colors")
    print("There are ", cool_count, " cool colors")
    print("There are ", neutral_count, " neutral colors")
    print("There are ", misc_count, " miscellaneous colors")


def random_thirds():
    numbers = []
    for i in range(9):
        numbers.append(random.randint(0, 100))
    length = len(numbers)
    start = length // 3
    stop = length // 3 * 2
    middle = numbers[start:stop]
    print(numbers)
    print("The middle is ", middle)

def random_add():
    numbers = []
    total = 0
    for i in range(20):
        numbers.append(random.randint(0, 100))
    for number in numbers:
        total += number
    print("The sum of numbers is ", total)
    print(sum(numbers))

def random_list():
    numbers = []
    odd = []
    even = []
    for i in range(20):
        numbers.append(random.randint(0, 100))

    for number in numbers:
        if number % 2 == 0:
          even.append(number)
        else:
          odd.append(number)

    print("The odd numbers: ", odd)
    print("The even numbers: ", even)
    print(len(odd) + len(even))

def main():
    random_list()

