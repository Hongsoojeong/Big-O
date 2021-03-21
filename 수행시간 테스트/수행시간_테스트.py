import random, time

def unique_n2(A): # A의 각 값을 다른 값들과 일일이 비교하는 방법 : 이중 for 루프 이용
	for i in range(0,len(A)): #0부터 len(A)-1까지 for문을 돌도록 한다.
		for j in range(i+1,len(A)): #위의 for문의 i의 값에 +1한 값부터 len(A)-1까지 for문을 돌도록 한다.
			#i+1을 한 이유는, A[i]와 같은 값을 가지면서 인덱스 값이 다른 지를 찾는 것이기 때문에
			#i에 +1한 상태로 시작하면, 비교할 때 인덱스가 겹칠 일이 없다. 
			if A[i]==A[j]: # 값이 서로 같을 경우 
				return print("NO") # 같은 값이 한 쌍 이상 존재하므로 NO를 출력하도록 한다.
	return print("YES") 
#for문에 if문이 걸리지않고 다 돌게된다면, 리스트 A에는 같은 값이 한 쌍 이상 존재하지 않으므로 YES를 출력하도록 한다. 


def unique_nlogn(A): #A.sort()함수를 호출해 오름차순으로 정렬-> 차례로 값을 비교
	A.sort() #리스트 A를 오름차순으로 정렬해준다.
	k=0
	for i in range(1,len(A)): # 1부터 len(A)-1까지 for문을 돌도록 한다.
		if A[k]==A[i]: #A[k]과 A[i]의 값이 같을 경우
			return print("NO") #이는 같은 값이 한 쌍 이상 존재하는 것이므로 NO를 출력하도록 한다.
		else:
			k+=1 #k의 값에 1을 더한다.
	return print("YES")
#for문에 if문이 걸리지않고 다 돌게된다면, 리스트 A에는 같은 값이 한 쌍 이상 존재하지 않으므로 YES를 출력하도록 한다.


def unique_n(A): #A의 값들이 -n부터 n 사이의 값들이라는 정보를 이용해 새로운 리스트 B를 정의해 이용하는 방법
	B=[] #빈 리스트 B를 선언
	k=0
	for i in range(0,len(A)+1): 
		#A의 값들이 -n부터 n 사이의 값들이므로 for문의 범위를 0부터 len(A)까지 잡는다.
		if (A[k]==i and A[k] not in B):
		#만약 i의 값이 리스트 A의 k번째에 존재하고 A[k]의 값이 리스트 B에 존재하지 않는다면
			B.append(A[k]) # A[k]의 값을 리스트 B에 append한다.
			k+=1 #k의 값에 1을 더해준다.
		elif (A[k]==-i and A[k] not in B): 
			#혹은 -i의 값이 리스트 A의 k번째에 존재하고 A[k]의 값이 리스트 B에 존재하지 않는다면
			B.append(A[k])# A[k]의 값을 리스트 B에 append한다.
			k+=1#k의 값에 1을 더해준다.
		elif (A[k] in B): #i의 값이 리스트 A의 k번째에 있는지 고려하기 전에, A[k]의 값이 이미 리스트 B에 존재하는 것이라면 
			return print("NO") #리스트 A에 이미 같은 값이 한 쌍 이상 존재하는 것이므로 NO를 출력해준다.
	return print("YES") 
#for문에 if문이 걸리지않고 다 돌게된다면, 리스트 A에는 같은 값이 한 쌍 이상 존재하지 않으므로 YES를 출력하도록 한다.

# input: 값의 개수 n
n = int(input())
# -n과 n 사이의 서로 다른 값 n 개를 랜덤 선택해 A 구성
A = random.sample(range(-n, n+1), n)

# 위의 세 개의 함수를 차례대로 불러 결과 값 출력해본다
# 당연히 모두 다르게 sample했으므로 YES가 세 번 연속 출력되어야 한다

# 동시에 각 함수의 실행 시간을 측정해본다



before=time.process_time()
unique_n2(A)
after=time.process_time()
uniqueN2=after-before


before=time.process_time()
unique_nlogn(A)
after=time.process_time()
uniquelogn=after-before


before=time.process_time()
unique_n(A)
after=time.process_time()
uniqueN=after-before


print(f"unique_n2 의 수행시간: {uniqueN2}\nunique_nlogn 의 수행시간: {uniquelogn}\nunique_n 의 수행시간: {uniqueN}")

# 이러한 과정을 n을 100부터 10만까지 다양하게 변화시키면서 측정한다
