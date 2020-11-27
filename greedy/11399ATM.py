import sys
input = sys.stdin.readline
N = int(input())#N명의 사람들을 입력
A = list(map(int,input().split(' ')))#N명의 사람들이 돈뽑는데 걸리는 시간
A.sort()#N명의 사람들을 시간이 낮은순으로 배열
t = 0 #걸리는 시간
w = 0 #기다리는 시간
for i in A: #A[리스트]에 있는 값을 하나씩 갖고와서 i라는 값으로 실행
    w= w+i #A[리스트] 값 i를 차례로 갖고와 더한다 = 각 사람이 기다리는 시간
    t= t+w #한사람 지날때마나 총 걸린시간
    
print(t)#총걸린시간 출력
