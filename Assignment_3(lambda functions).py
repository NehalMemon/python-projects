from functools import reduce

Input=['apple', 'banana', 'cherry', 'date', 'elderberry']

output=list(filter(lambda x:len(x)>5,Input))
print(output)

Input= [2, 4, 6, 8, 10]

dou_num=list(map(lambda x:x*2,Input))
sum_dou_num=reduce(lambda x,y:x*y, dou_num)
print(sum_dou_num)