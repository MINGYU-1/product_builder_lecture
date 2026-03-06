import sys
a = int(sys.stdin.readline())
data = []
for i in range(a):
    line = int(sys.stdin.readline())
    data.append(line)
data.sort()
for i in data:
    print(i)
