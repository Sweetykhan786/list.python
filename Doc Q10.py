"Largest & Smallest"
num=[21,34,56,100,56,78,90]
largest=num[0]
i=0
while i<len(num):
    if num[i]>largest:
        largest=num[i]
    i+=1
print(largest)
smallest=num[0]
i=0
while i<len(num):
    if num[i]<smallest:
        smallest=num[i]
    i+=1
print(smallest)

