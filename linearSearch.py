# Linear Search
def linearSearch(a,num):
    for i in range(len(a)):
        if num==a[i]:
            return i
    return -1

a=[int(x) for x in input("enter elements:").split()]
print(linearSearch(a,int(input("enter number:")))) 
