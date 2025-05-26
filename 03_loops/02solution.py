numbers = int(input("enter a numbers:"))
even_numbers = 0

for num in range(1, numbers + 1):
    if num % 2 == 0 :
        even_numbers = num + even_numbers 
print("sum of even numbers are: ",even_numbers)