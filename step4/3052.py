import sys

cnt = 0
dic = {}
for i in range(10):
    k = int(sys.stdin.readline()) % 42
    dic[k] = dic.get(k, 0) + 1
    if dic.get(k, 0) == 1:
        cnt += 1


print(cnt)
