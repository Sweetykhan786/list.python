numbers=[50,40,23,70,56,12,5,10,7]
a=len(numbers)
i=0
count=0
while i<a:
    c=numbers[i]
    if c>20 and c<40:
        count=count+1
    i+=1
print(count)
