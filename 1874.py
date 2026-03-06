stack = []
op = []
count = 1
temp = True
N = int(input())
for i in range(1,N+1):
    M = int(input())
    while count <= M:
        stack.append(count)
        op.append('+')
        count += 1
    if stack[-1] == M:
        op.append('-')
        stack.pop()
    else:
        temp =False
        break
if temp == False:
    print('NO')
else:
    for j in op:
        print(j)

