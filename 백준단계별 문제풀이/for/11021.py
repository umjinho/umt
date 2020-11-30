"""
N = int(input())
num = 1
for i in range(N):
    A, B = map(int,input().split())
    print('case #{}: {}'.format(num, A+B))
    num = num+1
# 런타임에러    
"""
T = int(input())
num = 1

for _ in range(T):
    A, B = map(int, input().split())
    print("Case #%s: %s" % (num, A+B))#{}을 %s로 적어도 같음
    num += 1#num = num+1와 같은 표현
    
#블로그에서 따온 무슨차이로 에러낫는지 이류를 모르겟음