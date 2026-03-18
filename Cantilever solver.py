
# Enter load 1 location
A1 = float(input("Distance from load 1 to WALL (m): "))
# Enter load mass
W1 = float(input("What is the mass of load 1? "))
# Enter load 2 location
A2 = float(input("Distance from load 2 to WALL (m): "))
# Enter load 2 mass
W2 = float(input("What is the mass of load 2 ? "))

Ry = W1 + W2
Rx = 0
M = (W1 * A1) + (W2 * A2)

print(f"Rx = {Rx} N")
print(f"Ry = {Ry} N")
print(f"M  = {M} N·m")
print(f"Check ΣFy = Ry - W = {Ry - (W1 + W2)}")  # should be 0