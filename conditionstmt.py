age=int(input("Enter your age :"))
if age<13:
    print("You are a child")
elif age>=13 and age<=18:
    print("you are a teenager")
elif age>=18 and age<60:
    print("You are an adult")
else:
    print("your are a senior ciizen")


fruit=input("Enter fruit :")
col=input("Enter color of the fruit :")
if col=="yellow":
    print(fruit,"is ripe")
elif col=="brown":
    print(fruit,"is over ripe")
else:
    print(fruit,"is unripe")