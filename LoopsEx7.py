#Search for a number x in this tuple using While loop:

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
idx = 0
x = 36
while idx < len(tup):
    if(tup[idx]==x):
        print("The x is found in Idx : ",idx)
    idx = idx + 1