def sum(a, b):
    sum = a + b
    return sum

a = int(input("Enter the number:"))

ask = "Y"

while (ask == "Y") :
    b = int(input("Enter the number:"))
    c = sum(a,b)
    a = c
    ask = input("Do you want to add more numbers(Y/N) : ")

else:
    c = a
    print(c)

