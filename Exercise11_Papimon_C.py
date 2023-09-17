number = int(input("enter number : "))
for x in range(number):
    print(" "*(number-(x-1)), "*"*(x+(x+1)))