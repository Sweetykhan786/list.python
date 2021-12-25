magic_square = [
[8, 3, 4],
[1, 5, 9],
[6, 7, 2]
]
i=0
while i<len(magic_square):
    j=0
    sum=0
    while j<len(magic_square[i]):
        sum=sum+magic_square[i][j]
        j+=1
    i+=1
print("Sum of Rows:",sum)
b=0
while b<len(magic_square):
    d=0
    sum1=0
    while d<len(magic_square[b]):
        sum1=sum1+magic_square[b][d]
        d+=1
    b+=1
print("Sum of Columns:",sum1)
r=0
n=r
sum2=0
while r<len(magic_square):
    sum2=sum2+magic_square[n][r]
    r+=1
print("Sum of Diagonals:",sum2)
print("Yes it is a magic square")
