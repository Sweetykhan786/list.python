elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=0
odd=0
while i<len(elements):
    if elements[i]%2==0:
        even+=1
    else:
        odd+=1
    i+=1
print("Even number in list:",even)
print("Odd number in list:",odd)
print("count of all numbers:",odd+even)
i=0
even=0
odd=0
while i<len(elements):
    if elements[i]%2==0:
        even+=elements[i]
    else:
        odd+=elements[i]
    i+=1
print("Sum of even numbers:",even)
print("Sum of odd numbers:",odd)
print("Sum of all:",even+odd)
i=0
even=0
odd=0
sum=0
while i<len(elements):
    if elements[i]%2==0:
        even+=elements[i]
        avg=even//4
    if elements[i]%2!=0:
        odd+=elements[i]
        avg1=odd//7
    if i<len(elements):
        sum=sum+elements[i]
        avg2=sum//11
    i+=1
print("Average of even number:",avg)
print("Average of odd number:",avg1)
print("Average of all:",avg2)
