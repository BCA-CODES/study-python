fruit = input("Enter a Fruit:").lower()
color = input("Enter a Color of fruit:").lower()

if fruit == "banana":
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("Overripe")
else :
    print("I have not available other fruit information right now!")
