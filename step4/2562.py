import sys


lst = []
for i in range(9):
    lst.append(int(sys.stdin.readline()))

print(max(lst), lst.index(max(lst))+1, sep="\n")
