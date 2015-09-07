data = ['a','b','c',['abcd','efg']]

print(data[1])
print(data[-1][-1])
# 데이터가 들어갈때 데이터 타입이 결정됨.
# 리스트 초기화가 필요할 땐 data = []로 해놓고 값을 변경시키거나 할 수 있음.

b = [1,2,3] 
c = ['Life', 'is', 'too', 'short']
d = b*3
e = b+c
print('b*3')
print(d)
print('b+c')
print(e)

G = ['a','b','c','d']

print(G)
G[0]='greenjoa'

print(G)

G[1]=['greenjoa1','greenjoa2'] # 리스트가 들어감
print(G)
G[1:2] = ['greenjoa1','greenjoa2'] #1,2번으로 추가 삽입
print(G)

G.insert(2, 'e')   #2번 인덱스에 'e' 삽입 
G.append('greenjoa2')    # 마지막에 추가됨
print(G[-1])
G.remove('c') 
G[1:2]=[] 
del G[0]
print(G)

#print(G.index('c'))  # 해당하는 데이터의 인덱스 반환. 데이터가 없으면 에러 발생

#ID값이 세개인 리스트
id = ['Life', 'Maru', 'Byul']

#리스트에 패스워드 넣기
id.insert(1,'123')
id.insert(3,'456')
id.insert(5,'789')
print(id)

#리스트에 리스트형 이름 전화번호 넣기

id.insert(2,['라이프','010-1234-5678']) # 리스트가 들어감
id.insert(5,['마루','010-7894-2648'])
id.insert(8,['별','010-6254-1672'])
print(id)

#리스트 멤버 Access _ 반복문을 사용하여 액세스 하기

print('******for setps in range(9):******')
for setps in range(9) :  #맨 끝에는 :
#괄호가 없고 들여쓰기
    print(id[setps])
    
print('******for steps in range(nEntries) :******')
nEntries = len(id)
for steps in range(nEntries) :
    print(id[steps])

print('******for ids in id :******')
for ids in id :
    print(ids)

#data2 = range(4)
#print(data2)

scores= [1,43,24,35,19,23,10]
print('******scores******')
print(scores)
scores.reverse()
print('******scores.reverse()******')
print(scores)

scores.sort()
print('******scores.sort()******')
print(scores)

top = scores[0:5]
print('******print(top)******')
print(top)

#isinstance 어떤 타입인지 알려주는 함수
#리스트인 것은 또 다시 반복하여 출력
print('리스트 출력 _ 리스트안의 리스트를 반복문을 이용하여 출력하기')
for steps in id :
    if isinstance(steps,list) : 
        for step in steps : 
            print(step)
    else : 
        print(steps)

#pop(), pop(n)
mynum = id.pop() #마지막 요소를 돌려주고 그 요소 삭제
print(mynum)
mynum2 = id.pop(2) #2번째 요소 돌려주고 요소 삭제
print(mynum2)
print(id)

id.append('Byul')
print(id)

#List와 비슷하지만 Tuple은 갱신이 불가능! 변경시킬 수 없다.
#Tuple은 변경연산시 오류가 남.
t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 =1,2,3
t5 = ('a','b',('c','d'))

print(t4)
