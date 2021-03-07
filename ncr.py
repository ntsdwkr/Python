# ncr using function
def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    return ans


def ncr(n, r):
    return fact(n)//(fact(r)*fact(n-r))


n = int(input())
r = int(input())
ans = ncr(n, r)
print(ans)
