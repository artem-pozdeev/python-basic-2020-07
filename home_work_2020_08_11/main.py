import operator

# common variables
n = 10
list_numbers = [i for i in range(0, n)]


# task #1
def calculate_power_for_collection(input_list, pow_number=2):
    power_list = list_numbers.copy()
    for i in power_list:
        power_list[i] = pow_number

    output_list = list(map(operator.ipow, input_list, power_list))

    return output_list


# pow_number = 2
# powered_list = calculate_power_for_collection(list_numbers, pow_number)
# print('task #1')
# print('source list:', list_numbers)
# print('powered in', pow_number)
# print('final list:', powered_list)
# print('')


# task #2
def get_filtered_numbers(input_list, numbers_type):

    def get_even(x):
        if x % 2 == 0:
            return x

    def get_odd(x):
        if x % 2 != 0:
            return x

    def get_prime(x):
        temper: int = 2
        while x % temper != 0:
            temper += 1
            if temper == x:
                break
        return x

    if numbers_type == 'even':
        return list(filter(get_even, input_list))
    elif numbers_type == 'odd':
        return list(filter(get_odd, input_list))
    elif numbers_type == 'prime':
        return list(filter(get_prime, input_list))



# NUMBERS_TYPE = 'prime'  # 'even/odd/prime'
# filtered_list = get_filtered_numbers(list_numbers, NUMBERS_TYPE)
# print('task #2')
# print('source list:', list_numbers)
# print('filtered to get', NUMBERS_TYPE, 'numbers')
# print('final list:', filtered_list)
# print('')


# task #3
def apend_next_phi(collect, max_count=20, a=0, b=1, counter=0):
    """
    :param collect: list of numbers phi
    :param a: first phi number
    :param b: second phi number
    :param counter: counting calculated numbers
    :param max_count: contains maximum iterations
    :return: collect - list with appended phi number
    """

    c = a + b
    collect.append(c)
    counter += 1
    if max_count == counter:
        return collect
    else:
        apend_next_phi(collect, max_count, b, c, counter)
    return collect


coll = [0, 1]
maxcount = 15
res_phi = apend_next_phi(coll, maxcount)

# print('task #3')
# print('calculating', maxcount, 'items of phi numbers')
# print('phi list', end=": ")
# for i in res_phi:
#     print(i, end=", ")

n = 4
d = 2
while n % d != 0:
    d += 1
print(d == n)