H, M=map(int,input().split(' '))#H,M 두 정수를 입력하는 방법


if M>=45:#조건에 맞으면 실행
    print(H,M+15)
elif H==0:#그렇지 않으면 다음조건을 본다
    print(23,15+M)
else:#그렇지 않으면 다음을 실행
    print(H-1, 15+M)

""" 
저는 컴파일러 에러가 드는데 다음 참고 코드는 에러가 안뜸 무슨차이인지 정확히 모르겠네요
h, m = map(int, input().split(" "))

if m >= 45 :
    print(h, m-45)
elif h == 0 :
    print(23, m+15)
else :
    print(h-1, m+15)
    [출처] 백준 알고리즘 2884번 알람 시계 - 파이썬|작성자 로아