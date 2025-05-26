distance = float(input("Please enter a distance of transportation in km:"))

if distance <= 3:
    print("Walk")
elif distance <= 15:
    print("Bike")
else:
    print("Car")
