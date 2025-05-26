number = int(input("enter a factorial number:"))
factorial = 1

while number > 0:
    factorial *= number
    number -= 1
print("factorial of given number is:",factorial)
