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
