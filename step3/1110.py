n = int(input())

cnt = 0
new = n
while True:
    a = n // 10
    b = n % 10
    c = (a+b) % 10
    n = b*10+c
    cnt += 1
    if n == new:

        break
print(cnt)
