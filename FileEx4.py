# WAF to find in which line of the file does the word “learning”occur first. Print -1 if word not found. 

def check_for_word():
    with open("sample.txt","r") as f:
        data = f.read()
        word = "learning"
        if(word in data):
            print("Found")
        else:
            print("Not Found")

def check_for_line():
    with open("sample.txt","r") as f:
        word = "learning"
        data = True
        line_no = 1
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

# print(check_for_line())
check_for_line()