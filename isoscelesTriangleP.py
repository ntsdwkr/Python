# isosceles triangle number pattern
n=int(input())  
for i in range(1,n+1,1):
    c=1
    d=i-1
    for j in range(1,n+1-i,1):
        print(" ",end="")
    for j in range(n+1-i,n+1,1):
        print(c,end="")
        c+=1
    for j in range(n+1,n+i,1):
        print(d,end="")
        d-=1
    print("\n")
        
    
