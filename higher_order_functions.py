def square(x):
    return x * x


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        
        result.append(func(i))
    return result




squares = my_map(square, [2,4,5,6,7,8]) 
print(squares)


