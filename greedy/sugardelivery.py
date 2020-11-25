a=int(input()) # a= 설탕의 무게
b = 0 # b = 3kg 봉지개수
while True:
    if a%5==0: #5kg 봉지로 나눠 떨어질때
        bag5=a//5 # a kg을 5봉지에 담았을때 봉지 수
        print(bag5+b)#5kg봉지개수와 3kg 봉지개수의 합
        break
    b = b+1#5kg봉지로 나눠 떨어지지 않을때 3키로 봉지수를 1개 추가 한다는 의미
    a = a-3#3kg 봉지수가 추가되면서 a는 3kg 씩 감소한다.
    if a<0:#5kg 봉지와 3kg봉지로 정확히 a kg이 나올 수 없을때 출력
        print(-1)
        break
        
    
