import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split(' ')))
A.sort()
t = 0
w = 0
for i in A:
    w= w+i
    t= t+w
    
print(t)

