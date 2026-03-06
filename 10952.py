import sys
input = sys.readline
def add(a,b):
    print(a+b)
while a==0 & b== 0:
    a,b = map(int,input().split())
    add(a,b)