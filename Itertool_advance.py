# # from itertools import product
# # a = [1,2,3]
# # b = [3]

# # prod = product(a,b, repeat=2)
# # print(list(prod))

# from itertools import permutations
# a = [1,2,3]
# perm = permutations(a,2)
# print(list(perm))

# from itertools import combinations, combinations_with_replacement
# a = [1,2,3]
# comb = combinations(a,2)
# print(list(comb))
# comb_wr = combinations_with_replacement(a,2)
# print(list(comb_wr))

# from itertools import accumulate #sum of the successive numbers
# import operator
# a = [1,5,3,4]
# acc = accumulate(a, func=max)
# print(a)
# print(list(acc))

# from itertools import groupby
# def smaller_than_3(x):
#     return x ==3
# persons = [{"name": "arati", "age":22},{"name": "bidesh", "age":22},{'name':"roshan", 'age':21}, {"name": "hush", "age":27}]

# a = [1,2,3,4]
# group_obj = groupby(persons, key = lambda x:x['age'])
# for key, value in group_obj:
#     print(key,list(value))
    
# from itertools import count, cycle, repeat
# a = [1,2,3]
# for i in repeat(1, 4):

#     print(i)
    # if i == 15:
    #     break
    
    
    

        
