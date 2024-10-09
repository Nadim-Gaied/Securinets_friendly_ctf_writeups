# Importing required libraries in SageMath
from sage.all import EllipticCurve, GF

# Define the finite field GF(p), where p is a small prime number
p = 23  # you can change this to any prime number
F = GF(p)

# Define the parameters of the elliptic curve: y^2 = x^3 + ax + b over GF(p)
a = 1  # coefficient of x
b = 1  # constant term
E = EllipticCurve(F, [a, b])

# View the elliptic curve
E

# Get the points on the elliptic curve
points = E.points()

# Print the points
print("Points on the elliptic curve:")
for point in points:
    print(point)

# Order of the elliptic curve (number of points)
order = E.order()
print(f"Order of the elliptic curve: {order}")
