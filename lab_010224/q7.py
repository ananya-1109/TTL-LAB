#7.write a python program to find out sum of all the items in a list. also sort the elements of the given list in descending order.

list=[3,2,5,8,10,45]
#print(sum(list))
sum=0
for i in list:
    sum=sum+i
print(sum)
print(list)
list.sort(reverse=True)
print(list)
