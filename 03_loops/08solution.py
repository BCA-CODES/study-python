number = int(input("enter a prime number checker:"))
    
prime = True

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
        
print(prime)
