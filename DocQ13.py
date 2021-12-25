"Iterate over both the values in a list and their indices"
"Output"
# => 0: flour
# => 1: cheese
# => 2: carrots

grocery_list = ['flour','cheese','carrots']
i=0
while i<len(grocery_list):
    print(i,":",grocery_list[i])
    i+=1

"Count unique values inside a list"
"Count = 5 #because [1,2,5,8,4] are unique values"

input_list = [1, 2, 2, 5, 8, 4, 4, 8]
b=[]
count=0
for i in input_list:
    if i not in b:
        b.append(i)
        count+=1
print("count of input_list:",count)        
print("Unique values:",b)        


"Remove empty List from List"
a=[5, 6, [], 3, [], [], 9]
while ([] in a):
    a.remove([])
print(a) 


"Find the sum of number digits in List"
a=[12,67,98,34]
i=0 
b=[]
while i<len(a):
    sum=0  
    while a[i]>0:
        sum+=(a[i]%10)
        a[i]=a[i]//10
    b.append(sum)   
    i+=1
print(b)

"18/12/21"
"Write a Python program to concatenate element-wise three given lists."
a=['0', '1', '2', '3', '4']
b=['red', 'green', 'black', 'blue', 'white']
c=['100', '200', '300', '400', '500']
i=0
while i<len(a):
    print(a[i]+b[i]+c[i])
    i+=1


"convert a given list of strings into list of lists"
a=['Red', 'Maroon', 'Yellow', 'Olive']
i=0
c=[]
while i<len(a):
    j=0
    b=[]
    while j<len(a[i]):
        b.append(a[i][j])
        j+=1
    c.append(b)    
    i+=1
print(c)


"Negative positive count"
"for loop"
a=[-12,14,95,3]
negative,positive=0,0
for num in a:
    if num>=0:
        positive+=1
    else:
        negative+=1
print("pos=",positive,"neg=",negative)           
"while loop"
a=[-12,14,95,3]
negative=0
positive=0
num=0
while num<len(a):
    if a[num]>0:
        positive+=1
    else:
        negative+=1
    num+=1    
print("pos=",positive,"neg=",negative) 


"Print numbers name"
a=["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
num=(input("enter number:"))
i=0
while i<len(num):
    s=int(num[i])
    print(a[s])
    i+=1


"Convert Character Matrix to single String;"
a=[["g","f","y"],["i","s"],["b","e","s","t"]]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j],end="")
        j+=1
    i+=1
print()

"List product excluding duplicates."
a = [6,1,3,5,6,3,1]
list=[]
i=0
while i<len(a):
    if a[i] in list:
        break
    else:
        list.append(a[i])
    i+=1
print(list)
i=0 
product=1
while i<len(list):
    product=product*list[i]
    i+=1
print(product)

"Space counting between the words"
a="Python is very easy"
count=0
i=0
while i<len(a):
    if a[i]==" ":
        count+=1
    i+=1
print(count)

"Count of words"
a='My name is Sweety'
b=[]
m=''
for i in a:
    if i=='':
        b.append(m)
    else:
        m+=i
b.append(m)
count=0
for i in b:
    count+=1
print(count)

"Reverse of words"
a="Python is very easy"
b=a.split()
i=0
while i<len(b):
    c=b[-i-1]
    i+=1
    print(c,end=" ")



"Show zero where negative integer is there"
a=[1,-5,7,5,-6,-9,2,4]
i=0
b=[]
while i<len(a):
    if a[i]<0:
        b.append(0)
    else:
        b.append(a[i])
    i+=1
print(b)


"Show zero at last "
a=[0,3,0,4,0,5,6]
i=0
b=[]
c=0
while i<len(a):
    if a[i]>0:
        b.append(a[i])
    elif a[i]<=0:
        c+=1
    i+=1
b.append(c)
j=0
while j<c:
    b.append(0)
    j+=1
print(b)

"Another method of printing zero at last"
a=[0,4,0,3,5]
i=0
b=[]
c=[]
while i<len(a):
    if a[i]>0:
        b.append(a[i])
    if a[i]==0:
        c.append(a[i])
    i+=1
b.extend(c)
print(b)


"Remove is"
a="My name is kirtee"
b=a.split()
b.remove("is")
print(b)