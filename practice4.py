def main():
    print("\n   Seismic Estimated Depth Calculator   ")

    velocity=get_velocity()
    time=get_time()
    
    print(f"\nVelocity: {velocity} m/s")
    print(f"Travel Time: {time} s")
    print(f"Estimated Depth: {round(depth(velocity,time),2)} m")

def get_velocity():
    while True:
        try:
            velocity= float(input("\nWhat's the seismic wave velocity in m/s? "))
        
        except ValueError:
            print("Invalid! Please enter a number.")
        else:
            if velocity<=0:
                print("Invalid! Velocity cannot be negative.")
            else:
                break
    
    return velocity

def get_time():
    while True:
        try:
            time= float(input("What's the travel time in s? "))
        
        except ValueError:
            print("Invalid! Please enter a number.")
        
        else:
            if time<=0:
                print("Invalid! Time cannot be negative.")
            else:
                break
    
    return time


def depth(velocity,time):
    return (velocity*time)/2


main()