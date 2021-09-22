#1

N = int(input())

n_list = map(int, input().split())

cnt = 0

for n in n_list:
    if n != 1:
        for i in range(2, n): #1과 자기자신을 제외한 수로 나뉘면 X
            if n % i == 0:
                break
        else:
            cnt += 1


print(cnt)


#2

min_num = int(input())
max_num = int(input())
decimal_list = []

for i in range(min_num, max_num + 1):  # 첫 입력값과 두번째 입력값 사이만 진행
    count = 0
    for j in range(1, i + 1):  # 1부터 i항까지 진행
        if i % j == 0:
            count += 1  # 나뉘면 count증가
            if count > 2:  # 2보다 크면 소수가 아니므로(소수는 1과 자기자신으로만 나뉨) 바로 다음식 진행
                break
    if count == 2:  # 소수
        decimal_list.append(i)
if len(decimal_list) != 0:  # 소수리스트에 값이 있다면 밑의 값을 출력
    print(sum(decimal_list))
    print(decimal_list[0])
else:  # 소수가 하나도 없다면
    print('-1')


#3

m, n = map(int, input().split())

def prime_list(m, n):
    n += 1
    sieve = [True] * n

    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(2*i, n, i):
                sieve[j] = False

    # return [i for i in range(2, n) if sieve[i] == True]
    for k in range(m, n):
        if k > 1 and sieve[k] == True:
            print(k)


prime_list(m, n)


# 4 솔루션

n = int(input())

def sosu(n):
    if n ==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True							#소수 구하는 방식은 위와 같다

all_list = list(range(2,246912))		#문제에서 제한한 범위
memo = []								#for문 밖에 리스트 정의

for i in all_list:						#2부터 2*123,456 범위
    if sosu(i):							#sosu함수에 해당하면
        memo.append(i)					#리스트에 추가


while True:
    count=0					#갯수를 세야하는 조건 때문에 카운트
    if n == 0 :
            break
    for i in memo:			#memo리스트 중에서
        if n < i <=2*n:		#입력한 값의 범위 내에서 값이 있으면
            count+=1		#있을 때 마다 카운트 +1
    print(count)
    n = int(input())		#0 입력받기 전까지 계속 해야하므로 입력 받음