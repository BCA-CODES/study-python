score = 176
letter = "You have scored a"

if score >= 101:
    print("Please check your score.")
    exit()

if score >= 90:
    print(letter,"A")
elif score >= 80:
    print(letter,"B")
elif score >= 70:
    print(letter,"C")
elif score >= 60:
    print(letter,"D")
else: 
    print(letter,"F")
