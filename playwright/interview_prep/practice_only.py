numbers1 = [ 31,12,23,42,5,36,8]
tripled_numbers = map(lambda x : x*3 ,numbers1)
print(list(tripled_numbers))

even_numbers = filter(lambda x : x%2 == 0 , numbers1)
print(list(even_numbers))

sorted_List = sorted(numbers1)
print(sorted_List)