size=int(input("Enter size of list:"))
a=[]
i = 0
while i<(size):
    num1=int(input("enter the number:"))
    a.append(num1)
    i+=1
print(a)
i=0
while i<len(a):
    j=0
    while j<len(a)-1:
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
        j=j+1
    i=i+1
print("The sorting list in ascending:",a)
