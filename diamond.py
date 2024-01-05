n = int(input("Enter N:"))

for i in range(0,n):
    for j in range(0,n):
        if(i+j<n-1):
            print(" ",end="")
        else:
            print("*",end="")
    for j in range(0,n):
        if(i==0):
            print(" ",end="")
        elif(j<i):
            print("*",end="")
        else:
            print(" ",end="")
            
    print(end="\n")
for i in range(n-2,-1,-1):
    for j in range(0,n):
        if(i+j<n-1):
            print(" ",end="")
        else:
            print("*",end="")
    for j in range(0,n):
        if(i==0):
            print(" ",end="")
        elif(j<i):
            print("*",end="")
        else:
            print(" ",end="")
    print(end="\n")