# Get season by the month number. Option 1
def season(numb):
    result = "A month with this number does not exist!"
    seasons = {
        "Winter": (1, 2, 12),
        "Spring": (3, 4, 5),
        "Summer": (6, 7, 8),
        "Autumn": (9, 10, 11)
    }
    for key, value in seasons.items():
        if numb in value:
            result = key
    return result


print("Option 1: ", season(7))


# Get season by the month number. Option 2
def season(numb):
    seasons = {
        1: "Winter",
        2: "Winter",
        3: "Spring",
        4: "Spring",
        5: "Spring",
        6: "Summer",
        7: "Summer",
        8: "Summer",
        9: "Autumn",
        10: "Autumn",
        11: "Autumn",
        12: "Winter"
    }
    result = seasons.get(numb, "A month with this number does not exist!")
    return result


print("Option 2: ", season(5))


def season(numb):
    seasons = ("Winter", "Spring", "Summer", "Autumn")
    months = ("January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December")
    table = {
        1: (0, 0),
        2: (0, 1),
        3: (1, 2),
        4: (1, 3),
        5: (1, 4),
        6: (2, 5),
        7: (2, 6),
        8: (2, 7),
        9: (3, 8),
        10: (3, 9),
        11: (3, 10),
        12: (0, 11)
    }
    result = "A month with this number does not exist!"
    if numb in table:
        index = table.get(numb)
        result = seasons[index[0]] + "  it is " + months[index[1]]
    return result


print("Option 3: ", season(6))


# task 2
def ku(arg1, arg2=":-)"):
    result = arg2
    if arg2 is not ku.__defaults__[0]:
        result = arg1 + arg2
    return result


print(ku(1))


# task 3
def func1(a):
    return a * a


def func2(b):
    return b + 1


def func3(c):
    return c - 1


def func4(a, b, c):
    return func1(a) + func2(b) + func3(c)


print(func4(1, 2, 3))


# task 4
def task4(x, y):
    if x > y:
        result = "x is greater than y " + str((x - y))
    elif x < y:
        result = "y is greater than x " + str((y - x))
    else:
        result = "x = y = " + str(x)
    return result


print(task4(2, 2))


# task 6
# print digits words and len
def wdl(s, ln):
    wrds = 0
    digits = 0
    i = 0
    while(i < ln):
        if str.isdigit(s[i]):
            digits += 1
        else:
            wrds += 1
        i += 1
    print("digits = %d, wrds = %d, len = %d" % (digits, wrds, ln))


# task 6
def get_sum_and_clean_string(s, ln):
    sum_digits = 0
    clean_string = ""
    i = 0
    while(i < ln):
        if str.isdigit(s[i]):
            sum_digits += int(s[i])
        else:
            clean_string += s[i]
        i += 1
    print("sum_digits = %d, clean_string = %s" % (sum_digits, clean_string))


# task 5
def task5(s):
    ln = len(s)
    if ln >= 30 and ln <= 50:
        wdl(s, ln)
    elif ln < 30:
        get_sum_and_clean_string(s, ln)
    # elif ln > 50:


task5("1kjgyu78,ytt1563f1g56dr1g56sg")
