number = int(input("enter a number to multiplication table:"))

for i in range(1, 11):
    if i==5:
        continue
    print(number, "x", i, "=", number*i)
