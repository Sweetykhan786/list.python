a=[[1,40,45],[50,21],[22,90]]
i=0
count=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][j]>count:
            count=a[i][j]
        j+=1
    i+=1
print(count)




