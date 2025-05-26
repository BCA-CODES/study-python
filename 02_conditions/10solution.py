pet_type = input("Enter your pet type(ex.cat, dog, etc.):").lower()
pet_age = float(input("Enter your pet age: "))

if pet_type == "dog":
    if pet_age <= 2:
        print("Recommanded: Puppy food")
    else:
        print("Recommanded: Adult dog food")
elif pet_type == "cat":
    if pet_age <= 5:
        print("Recommanded: Puppy food")
    else:
        print("Recommanded: Senior cat food")
else:
    print("Right now, entered pet details are not available.")
