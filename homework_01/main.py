def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    return [number ** 2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(numbers):
    prime_list = []
    for num in numbers:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_list.append(num)
    return prime_list


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    if filter_type == ODD:
        return list(filter(lambda x: x % 2 == 1, numbers))
    elif filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, numbers))
    elif filter_type == PRIME:
        return is_prime(numbers)
