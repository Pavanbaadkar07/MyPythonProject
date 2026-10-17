a=int(input("Enter a 1st num:"))
b=int(input("Enter a 2st num:"))
c=int(input("Enter a 3st num:"))
if a>b and a>c:
    print("The largest number is",a)
elif b>c:
    print("The largest number is",b)
else:
    print("The largest number is",c)