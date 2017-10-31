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
