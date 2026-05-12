def main():
    # Asks for a seismic wave velocity (float) in m/s
    velocity=float(input("What's the value of seismic wave velocity in m/s? "))
    material=classify(velocity)

    print(f"Seismic velocity: {velocity:.2f} m/s")
    print(f"Material type: {material}")

# Classifies what material the wave is travelling through based on the velocity
def classify(velocity):
    if velocity <500:
        return "Air / loose soil"
    elif 500<= velocity <=1500:
        return "Sand / Clay"
    elif 1500<= velocity <=3000:
        return "Sandstone"
    elif 3000<= velocity <=5000:
        return "Limestone / Granite"
    else:
        return "Dense Crystalline Rock"
    
main()