#WAF to Search if the word “learning” exists in the file or not.

def find():
    with open("sample.txt","r") as f:
        data = f.read()
        word = "learning"
        if(word in data):
            print("Found")
        else:
            print("Not Found")

find()
