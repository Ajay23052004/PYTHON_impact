def primeRange(x,y,i=2):
    if x%i==0:
        print(i)
        x=x/i
        i=2
    if x==1:
        return
    if x%i!=0:
        i+=1
        primeRange(x+1,y,i)
    else:
        print(i)
        x=x/i
        i=2
        primeRange(x+1,y,i)
        
    
    
start = int (input("Start:"))
end = int (input("End:"))
print(primeRange(start,end))