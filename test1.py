# Ask the user for their name
name=input("What's is your name? ")
print(f"Hello, {name}!")

# Asks for a seismic wave velocity (float) in m/s 
def data1():
    Velocity=float(input("What's the value of seismic wave velocity in m/s? "))
    Time=float(input("What's the value of travel time in second? "))
    return Velocity,Time

# Calculates the depth
def depth(Velocity,Time):
    return ((Velocity*Time)/2)

# Result
def result(Velocity,Time):
    print("Estimated Depth is", round(depth(Velocity,Time),2),"m")

# Run everything
Velocity,Time=data1()
result(Velocity, Time)

