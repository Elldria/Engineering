L = float(input("Enter beam length (m): "))
# Enter load 1 location
A1 = float(input("Distance from A (pin) to load (m): "))
# Enter load mass
W1 = float(input("What is the mass of load (N): "))
# Enter load 2 location
A2 = float(input("Distance from A (pin) to load 2 (m): "))
# Enter load 2 mass
W2 = float(input("What is the mass of load 2 ? "))

RAx = 0
RBy = (W1 * A1 + W2 * A2) / L
RAy = (W1 + W2) - RBy

print(f"RBy = {RBy} N")
print(f"RAy = {RAy} N")
print(f"RAx = {RAx} N")


# After:
print(f"Check ΣFy = {(RAy + RBy) - (W1 + W2)}")