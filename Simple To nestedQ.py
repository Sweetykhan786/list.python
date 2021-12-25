a=[1,2,3,4,5,6,7,8,9]
i=0
final=[]
b=[]
count=0
while i<len(a):
    if count==2:
        final.append(b)
        b=[]
        count=1
    else:
        count+=1
        b.append(a[i])
        i+=1
final.append(b)
print(final)
    