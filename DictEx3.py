marks = {}

x = int(input("Enter phy marks : "))
marks.update({"Phy " : x})
y = int(input("Enter math marks : "))
marks.update({"math " : y})
z = int(input("Enter che marks : "))
marks.update({"che ": z})

print(marks)