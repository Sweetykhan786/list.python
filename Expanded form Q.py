num=input("Enter max size:")
i=0
add=""
while i<len(num):
    add+=num[i]
    j=1
    while j<=(len(num)-(i+1)):
        add+="0"
        j+=1
    if i==(len(num)-1):
        break
    else:
        add+="+"
    i+=1
print("Expanded list:",add)

