N = int(input())
num = 1
for i in range(N):
    A, B = map(int,input().split())
    print('Case #{}: {} + {} = {}'.format(num, A, B, A+B))
    num = num+1