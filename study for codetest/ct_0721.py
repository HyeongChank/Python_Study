# elist = ['a', 'e', 'i','o','u']

# while True:
#     count =0
#     context = input()
#     if context[0] == '#':
#         break
#     contextlist = list(context)
#     contextlist_lower = [i.lower() for i in contextlist]
#     for i in contextlist_lower:
#         for j in elist:
#             if i ==j:
#                 count +=1
#     print(count)
    

n = int(input())
context_list = []
result = []
for i in range(n):
    context = input()
    context_list.append(context)
    lengthcontext = len(context)
for i in range(lengthcontext):
    cont_set = set([c[i] for c in context_list])
    if len(cont_set) > 1:
        result.append('?')
    else:
        result.append(context_list[0][i])
result_text = ''.join(result)
print(result_text)