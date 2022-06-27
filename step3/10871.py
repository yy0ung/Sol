import sys


n, x = map(int, input().split())

a = list(map(int, sys.stdin.readline().split()))

lst = []

for i in range(n):
    if a[i] < x:
        lst.append(a[i])

print(*lst)
