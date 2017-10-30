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


print(season(7))
