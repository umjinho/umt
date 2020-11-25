a=int(input())
b=int(input())

#c=a*(b%10)
#print(c)
#d=a*((b//10)%10)
#print(d)
#e=a*(b//100)
#print(e)
#
#print(c+10*d+100*e)

result = 0 
b = str(b)
for i in range(3):
    index=2-i
    n=b[index]
    num=int(n)*a
    print(num)
    result +=(10**i)*num
    
print("{}*{} = {}".format(a,b,a*int(b)))
pirnt(result)