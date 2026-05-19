# Reads survey.csv automatically
# Prints a clean report

import csv

def main():
    print("\n   Survey Seismic Report   \n")
    with open("result.csv", "w", newline="") as file:
        writer=csv.DictWriter(file, fieldnames=["Survey Point", "Estimated Depth", "Material"])
        writer.writeheader()

        with open("survey.csv") as file:
            reader=csv.DictReader(file)
            for row in reader:
                number=row["survey_point"]
                velocity = float(row["velocity"])
                travel_time = float(row["travel_time"])
                print(f"Survey Point: {number}", f"Velocity: {velocity} m/s", f"Travel Time: {travel_time} s", f"Depth: {round(depth(velocity, travel_time), 2)} m", f"Material: {classify(velocity)}", sep=", ")
                
                writer.writerow({
                    "Survey Point": number, 
                    "Estimated Depth": round(depth(velocity,travel_time),2), 
                    "Material": classify(velocity) 
                })
    

# Calculates depth for each point

def depth(velocity,travel_time):
    return velocity*travel_time/2

# Classifies rock type for each point

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

