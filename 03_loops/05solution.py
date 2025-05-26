name = input("enter a name:")

for char in name:
    print(char)
    if name.count(char) == 1:
        print("count is:",char)
        