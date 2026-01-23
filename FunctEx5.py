#WAP to find even or odd

"""
Logic :

    n%2 = even
    else 
    odd
"""

def print_result(n):
    value = n%2
    if(value==0):
        print("Even")
    else:
        print("Odd")

print_result(7)