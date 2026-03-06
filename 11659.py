import sys
input = sys.stdin.readline
sum = 0
N,M = map(int,input().split())
prefux_sum = [0]*(N+1)
list_1 = list(map(int,input().split()))
for i in range(N):
    sum += list_1[i]
    prefux_sum.insert(i+1, sum)
for _ in range(M):
    i,j = map(int,input().split())
    result = prefux_sum[j]- prefux_sum[i-1]
    print(result)