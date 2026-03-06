import sys
input = sys.stdin.readline
input() 
N,M = map(int,input().split())
prefix=[]
prefix = [[0]*N for _ in range(M)]
