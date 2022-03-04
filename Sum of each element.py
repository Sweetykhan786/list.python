"Sum of each element"
# a=[1,2,3,4]
# b=[2,3,4,1]
# i=0
# c=[]
# while i<len(a):
#     c.append(a[i]+b[i])
#     i+=1
# print(c)

"Multiplication of the following list"
# a=[1,2,3]
# b=[3,2,1]
# i=0
# sum=1
# while i<len(a):
#     sum=sum*a[i]*b[i]
#     i+=1
# print(sum)


"Minimum question"
# a=[2,3,1,4,5]
# b=a[0]
# i=0
# while i<len(a):
#     if a[i]<b:
#         b=a[i]
#     i+=1
# print(b)

"Sum of sub nested list"
# a=[1,2,[4,5,6],[1,2]]
# b=[]
# i=0
# sum=0
# while i<len(a):
#     if (type(a[i])==list):
#         j=0
#         while j<len(a[i]):
#             b.append(a[i][j])
#             sum=sum+a[i][j]
#             j+=1
#     else:
#         b.append(a[i])
#         sum=sum+a[i]
#     i+=1
# print(sum)