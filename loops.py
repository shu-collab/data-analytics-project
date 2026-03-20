#for loop
'''number=[1,-3,2,-4,5,9,10,-32,-45]
positive_num_count=0
for i in number:
    if i>0:
        positive_num_count+=1
print("final count of +ve no. is:",positive_num_count)
'''
#while loop
'''i=int(input("Enter value of i :"))
while(i<=38):
    i=int(input("enter value of i :"))
    print(i)
if(i>=38):
    print("Enter the smaller value of i")
else:
    print("Done with the loop")
'''
'''i=int(input("Enter value of i :"))
while(i<38):
    i=int(input("enter value of i :"))
    print(i)
if(i>38):
    print("Enter the smaller value of i")
else:
    print("Done with the loop")

n=int(input("Enter number:"))
j=int(input("till what number:"))
for i in range(1,j+1):
    if i==5:
        continue
    print(n,"x",i,"=",n*i)
for i in range(1,j+1):
    if i==5:
        break
    print(n,"x",i,"=",n*i)
'''
i=int(input("Enter value of i :"))
if(i<38):
    i=int(input("enter value of i :"))
    print(i)
if(i>38):
    print("Enter the smaller value of i")
else:
    print("Done with the loop")