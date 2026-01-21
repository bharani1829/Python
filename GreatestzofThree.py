#WAP to find the greatest of 3 numbers entered by the user
a =int(input("Enter the First Number"))
b =int(input("Enter the Second Number"))
c =int(input("Enter the Third Number"))
if(a>=b and a>=c):
    print("First is Greatest")
elif(b>=c):
    print("Second is Greatest")
else:
    print("Third is Greatest")
