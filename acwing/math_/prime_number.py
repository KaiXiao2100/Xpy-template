#朴素筛
def get_prime1(N):
    prime_vals = []
    flag = [False]*(N+1)
    for val in range(2,N+1):
        if(flag[val])continue
        prime_vals.append(val)
        for p_val in range(val+val,N+1,val)
            flag[p_val] = True
    return prime_vals,flag


#线性筛
def get_prime2(N):
    prime_vals = []
    flag = [True]*(N+1)
    for val in range(2,N+1):
        if flag[val]:
            prime_vals.append(val)
        for p_val in prime_vals:
            if val * p_val>N:
                break
            
            flag[val*p_val] = False

            if val%p_val == 0:
                break
    return prime_vals,flag

#分解质因数
#预处理出范围内所有质数，枚举处理是否能够整除质数


#快速幂
def GP(a1,q,k):
    res = a1 % Mod
    while k:
        if k & 1:
            res = (res * q) % Mod
        k >>= 1
        q = (q * q) % Mod

    return res

#约数个数


