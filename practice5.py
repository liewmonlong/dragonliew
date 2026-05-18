import statistics
import random

def main():
# Stores a list of seismic velocities from different survey points
    print("=== Seismic Survey Statistics ===")
    
    velocities=[1500, 2000, 2500, 3000, 3500, 1800, 2200]

    print(f"\nSurvey Velocities: {velocities}")
    print(f"\nMean Velocity:{round(mean(velocities),2)} m/s")
    print(f"Median Velocity:{round(median(velocities),2)} m/s")
    print(f"Std Deviation Velocity:{round(stdev(velocities),2)} m/s")
    print(f"Simulated Reading: {simulated(velocities)} m/s")

def mean(velocities):
    mean=statistics.mean(velocities)
    return mean

def median(velocities):
    median=statistics.median(velocities)
    return median

def stdev(velocities):
    stdev=statistics.stdev(velocities)
    return stdev


def simulated(velocities):
    simulated=random.choice(velocities)
    return simulated


main()