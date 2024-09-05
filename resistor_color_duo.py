def value(colors):
    bands = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    value = ""
    if colors[0] in bands and colors[1] in bands:
        value = value + str(bands.index(colors[0]))
        value = value + str(bands.index(colors[1]))
        return int(value)
