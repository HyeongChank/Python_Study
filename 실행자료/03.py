"""string = "abcdefghij"

result = ""
for i in range(len(string)):
    if i % 2 == 0:
        result += string[i]

print(result)

슬라이싱 기본 문
string[start:end:step]

s = "Hello, world!"
reversed_s = s[::-1]
print(reversed_s)

s = "hello"
n =3
print(s+str(n))

s = "hello"
s2 = "H" + s[1:]
print(s2)

isalnum(): 문자열이 알파벳과 숫자로만 이루어졌는지 여부를 반환합니다.
isalpha(): 문자열이 알파벳으로만 이루어졌는지 여부를 반환합니다.
isdecimal(): 문자열이 10진수 숫자로만 이루어졌는지 여부를 반환합니다.
isdigit(): 문자열이 숫자로만 이루어졌는지 여부를 반환합니다.
isidentifier(): 문자열이 파이썬 식별자로 사용 가능한지 여부를 반환합니다.
islower(): 문자열이 소문자로만 이루어졌는지 여부를 반환합니다.
isnumeric(): 문자열이 숫자로만 이루어졌는지 여부를 반환합니다.
isprintable(): 문자열이 출력 가능한지 여부를 반환합니다.
isspace(): 문자열이 공백 문자로만 이루어졌는지 여부를 반환합니다.
istitle(): 문자열이 제목 케이스로 이루어졌는지 여부를 반환합니다.
isupper(): 문자열이 대문자로만 이루어졌는지 여부를 반환합니다.
upper(): 문자열의 모든 알파벳을 대문자로 변환한 새로운 문자열을 반환합니다.
lower(): 문자열의 모든 알파벳을 소문자로 변환한 새로운 문자열을 반환합니다.
capitalize(): 문자열의 첫 문자를 대문자로, 나머지 문자를 소문자로 변환한 새로운 문자열을 반환합니다.
title(): 문자열에서 단어의 첫 문자를 대문자로, 나머지 문자를 소문자로 변환한 새로운 문자열을 반환합니다.
swapcase(): 문자열에서 대문자는 소문자로, 소문자는 대문자로 변환한 새로운 문자열을 반환합니다.
find(sub): 문자열에서 지정된 문자열(sub)을 찾아서 그 위치를 반환합니다. 찾지 못한 경우에는 -1을 반환합니다.
rfind(sub): 문자열에서 지정된 문자열(sub)을 뒤에서부터 찾아서 그 위치를 반환합니다. 찾지 못한 경우에는 -1을 반환합니다.
index(sub): 문자열에서 지정된 문자열(sub)을 찾아서 그 위치를 반환합니다. 찾지 못한 경우에는 ValueError 예외가 발생합니다.
rindex(sub): 문자열에서 지정된 문자열(sub)을 뒤에서부터 찾아서 그 위치를 반환합니다. 찾지 못한 경우에는 ValueError 예외가 발생합니다.
count(sub): 문자열에서 지정된 문자열(sub)이 몇 번 등장하는지 카운트하여 반환합니다.



print("avc".upper())
print("aAbdfDFE".swapcase())
print("234d".isalnum())

num = "123987a"
print(str.find("g"))
print(num.isnumeric())
print(str.strip())
print(str.replace("an","o"))


str = "KimHyeong Chan"
string_list = str.split()
string1 = str.split()
print(string1)
print(string_list)


string = "hello world"
string_list = string.split()  # 기본값인 공백을 구분자로 사용
print(string_list)




s = "개발자"
result =""
for i in range(1,11):
    result += s
print(result)
s = "abCD1234"
print(len(s))
print(s[0])
print(s[0:3])
print(s[-3:])
print(s[::-1])
print(s[6])

if len(s)>7:
    print(s[6])
else:
    print("문자열이 없음")

print(s[1:-1])
print(s.upper())
print(s.lower())
print(s.replace("a","e"))
    
s = input("a가 들어가는 문자")
f = s.find("a")
print(s[:f+1])
print(s[f+1:])


sum=0
for i in range(1,1001):
    sen = str(i)      
    for s in sen:
        sum += int(s)
    print(sum)
    sum=0


s = "asdfajgalg"
print(s.replace("a","a\n"))
print(s.replace("a"," a").split(" "))
st = s.replace("a"," a").split(" ")

print("st" , st)
st.remove("")
print("st", st)

list = [1,2,3,4]
print(list)
list.remove(2)
print(list)

even_num = [num for num in range(1,11) if num%2==0]
print(even_num)
"""
words = ['qpple', 'banana', 'cap']
d = []
st = 'asc'
c = st.upper()
print(c)
for i in words:
    d.append(i.upper())
print(d)
print(d.sort())
"""
word_lengths = [len(word) for word in words]
print(word_lengths)
word_upper = [word.upper() for word in words if len(word)>=5]
print(word_upper)
word_replace = [word.replace("a","A++") for word in words]
print(word_replace)

original_list = [[1,2],[3,4],[5,6]]
new_list = [num for sublist in original_list for num in sublist if num%2==0]
print(new_list)

list = [1,2,10,3,4,5]
list[1:4] = []
print(list)
list = [1,8,10,20,3,"kim",4,5,100]
del list[2]
print(list)
list.remove(100)
print(list)
list.pop()
print(list)
list.pop(0)
print(list)
list.clear()
print(list)
list = [1,8,10,20,3,"kim",4,5,100]
for i in list:
    print(i)
iter = iter(list)
print(iter)
print(next(iter))
"""
flist = ["Kim", "lee", "park"]
print(flist)
flist.insert(0,"choi")
print(flist)
flist.insert(3,"ki")
print(flist)
flist.append("eom")
print(flist)
"""
nlist = [1,2,3]
nlist[1] = 17
print(nlist)
addlist = [4,5,6]
nlist.extend(addlist)
print(nlist)
nlist.append(9)
print(nlist)
nlist.sort()
print(nlist)
nlist.insert(2,25)
print(nlist)

list = []
for i in range(0,50):
    list.append(i)
print(list)

list =[]
for i in range(1,51):
    list.append(i*i)
print(list)

l =[1,2,3]
m =[4,5,6]
print(len(l))
result =[]
for i in range(0, len(l)):
    result.append(l[i] + m[i])
print(result)
"""

list = []
result =""

for i in range(5):
    list.append(input("문자열 입력"))
    result += (list[i] + "+")
print(result[:-1])


def calculate(x, y):
    add = x + y
    subtract = x - y
    multiply = x * y
    divide = x / y
    return add, subtract, multiply, divide

result = calculate(10,2)
print(result)

z=1
y =2
print(z, " " , y)
z,y = y,z
print(z, " " , y)





