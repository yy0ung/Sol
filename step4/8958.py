import sys


n = int(input())

lst = []

for i in range(n):
    line = sys.stdin.readline().rstrip()
    val = 0
    score = 0
    for j in range(len(line)):
        if val == 0 and line[j] == "O":
            score += 1
            val += 1
        elif val != 0 and line[j] == "O":
            score = score + val+1
            val += 1
        elif line[j] == "X":
            val = 0
    print(score)
