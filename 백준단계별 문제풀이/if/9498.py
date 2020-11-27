a=int(input())#정수 a를 입력

if a > 89 and a <=100:
    print('A')
else: #조건문에 맞지 않을 때 실행 
    if a >=80 and a <90:#그렇지 않으면 다음조건을 본다
        print('B')
    else:
        if a >=70 and a <80:#그렇지 않으면 다음조건을 본다
            print('C')
        else:
            if  60<= a <70:#그렇지 않으면 다음조건을 본다
                print('D')
            else:
                print('F')
#elif = else if       
"""                 
b=int(input())
if b > 89 and b <=100:
    print('A')
elif b >=80 and b <90:
    print('B')
elif b >=70 and b <80:
    print('C')
elif b >=60 and b <70:
    print('D')
elif b <60:
    print('F')
"""