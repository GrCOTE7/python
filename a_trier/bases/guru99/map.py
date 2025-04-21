def square(n):
    return n * n


my_list = range(10)

print(my_list)
print(list(my_list))
print(*my_list)

updated_list = map(square, my_list)
updated_list2 = map(lambda x: x **2, my_list)

print(updated_list)
print(*updated_list)

print(updated_list2)
print(*updated_list2)
print(*[n * n for n in my_list])

my_tuple = ('php','java','python','c++','c')
print(*[s.title() for s in my_tuple])

def myMapFunc(list1, list2):
    return list1+list2

my_list1 = [2,3,4,5,6,7,8,9]
my_list2 = [4,8,12,16,20,24,28]

updated_list1et2 = map(myMapFunc, my_list1,my_list2)
print(updated_list1et2)
print(list(updated_list1et2))

def myMapFunc(list1, tuple1):
    return list1+"_"+tuple1

my_list = ['a','b', 'b', 'd', 'e']
my_tuple = ('PHP','Java','Python','C++','C')

updated_list3 = map(myMapFunc, my_list,my_tuple)
print(updated_list3)
print(list(updated_list3))
