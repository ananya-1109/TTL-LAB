#10.write a python program to convert a tuple to a string then create a list where all the items of the list are takem from keyboard dynamically then convert that list to a tuple.
t=("Ana","nya"," Sharma")
l=[]
for i in t:
    l.append(i)
print(l)
s=" "
s1=s.join(l)
print(s1)
