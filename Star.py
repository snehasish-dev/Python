n = int(input("How many row you are print:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*(i-1)+1))
print("\n")
name = "snehasish"
for i in range(len(name)):
    print(name[i])
    