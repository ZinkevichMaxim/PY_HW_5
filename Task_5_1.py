# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.

# Функция не должна ничего выводить, только возвращать значение.

# Пример:


# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8

a = int(input('Введите число a \n'))
b = int(input('Введите числ b \n'))

def f(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return 1 / f(a, -b)
    else:
        return a * f(a, b-1)

res = f(a, b)
print(res)

#   https://xn-----6kcjd7aa0cfnmaec4e.xn--p1ai/%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%BE-%D0%BD%D0%B0%D0%BF%D0%B8%D1%88%D0%B8%D1%82%D0%B5-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8E-f-%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D0%B0%D1%8F-%D0%BD%D0%B0-%D0%B2/#:~:text=%D0%94%D0%BB%D1%8F%20%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B8%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8,%D0%B8%20b%2D1.