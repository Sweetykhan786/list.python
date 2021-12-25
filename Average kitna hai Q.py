elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=0
odd=0
while i<len(elements):
    if elements[i]%2==0:
        even+=elements[i]
        avg=even//4
    else:
        odd+=elements[i]
        avg1=odd//7
    i+=1
print("Average of even number:",avg)
print("Average of odd number:",avg1)
