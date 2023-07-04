li = [[1,3],[1,1],[5,1]]
answer_list = []
for i in li:
    answer_list.append(i[0])
    answer_list.append(i[1])
print(answer_list)
answer_list_set = set(answer_list)
answer_dict = {key : 0 for key in answer_list_set}
print(answer_dict)
for i in answer_list:
    answer_dict[i] +=1
    
print(answer_dict)
for key, value in answer_dict.items():
    if value % 2 ==1:
        print(key)
        
        
a = []
b = []   
for i in li:
    a.append(i[0])
    b.append(i[1])
print(a)
print(b)
seta = set(a)
setb = set(b)

aa= seta-setb
bb = (setb-seta)
resultb = list(aa)
resulta = list(bb)
answer = []
answer.append(resulta[0])
answer.append(resultb[0])
print(answer)

