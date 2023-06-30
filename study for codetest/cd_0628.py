## 입력값 띄어쓰기로 2개 이상 받을 때 map 쓰기
# num = int(input())
# for i in range(1,num+1):
#     a, b = map(int, input().split())
#     print(f'Case #{i}: {a+b}')
    
    
# num = int(input())
# for i in range(1, num+1):
#     a, b = map(int, input().split())
#     print(f'Case #{i}: {a} + {b} = {a+b}')
    


# num = int(input())
# for i in range(1,num+1):
#     blink = ' ' * (num-i)
#     star = '*' * i
#     print(blink + star)
    
## try, except 문 추가해야 오류 안남
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)    
#     except:
#         break
    
# a,b = map(int, input().split())
# a_list = list(range(1,(a+1)))
# a_dict = {num : 0 for num in a_list}
# for i in range(1, b+1):
#     a,b,c = map(int, input().split())
#     for j in range(a, b+1):
#         a_dict[j] = c
        
# result_list = list(a_dict.values())
# print(' '.join(map(str, result_list)))




# a,b = map(int, input().split())
# a_list = list(range(1,a+1))
# a_dict = {num:num for num in a_list}
# print(a_dict)

# for i in range(1, b+1):
#     a,b = map(int, input().split())
#     inter = a_dict[a]
#     a_dict[a] = a_dict[b]
#     a_dict[b] = inter
    
# result_list = list(a_dict.values())
# print(' '.join(map(str, result_list)))





# total_list = list(range(1,31))
# attend_list = []
# attend_dict = {num:0 for num in total_list}
# for i in range(28):
#     num = int(input())
#     attend_list.append(num)

# ## 리스트 차집합 방법 2개
# result_list = [num for num in total_list if num not in attend_list]
# #result_list = list(set(total_list) - set(attend_list))

# ## sort 방법 2개 
# #result_list.sort()
# result_list = sorted(result_list)
# for i in result_list:
#     print(i)


# num = int(input())
# calnum = input()
# if len(calnum) == num:
#     calnum_list = list(calnum)
#     result_list = [int(num) for num in calnum_list]
#     print(sum(result_list))


compare_list = []
for i in range(10):
    num = int(input())
    compare_list.append(num % 42)
print(len(set(compare_list)))
    