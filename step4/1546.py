import sys


n = int(input())
a = list(map(int, sys.stdin.readline().split()))

sum_lst = []
maxx = max(a)
for i in range(n):
    sum_lst.append(a[i]/maxx*100)

print(sum(sum_lst)/n)
