def sub(num1,num2):
    sub = a - b
    return sub

a = int(input("Enter the number:"))

ask = "Y"

while (ask == "Y") :
    b = int(input("Enter the number:"))
    c = sub(a,b)
    a = c
    ask = input("Do you want to subtract more numbers(Y/N) : ")

else:
    c = a
    print(c)
