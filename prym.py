n=int(input())
#for i in range(1,n):
#   for j in range(1,i):
#       print("*",end=" ")
#    print("\n")
for i in range(n):
    print(' ' * (n - i - 1), end='')
    print('* ' * (i + 1))
