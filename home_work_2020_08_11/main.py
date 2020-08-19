import operator
import datetime
from functools import wraps
from itertools import repeat

# common variables
n = 10
list_numbers = list(range(n))


# decorators
def count_time(func):
    @wraps(func)
    def wrapper(*args):
        start_time = datetime.datetime.now()
        res = func(*args)
        time_spent = datetime.datetime.now() - start_time
        print('time spent for:', func.__name__, time_spent)
        return res

    return wrapper


def show_iterations(func):
    func.count = 0
    @wraps(func)
    def wrapper(*args):
        func.count += 1
        print('_' * func.count, '-->', func.__name__, '({0})'.format(func.count))
        res = func(*args)
        func.count -= 1
        print('_' * func.count, '<--', func.__name__, '({0})'.format(func.count), '==', res)
        return res

    return wrapper


# task #1
@count_time
def calculate_power_for_collection(input_list, pow_number=2):
    power_list = repeat(pow_number, len(input_list))
    return list(map(operator.ipow, input_list, power_list))


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

    if numbers_type == 'even':
        return list(filter(lambda x: x % 2 == 0, input_list))
    if numbers_type == 'odd':
        return list(filter(lambda x: x % 2 != 0, input_list))
    if numbers_type == 'prime':
        return list(filter(get_prime, input_list))


def get_prime(x):
    if x <= 1:
       return True
    temper: int = 2
    while x % temper != 0:
        temper += 1
    return temper == x


print("task #2")
NUMBERS_TYPE = 'even'  # 'even/odd/prime'
filtered_list = get_filtered_numbers(list_numbers, NUMBERS_TYPE)
print('source list:', list_numbers)
print('filtered to get', NUMBERS_TYPE, 'numbers')
print('final list:', filtered_list)
print('')


# task #3
@show_iterations
def return_next_phi(n):
    if n < 2:
        return 1
    return return_next_phi(n - 1) + return_next_phi(n - 2)


print()
print('task #3 ver.2')
maxcount = 5
start_time = datetime.datetime.now()
list_numbers = list(range(maxcount))
res_phi = [0, 1, ]
counter_phi = 0
for i in list_numbers:
    if i > 1:
        res_phi.append(return_next_phi(i))

print('phi list', end=": ")
for i in res_phi:
    print(i, end=", ")

print()
time_spent = datetime.datetime.now() - start_time
print('time spent for:', return_next_phi.__name__, time_spent)
