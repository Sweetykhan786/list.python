
marks = [
[78, 76, 94, 86, 88],
[91, 71, 98, 65],
[95, 45, 78]
]
i=0
sum=0
while i<len(marks):
    add=0
    while add<len(marks[i]):
        sum=sum+marks[i][add]
        add+=1
    i+=1
print(sum)