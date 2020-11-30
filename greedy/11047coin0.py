#동전 종류 개수와 돈
N, K = map(int,input().split(' '))
#동전 
coins = sorted([int(input()) for _ in range(N)])
reminder = K
count = 0
for i in coins[::-1]:#[A:B:C] A부터 B까지 C(-1이면 역순)간격으로 배열
    count = count + reminder//i
    reminder = reminder%i
    
print(count)