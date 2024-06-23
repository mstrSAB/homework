def print_params(a = 1, b = 'строка', c = True):
        print(a, b, c)

print_params()
print_params(b = 25)
print_params(b = 'test1')
print_params(c = 5)
print_params(c = [1,2,3])

def print_params (a, b, c):
   print (a, b, c)

value_list = [20, 30, 40]
values_dict = {'a': 23, 'b': 'slovo', 'c': 'pravda'}
value_list_2 = [20.34, 'slovo3']

print_params(*value_list)
print_params(**values_dict)
print_params(*value_list_2, 2.42)


