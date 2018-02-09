#filter메소드를 사용하여 정수리스트에서 소수만 걸러내기
def getPrime(x):
    for i in range(2,x-1):
        if x%i == 0:
            break
    else:
        return x

def getAllPrime(n):
    if n<3:
        return "Please input number over 3"
    ret = [2,3]
    if n <=3:
        return ret

    for i in range(4,n+1):
        for k in range(2,i-1):
            a = i % k
            if a==0:
                isPrime = False
                break
            else:
                ret.append(i)
        return ret

listdata = [117,119,1113,11113,11119]
ret = filter(getPrime, listdata)
print(list(ret))
print(getAllPrime(3))

# filter()의 리턴값은 결과가 담긴 filter 객체이다.
# list()를 이용해 filter객체를 리스트로 변환하여 출력한다.
