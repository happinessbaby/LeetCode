#solution1: non-recursive
def tribonacci(N):
    trib={}
    trib[0] = 0
    trib[1] = 1
    trib[2] = 1
    n = 3
    while n <= N:
        trib[n] = trib[n-1] + trib[n-2] + trib[n-3]
        n += 1
    return trib[N]

#solution2: recursive
memo = {}
def trib(n, memo):
    if n in memo:
        return memo[n]
    if n==0:
        return 0
    if 0<n <= 2:
        return 1
    memo[n] = trib(n-1, memo)+trib(n-2, memo)+trib(n-3, memo)
    return memo[n]


#print(tribonacci(25))
print(trib(25, memo))
