def main():

# Stores 5 survey points in a list, each with a velocity and travel time
    survey_points=[
    {"survey_point": 1, "velocity": 1500 , "travel_time": 0.5},
    {"survey_point": 2, "velocity": 2000 , "travel_time": 0.8},
    {"survey_point": 3, "velocity": 2500 , "travel_time": 1.2},
    {"survey_point": 4, "velocity": 3000 , "travel_time": 0.6},
    {"survey_point": 5, "velocity": 3500 , "travel_time": 0.9}
    ]

# Loops through each survey point
    for survey_point in survey_points:
       number=survey_point["survey_point"]
       velocity=survey_point["velocity"]
       travel_time=survey_point["travel_time"]
       print(f"Survey Point: {number}", f"Velocity: {velocity} m/s", f"Travel Time: {travel_time} s", f"Estimated Depth: {round(depth(velocity, travel_time), 2)} m", sep=", ")

# Calculates depth for each point
def depth (velocity,travel_time):
    return((velocity*travel_time)/2)


main()