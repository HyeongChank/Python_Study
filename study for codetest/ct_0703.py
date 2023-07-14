dica = {'a':0, 'b':1}
print(dica.values())

list_dica = list(dica.values())
print(list_dica)


abc = 'abc,def,gh'
list_abc = abc.split(',')
print(list_abc)

sortabc = 'dskfjekwf'
list_sort = sorted(sortabc)
print(''.join(list_sort))



def operate(n):
    for i in range(1,10000000):
        if i % 2 ==0:
            if (i * (i+1)) / 2 >= n:
                up = i - ((i * (i+1)) / 2 - n)
                down = 1 + ((i * (i+1)) / 2 - n)
                print(str(int(up)) + "/" + str(int(down)))
                break
        elif i % 2 ==1 :
            if (i * (i+1)) / 2 >=n :
                up = 1 + ((i * (i+1)) / 2 - n)
                down = i - ((i * (i+1)) / 2 - n)
                print(str(int(up)) + "/" + str(int(down)))
                break
                
operate(7)


# sentence = input()
def operate(sentence):

    sentence_list = list(sentence)
    
    lowercase_letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
    result_dict = {key:-1 for key in lowercase_letters}
    for i in range(0, len(sentence_list)):
        if result_dict[sentence_list[i]] == -1:
            result_dict[sentence_list[i]] = i
        
    answer = list(result_dict.values())
    answer_str = [str(i) for i in answer]
    result = ' '.join(answer_str)
    print(result)
# operate(sentence)




# a, b = map(int, input().split())
answer_list = []
def operate(a, b):
    for i in range(1, 1000):
        for j in range(1, i+1):
            answer_list.append(i)
    print(answer_list)
    print(sum(answer_list[a-1:b]))
    
operate(3,7)



def operate(a,b,c):
    result = 1
    for i in range(1, b):
        result *= a
    print(result % c)
operate(10, 11, 12)





def operate(a,b,c):
    if b==1:
        return a % c
    temp = operate(a,b//2, c)
    
    if b%2 ==0:
        return temp* temp %c
    else:
        return temp*temp * a % c
print(operate(10,11,12))



a,b = map(int, input().split())

coin_list = []
def operate(a,b):
    price = b
    for i in range(a):
        coin_list.append(int(input()))
    coin_list.reverse()
    sum = 0
    for i in coin_list:
    
        if price // i >0:
            sum += (price//i)
            price = price % i
    print(sum)
operate(a,b)