# a,b = map(int, input().split())
# result_list = list(range(1,a+1))
# for i in range(1, b+1):
#     a,b = map(int, input().split())
#     result_list[a-1:b] = result_list[a-1:b][::-1]
# print(' '.join(map(str, result_list)))
    
    
# a = [1,2,3,4,5]
# print(a[3:0:0-1])


###################queue

# from collections import deque

# queue = deque()
# num = int(input())
# for i in range(num):
   
#     anum = int(input())
#     if anum != 0:
#         queue.append(anum)
#     if anum ==0:
#         queue.popleft()
#     print(queue)
# print(sum(queue))


    ######################stack
# num_list = []
# num = int(input())
# for i in range(num):
#     anum = int(input())
#     if anum != 0:
#         num_list.append(anum)
#     if anum ==0:
#         num_list.pop()
# print(sum(num_list))




num = int(input())
for i in range(num):
    sign_list = []
    sign = input()
    for j in sign:
        if j == '(':
            sign_list.append(j)
        elif  j == ')':
            if sign_list:
                sign_list.pop()
            else:
                print("NO")
                break

    else:
        if sign_list:
            print("NO")
        else:
            print("YES")