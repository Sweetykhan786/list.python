marks = [
[78, 76, 94, 86, 88],
[91, 71, 98, 65, 76],
[95, 45, 78, 52, 49]
]
i=0
sum=0
while i<len(marks):
    x=0
    while x<len(marks[i]):
        sum=sum+marks[i][x]
        x+=1
    i+=1
print(sum)
