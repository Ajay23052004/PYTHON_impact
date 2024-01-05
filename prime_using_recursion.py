def prime(num,i=2):
    if(num<=2):
        return True
    elif(num % i==0 ):
        return False
    elif(i*i >num):
        return True
    else:
        return prime(num,i+1)
    
    
num = int (input("Enter NUmber:"))    
print(prime(num))