#wap to generate a pyramid upto n terms using nested loop 
a = int(input("Enter limit"))
number = 1
for i in range(1, a+1):
    for j in range(1, i+1):
        print(number, end=" ")
        number+=1
    print("")
