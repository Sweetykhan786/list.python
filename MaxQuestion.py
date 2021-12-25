numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
a=0
i=0
while i<len(numbers):
    if numbers[i]>a:
        a=numbers[i]
    i+=1
print(a)