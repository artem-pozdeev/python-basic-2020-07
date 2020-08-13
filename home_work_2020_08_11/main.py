import operator
import datetime
from functools import wraps

# common variables
n = 10
list_numbers = [i for i in range(0, n)]


# decorators
def count_time(func):
    @wraps(func)
    def wrapper(arg1, arg2):
        start_time = datetime.datetime.now()
        res = func(arg1, arg2)
        end_time = datetime.datetime.now()
        time_spent = end_time - start_time
        print('time spent for:', func.__name__, time_spent)
        return res
    return wrapper


def count_iterations(func):
    @wraps(func)
    def wrapper(arg1, arg2, arg3):
        print('-' * arg3, '>', arg3)
        res = func(arg1, arg2, arg3)
        print('-' * arg3, '>', arg3)
        return res
    return wrapper


# task #1
@count_time
def calculate_power_for_collection(input_list, pow_number=2):
    power_list = list_numbers.copy()
    for i in power_list:
        power_list[i] = pow_number

    output_list = list(map(operator.ipow, input_list, power_list))

    return output_list


print('task #1')
pow_number = 2
powered_list = calculate_power_for_collection(list_numbers, pow_number)
print('source list:', list_numbers)
print('powered in', pow_number)
print('final list:', powered_list)
print('')


# task #2
@count_time
def get_filtered_numbers(input_list, numbers_type):

    def get_prime(x):
        if x == 1:
            return True
        temper: int = 2
        while x % temper != 0:
            temper += 1
        return temper == x

    if numbers_type == 'even':
        return list(filter(lambda x: x % 2 == 0, input_list))
    elif numbers_type == 'odd':
        return list(filter(lambda x: x % 2 != 0, input_list))
    elif numbers_type == 'prime':
        return list(filter(get_prime, input_list))


print('task #2')
NUMBERS_TYPE = 'even'  # 'even/odd/prime'
filtered_list = get_filtered_numbers(list_numbers, NUMBERS_TYPE)
print('source list:', list_numbers)
print('filtered to get', NUMBERS_TYPE, 'numbers')
print('final list:', filtered_list)
print('')


# task #3
@count_iterations
def apend_next_phi(collect, max_count=20, counter=0):
    """
    :param collect: list of numbers phi
     :param counter: counting calculated numbers
    :param max_count: contains maximum iterations
    :return: collect - list with appended phi number
    """

    collect.append(collect[-1] + collect[-2])
    counter += 1
    if max_count == counter:
        return collect
    else:
        apend_next_phi(collect, max_count, counter)
    return collect

print('task #3')
coll = [0, 1]
maxcount = 15
res_phi = apend_next_phi(coll, 15, 0)
print('calculating', maxcount, 'items of phi numbers')
print('phi list', end=": ")
for i in res_phi:
    print(i, end=", ")
