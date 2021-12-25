marks = [
[78, 76, 94, 86, 88],
[91, 71, 98, 65],
[95, 45, 78],
[87, 67, 49, 68, 88]
]
i=0
sum=0
while i<len(marks):
    y=0
    while y<len(marks[i]):
        sum=sum+marks[i][y]
        y+=1
    i+=1
print(sum)