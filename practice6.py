def depth(velocity, time):
    return (velocity * time) / 2

def classify(velocity):
    if velocity < 500:
        return "Air / loose soil"
    elif 500 <= velocity <= 1500:
        return "Sand / Clay"
    elif 1500 <= velocity <= 3000:
        return "Sandstone"
    elif 3000 <= velocity <= 5000:
        return "Limestone / Granite"
    else:
        return "Dense Crystalline Rock"