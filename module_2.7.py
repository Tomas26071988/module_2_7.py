def print_params(a: object = 1, b: object = 'строка', c: object = True):
    print(a, b, c)


print_params(b=25, c=[1, 2, 3])

values_list = [1, 'Hello', True]

def print_params(*params):  # ввел args в виде * чтобы передавать неизвестное кол-во параметров
    print(*params)


print_params(*values_list)  # распакрвал список ввел args в виде * для списка
# чтобы передать в параметры (вместо предыдущих)


values_dict = {'a': 5, 'b': 'Hello', 'c': True}


def print_params2(a, b, c):
    print(a, b, c)


print_params2(**values_dict)  # распаковал словарь.

# ВАЖНО! Для распаковки количество параметров списка и словаря дб ровны кол-ву параметров функции
# НЕЛЬЗЯ распаковать одновременно и список и словарь тк совместно у них ШЕСТЬ параметров


values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
