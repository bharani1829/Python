# Write a recursive function to print all the elements in a list (Use list and index as parameter )

def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
    
fruits =["apple","banana","Mango"]

print_list(fruits)
