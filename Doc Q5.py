"10 User Input Program"
i=0
b=[]
while i<10:
    num=int(input("Enter number:"))
    b.append(num)
    i+=1
print(b)
num=int(input("Enter number:"))
if num in b:
    print("Yes Present")
else:
    print("Not present")