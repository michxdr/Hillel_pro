# 1. Рядки (Strings
def string_length(s: str) -> int:
    return len(s)

def concat_strings(s1: str, s2: str) -> str:
    return s1 + s2


# 2. Числа (int / float)

def square_number(x):
    return x ** 2

def sum_numbers(a, b):
    return a + b

def int_division(a: int, b: int):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

# 3. Списки (Lists)

def average_of_list(numbers: list) -> float:
    return sum(numbers) / len(numbers) if numbers else 0

def common_elements(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))


# 4. Словники (Dictionaries)

def print_dict_keys(d: dict):
    for key in d:
        print(key)

def merge_dicts(d1: dict, d2: dict) -> dict:
    return d1 | d2   # Python 3.9+

# 5. Множини (Sets)

def union_sets(set1: set, set2: set) -> set:
    return set1 | set2

def is_subset(set1: set, set2: set) -> bool:
    return set1.issubset(set2)

# 6. Умовні вирази та цикли

def even_or_odd(n: int) -> str:
    return "Парне" if n % 2 == 0 else "Непарне"

def even_numbers_from_list(numbers: list) -> list:
    return [n for n in numbers if n % 2 == 0]

# 7. Лямбда-функція

is_even_lambda = lambda x: "парне" if x % 2 == 0 else "не парне"

# Приклади використання

if __name__ == "__main__":

    print("1. Рядки")
    print(string_length("Привіт"))
    print(concat_strings("Hello, ", "World"))
    print()

    print("2. Числа")
    print(square_number(5))
    print(square_number(2.5))
    print(sum_numbers(10, 20))
    print(int_division(17, 5))
    print()

    print("3. Списки")
    numbers = [1, 2, 3, 4, 5]
    print(average_of_list(numbers))

    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    print(common_elements(list1, list2))
    print()

    print("4. Словники")
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "b": 4}

    print("Ключі словника d1:")
    print_dict_keys(d1)

    print("Об'єднаний словник:")
    print(merge_dicts(d1, d2))
    print()

    print("5. Множини")
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    set3 = {1, 2}

    print(union_sets(set1, set2))
    print(is_subset(set3, set1))
    print(is_subset(set2, set1))
    print()

    print("6. Умови та цикли")
    print(even_or_odd(10))
    print(even_or_odd(7))
    print(even_numbers_from_list([1, 2, 3, 4, 5, 6]))
    print()

    print("7. Lambda")
    print(is_even_lambda(8))
    print(is_even_lambda(9))
