a=int(input())


if a%4==0 and a%100!=0 or a%400==0:# and는 둘다 맞을때 실행 / or은 둘 중하나가 맞을때 실행
    print(1)
else:#조건에 적합하지 않을시 출력
    print(0)