# WAP to find factorial of first n numbers Using (For And While )Loops :

#Using For Loop

n = int(input("Enter the Number : ")) #This Input We Used for both For And While Loops

fact = 1

for i in range(1,n+1):
    fact = fact * i

print("The Factorial Is (By Using For)-->",fact)

#USing While Loop

fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1

print("The Factorial is(By Using While)-->",fact)



