# WAF that replace all occurrences of “java” with “python” in above file.
# To Replace the data we first need to read and then replace 

def replace_word():
    with open("sample.txt","r") as f :
        data = f.read()

    new_data=data.replace("java","python")
    print(new_data)


    with open("sample.txt","w") as f :
        f.write(new_data)

replace_word()
