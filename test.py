from math import sqrt


message: str = 'Добро пожаловать в самую лучшую программу для вычисления '\
          'квадратного корня из заданного числа'

print(message)


def calculate_square_root(Number: float) -> float:
    """ Вычисляет квадратный корень"""
    return sqrt(Number)


def calc(your_number: float) -> None:
    if your_number <= 0:
        return None
    root = calculate_square_root(your_number)
    print(f"Мы вычислили квадратный корень из введённого вами числа."
          f"Это будет: {root}")


calc(25.5)
