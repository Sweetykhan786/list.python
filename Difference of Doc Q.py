"Interview Questions"
a=[2,5,4,6,7]
i=1
b=[]
x=0
while i<len(a):
    c=a[i]-a[x]
    b.append(c)
    i+=1
    x+=1
print(b)
