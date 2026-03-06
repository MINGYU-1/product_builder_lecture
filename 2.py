import sys
input = sys.stdin.readline()
from collections import Counter
N = Counter()
while True:
    try:
        M = input().rstrip()
        N.update(Counter(M))
    except:
        break
print(N)