import sys
input = sys.stdin.readline
a,b = map(int,input().split())

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return int(a/b)
def nam(a,b):
    return a%b
print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
print(nam(a,b))