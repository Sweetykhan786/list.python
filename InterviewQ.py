n=int(input("enter the numbers:"))
i=0
a=[]
while i<n:
    num=int(input("enter no:"))
    a.append(num)
    j=0
    sum=0
    while j<len(a):
        sum=sum+a[j]
        j+=1
    i+=1
print(sum)