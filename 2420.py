import sys
input = sys.stdin.readline
def add(a,b):
    print(a+b)
a,b = map(int,input().split())
try:
    while a != 0 and b != 0:
        add(a,b)
        try:
            a,b = map(int,input().split())
        except:
            break
except:
    pass