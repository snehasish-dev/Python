n = int(input("How many row you are print:"))
for i in range(1,n):
    print(" "*(n-i),end="")
    print("*"*(2*(i-1)+1))

    