def even(number):
    for i in range(2, number+1, 2):
        yield i
    
for num in even(8):
    print(num)
    