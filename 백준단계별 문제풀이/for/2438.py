N = int(input())
num =0#변수를 지정

for i in range(N):#0부터 N-1까지 반복 i는 반복한 횟수를 나타냄 i = 0, 1, 2, ... N
    num = num+1#1회 반복마다 1씩 증가 ex) num = 0, 1, 2, 3...
    print('*'*num)