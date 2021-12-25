n = [19, 17, "python", 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
list=[]
while i<len(n):
    if n[i] in list:
        pass
    else:
        list.append(n[i])
    i+=1
print(list)



  