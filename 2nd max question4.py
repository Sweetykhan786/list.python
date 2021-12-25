numbers=[50,40,23,70,56,12,5,10,7]
a=0
i=0
while i<len(numbers):
    if numbers[i]>a:
        a=numbers[i]
    i+=1
i=0
a1=0
while i<len(numbers):
    if numbers[i]>a1:
        if numbers[i]!=a:
         a1=numbers[i]                                                       
    i+=1
print(a)

