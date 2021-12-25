"List items divisible by 5"
num=[5,6,7,10,15,35,56,65]
i=0
a=[]
while i<len(num):
    if num[i]%5==0:
        m=num[i]
        a.append(m)
    i+=1
print(a)
    

    