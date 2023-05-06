def mul(num1,num2):
    mul = a * b
    return mul

a = int(input("Enter the number:"))

ask = "Y"

while (ask == "Y") :
    b = int(input("Enter the number:"))
    a = mul(a,b)
   
    ask = input("Do you want to multiply more numbers(Y/N) : ")

else:
    
    print("Answer is:", a, "*", b, "=", a)
