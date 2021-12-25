"Interview Question"
# a=[110,1000,19000,12000,1230000]
# i=0
# b=[]
# while i<len(a):
#     while a[i]>0:
#         if a[i]%10!=0:
#             b.append(a[i])
#             break
#         a[i]//=10
#     i+=1
# print(b)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)