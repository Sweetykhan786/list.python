# places=["Delhi", "Gujrat", "Rajasthan", "Punjab", "Kerala"]
# places=[1,2,3,4,5,6,7,8,9]
# i=0
# while i<len(places):
#     back=places[-i -1]
#     i+=1
#     print(back,end=" ")



# a=[1,2,3,4,5,6]
# a=(a[::-1])
# print(a)

a=[[1,2,3],[4,5],[6.7]]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        b.append(a[i][j])
        j+=1
    i+=1
print(b)