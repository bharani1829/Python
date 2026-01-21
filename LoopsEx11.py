#WAP to find the sum of first n numbers. (using For And While) :

#1.Usinf For Loop
n = int(input("Enter a Number : "))

sum = 0

for i in range(1,n+1):
    sum = sum + i


print("The Sum Is (For Loop) : ",sum)

#2.Using While Loop



sum = 0
i = 1
while i<=n:
    sum = sum + i 
    i = i + 1

print("The Sum Is (While Loop) : ",sum)

    


