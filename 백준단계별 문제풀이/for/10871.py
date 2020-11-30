N, X = map(int,input().split())
A = list(map(int,input().split()))
for i in A:#리스트를 반복문에 실행 리스트 값들을 i에 하나씩 대입
    if i< X:#리스트 값 i가 X보다 작으면 실행
        print(i,end=' ')