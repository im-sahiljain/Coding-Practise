sample_dict: dict = {0:['a','b'], 1:['c','d'], 2:['e','f']}
my_copy: dict = sample_dict.copy()

my_copy[0][0] = '!!!'
print(sample_dict)
print(my_copy)
print(id(sample_dict))
print(id(my_copy))