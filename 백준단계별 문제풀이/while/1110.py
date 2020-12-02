import sys
input = sys.stdin.readline

N = int(input())
num = N
cycle = 0

while True:
    cycle = cycle + 1
    a = num//10
    b = num%10
    num = b*10+((a+b)%10)
    if N == num:
        break
print(cycle)