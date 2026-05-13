def main():
    # Ask the user for their name
    name=input("What's your name? ")
    print(f"Hello, {name}")
    #Asks for a seismic wave velocity (float) in m/s & travel time in second
    velocity=float(int(input("What's the value of seismic wave velocity in m/s? ")))
    time=float(int(input("What's the value of travel time in second? ")))
    #Calculates the depth
    print("The estimated depth is,", round(depth(velocity,time),2),"meter")

def depth(velocity,time):
    return ((velocity*time)/2)

main()