"Removing even numbers"
list = [1,2,3,4,5,6,7,8,9,10,12,21,13,31,14,41,15,51,61,16,72]
i=0
a=[]
while i<len(list):
    if list[i]%2==0:
        pass
    else:
        list[i]
        a.append(list[i])
    i+=1
print("List after removing even numbers:",a)