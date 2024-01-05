def fact(x):
    if x==1:
        return 1
    else:
        return(x*fact(x-1))

num =30
print("Factorial of ",num,"is",fact(num))