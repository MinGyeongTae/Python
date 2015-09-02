
print("한글") #기본 한국어에서 UTF-8로 바꿀것.

print("Hello World")
print('I have %3d cats' % 6)
print("I have {0:d} cats".format(6))
print("Here are the numbers!"+ \
      " The first is{0:d} The second is{1:4d} ".format(7,8))

#salary = int(input('Please enter your salary : '))
#bonus = int(input('Please enter your bonus : '))

#payCheck = salary+ bonus

#print(payCheck)

#print(type(payCheck))

print('''Hickory Dickory Dock! The mouse ran up the clock''')

print("="*10)

name="greenjoa" 
print(name[0])
print(name[1]) 
print(name[2]) 
print(name[3]) 
print(name[-4])
print(name[-3])
print(name[-2])
print(name[-1])


#• name[:5] : 처음부터 지정된 범위까지 
#• name[5:] : 지정된 위치부터 끝까지

info = "201111289_민경태"
sid = info[:9]
sname = info[9:]
print(sid +" " +sname)

#오른쪽 정렬 
a ="I eat %10s apples." % "five"
print(a)
#왼쪽 정렬 
a ="I eat %-10s apples." % "five"
print(a)

# %를 나타내기
a ="Error is %d%%." % 98 
print(a)

## 이름으로 치환하기
#"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3) 

## 정렬하기

##좌측 정렬 
# "{0:<10}".format("hi")
##우측 정렬 
# "{0:>10}".format("hi") 
##가운데 정렬 
# "{0:^10}".format("hi")
## 공백 채우기
#"{0:=^10}".format("hi")

myin = input("종료할까요? (Y : 예, N : 아니요)")
real = myin.lower()
print(real)