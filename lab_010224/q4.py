#4.write a python program to count total number of characters of given string without space.

str="how are you doing?"
count=0
len(str)
for i in range(0,len(str)):
    if str[i]!=" ":
        count=count+1
print(count)
