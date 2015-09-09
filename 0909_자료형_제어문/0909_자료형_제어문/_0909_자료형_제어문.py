##Dictionary

#dic = {'name':'pey','phone':'01092938273','birth':'931005'} #'키':'밸류'

#print(dic['name'])

#a = {1: 'a'}

##추가
#a[2] = 'b'
#print(a[2])

#a['name'] = 'pie' 
#print(a['name'])

#a[3] = [1,2,3]
#print(a[3])
#a[4] = 'a'

##삭제
#del a['name']
##print(a['name'])

#b = dic.keys();
#print(b)

#b= list(a.keys()) #a의 키를 리스트형태로 반환
#print(b)

#b = list(dic.items())#dic의 value값을 리스트로 반환
##지우기
##dic.clear()
##print(dic)

#c = dic.get('name') #없는 값일 경우 에러가 남
#print(c)

#'name' in a #해당 Key가 있는지 조사 

##영화 별점주기

#score = {'하정우':{'베테랑':5.0,'암살':7.0,'뷰티인사이드':4.5},
#         '유아인':{'베테랑':10.0,'암살':3.0,'뷰티인사이드':2.0},
#         '전지현':{'베테랑':1.0,'암살':10.0,'뷰티인사이드':0.5},
#         '한효주':{'베테랑':1.0,'암살':2.0,'뷰티인사이드':10.0}}
#print(score.get('하정우'))#하정우의 영화 평점
#print(score['하정우'])#하정우의 영화 평점
#print(score['유아인']['암살'])#유아인 암살의 평점

##제어문
#answer=input("Would you like express shipping? (Yes or No)")
#myanswer = answer.lower()
#if myanswer == "yes" :
#    print("That will be an extra $10")
#print("Have a nice day")

#pass : 아무런 일도 하지 않도록 할 때

#pocket = ['paper','money','cellphone']
#if 'money' in pocket :
#    pass
#else:
#    print('카드를 꺼내라')
##한줄로 되어있을때
#pocket = ['paper', 'money', 'cellphone']
#if 'money' in pocket: pass 
#else: print("카드를 꺼내라")

#a = [(1,2), (3,4), (5,6)] #Tuple에 존재하는 항목을 담아 출력할 수 있음.
#for (first, last) in a:
#   print(first + last)

#for steps in range(1,10,2):
#    print(steps)

#marks = [90, 25, 67, 45, 80] 
#for number in range(len(marks)):
#    print(number)

#for i in range(1,10): 
#    for j in range(1, 10): 
#        print("%d * %d = %d" %(i, j,i*j),end = " ") 
#    print('') #,end = " "을 입력하면 줄바꿈이 되지 않음.

#Turtle(그리기)

import turtle #라이브러리 불러오기
#for steps in range(4) :
#    turtle.forward(100)
#    turtle.right(90)
#for steps in range(4) : 
#    turtle.forward(100) 
#    turtle.right(90) 
#    for moresteps in range(4) : 
#        turtle.forward(50) 
#        turtle.right(90)

#nSides = 8
#for colors in ['red','blue','green','black'] :
#    for steps in range(nSides) :
#        turtle.color(colors)  
#        turtle.forward(100) 
#        turtle.right(360/nSides) 
#        for moresteps in range(nSides) : 
#            turtle.forward(50) 
#            turtle.right(360/nSides)

#for steps in ['red','blue','green','black'] : 
#    turtle.color(steps) 
#    turtle.forward(100) 
#    turtle.right(90)

#메뉴 만들기
prompt = """
1. Add 
2. Del 
3. List 
4. Quit

Enter number: """
number = 0 
while number != 4: 
    print(prompt,  end="") 
    number = int(input())