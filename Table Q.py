n=int(input("Enter any number:"))
i=1
b=[]
while i<=n:
    count=1
    while count<=10:
        c=i*count
        b.append(c)
        count+=1
    i+=1
print(b)