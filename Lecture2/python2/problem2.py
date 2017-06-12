def triangle_numbers(count):
    '''A generator to generate count
    number of Triangle numbers'''
    sum = 1
    next_num = 2
    for i in range(count):
        yield sum
        sum += next_num
        next_num += 1

n = int(raw_input("How many triangle numbers: "))
for tri_num in triangle_numbers(n):
    print tri_num