
import math

print("================================")
print(" PETROLEUM ENGINEERING CALCULATOR")
print("================================")

print("\n1. Hydrostatic Pressure")
print("2. Fluid Density")
print("3. Pipe Cross-sectional Area")

choice = input("\nChoose a calculation: ")

if choice == "1":
    density = float(input("Enter fluid density (kg/m3): "))
    height = float(input("Enter fluid height (m): "))

    g = 9.81
    pressure = density * g * height

    print(f"\nHydrostatic Pressure = {pressure:.2f} Pa")
    print(f"Pressure = {pressure / 1_000_000:.4f} MPa")

elif choice == "2":
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m3): "))

    if volume <= 0:
        print("Volume must be greater than zero.")
    else:
        density = mass / volume
        print(f"\nFluid Density = {density:.2f} kg/m3")

elif choice == "3":
    diameter = float(input("Enter pipe diameter (m): "))

    if diameter <= 0:
        print("Diameter must be greater than zero.")
    else:
        area = math.pi * diameter**2 / 4
        print(f"\nPipe Area = {area:.4f} m2")

else:
    print("Invalid selection. Try again.")
