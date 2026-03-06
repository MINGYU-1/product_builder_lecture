import sys
input = sys.stdin.readline
list_bear = []
for _ in range(3):
    num = int(input().rstrip())
    list_bear.append(num)
list_bear.sort()
print(list_bear[1])

