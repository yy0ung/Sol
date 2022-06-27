h, m = map(int, input().split())

min = int(input(''))


sumMin = m+min
if sumMin >= 60:
    h += sumMin // 60
    m = sumMin % 60
else:
    m = sumMin
if h >= 24:
    print(h % 24, m)
else:
    print(h, m)
