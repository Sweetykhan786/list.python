a=[[1,2],[3,4],[4,5]]
i=0
sum=0
while i<len(a):
    j=0
    while j<=i-i:
        sum=sum+a[i][j]
        j+=1
    i+=1
print(sum)
