"Square/Cube/Sum"
num=[1,2,3,4,5,5,6,7,8,9,10,11,12,13,14,15]
i=0
b=[]
x=[]
sum=0
while i<len(num):
   m=num[i]**2
   b.append(m)
   m1=num[i]**3
   x.append(m1)
   sum=sum+num[i]
   i+=1
print("Square of list:",b) 
print("Cube of list:",x)
print("Sum of list:",sum)



"Aage se square and then piche se sqaure"
num=[1,2,3,4,5,5,6,7,8,9,10,11,12,13,14,15]
i=0
c=[]
b=[]
while i<=5:
    m=num[i]**2
    b.append(m)
    i+=1
i=-1
while i>=-5:
    m=num[i]**2
    c.append(m)
    i-=1
print(b)
print(c)
print(b+c)

    
"answer should be 66"
a=[1,2,3,4,5,6]
b=[7,8,9,10,11]
i=0
sum=0
while i<len(a):
    sum=sum+a[i]
    i+=1
i=0
sum1=0
while i<len(b):
    sum1=sum1+b[i]
    i+=1
print("sum:",sum+sum1)

"Opposite of above"
# a=[1,2,3,4,5]
# b=[7,8,9,2,1]
# d=[1,2,3,5,3]
# i=0
# c=[]
# while i<len(a):
#     s=(a[i]+b[i]+d[i])
#     c.append(s)
#     i+=1
# print(c)


a=["sweety","mango","swati"]
b=["monika","prachi","shivani"]
i=0
c=[]
while i<len(a):
    s=(a[i]+b[i])
    c.append(s)
    i+=1
print(c)


