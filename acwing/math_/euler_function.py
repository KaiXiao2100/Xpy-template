#数论中，对正整数n，欧拉函数是小于或等于n的正整数中与n互质的数的数目
def euler_function(n: int):
    phi = [0]*n
    st = [False]*n
    primes = [0]*n
    cnt = 0
    phi[1] = 1
    for i in range(2,n+1):
        if not st[i]:
            primes[cnt] = i
            phi[i] = i-1
            cnt += 1
        for j in primes:
            if j*i>n:
                break
            st[j*i] = True
            if i%j==0:
                phi[i*j] = phi[i]*j
                break
            
            phi[i*j] = phi[i]*(j-1)
    
#同余方程
def exgcd(a, b):
    if not b:
        return 1, 0
    x, y = exgcd(b, a % b)
    return y, x - a // b * y

a, b = map(int, input().split())

x, y = exgcd(a, b)
print(x % b)