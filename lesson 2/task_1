def factorial(n):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определён")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def max_of_three(numbers):
    if len(numbers) != 3:
        raise ValueError("Функция принимает кортеж ровно из трёх чисел")
    return max(numbers)


def right_triangle_area(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Длины катетов должны быть положительными числами")
    return 0.5 * a * b


if __name__ == "__main__":
    print(f"Факториал 5: {factorial(5)}")
    nums = (10, 20, 15)
    print(f"Наибольшее число из {nums}: {max_of_three(nums)}")
    cathetus1, cathetus2 = 3, 4
    print(f"Площадь треугольника с катетами {cathetus1} и {cathetus2}: "
          f"{right_triangle_area(cathetus1, cathetus2)}")
