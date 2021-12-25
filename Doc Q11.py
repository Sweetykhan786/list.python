"20 integer inputs from user"
i=0
b=[]
while i<20:
    num=int(input("enter numbers:"))
    b.append(num)
    i+=1
print(b)
i=0
positive=[]
negative=[]
even=[]
odd=[]
zero=[]
while i<len(b):
    
    if b[i]>0:
        a=b[i]
        positive.append(a)
    if b[i]<0:
        n=b[i]
        negative.append(n)
    if b[i]%2==0:
        e=b[i]
        even.append(e)
    if b[i]%2!=0:
        o=b[i]
        odd.append(o)
    if b[i]==0:
        z=b[i]
        zero.append(z)
    i+=1
print("Positive:",positive)
print("Negative:",negative)
print("Even:",even)
print("Odd:",odd)
print("Zero:",zero)





    
