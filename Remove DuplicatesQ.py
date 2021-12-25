'Interview Question'
a=[1,2,2,3,3,4,5,6,7,7,9,0]
i=0
b=[]
while i<len(a):
    j=0
    c=1
    while j<len(a):
        if a[i]==a[j] and i!=j:
            c+=1
        j+=1
    if c>=2:
        pass
    else:
        b.append(a[i])
    i+=1
print(b)