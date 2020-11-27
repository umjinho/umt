x=int(input()) #정수 x를 입력
y=int(input()) #정수 y를 입력


if x>0 and y>0:#조건에 맞으면 실행
    print(1)
elif x<0 and y>0:#그렇지 않으면 다음조건을 본다
    print(2)
elif x<0 and y<0:#그렇지 않으면 다음조건을 본다
    print(3)
elif x>0 and y<0:#그렇지 않으면 실행
    print(4)