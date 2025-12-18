 
import ctypes

import time

import random

import math

# Тестирование C++ модуля

try:

    median_lib = ctypes.CDLL('./median.dll')

except OSError as e:

    print(f"Ошибка загрузки DLL: {e}. Проверьте путь и разрядность.")

    exit(1)

median_lib.calculate_median.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int]

median_lib.calculate_median.restype = ctypes.c_double
 

def generate_random_array(size):

    """Генерирует массив случайных чисел."""

    return [random.uniform(0.0, 1000.0) for _ in range(size)]

# Функция на чистом Python

def calculate_median_py(arr):

    """Вычисляет медиану на чистом Python."""

    if not arr:

        return 0.0

    sorted_arr = sorted(arr)

    n = len(sorted_arr)

    mid = n // 2

    if n % 2 == 0:

        return (sorted_arr[mid - 1] + sorted_arr[mid]) / 2.0

    else:

        return sorted_arr[mid]

 
# Проведение замеров

test_iterations = [10000, 50000, 100000]

results = []

print("Начинаем замеры производительности...")

print("-" * 50)

for i, N in enumerate(test_iterations, 1):

    print(f"\nТест {i}: N = {N:,}")

    arr = generate_random_array(N)

    c_arr = (ctypes.c_double * N)(*arr)

    cpp_time = median_lib.calculate_median(c_arr, N)

 
    py_start = time.perf_counter()

    _ = calculate_median_py(arr)

    py_time = time.perf_counter() - py_start

 
    results.append([i, N, round(cpp_time, 6), round(py_time, 6)])

    print(f"  C++ время:  {cpp_time:.6f} с")

    print(f"  Python время: {py_time:.6f} с")

    if py_time > 0:

        print(f"  Отношение (Python/C++): {py_time / cpp_time:.2f}")

 
#Вывод таблицы

print("\n" + "="*50)

print("ИТОГОВАЯ ТАБЛИЦА ЗАМЕРОВ")

print("="*50)

print(f"{'№ Теста':<10} {'Кол-во итераций':<18} {'C++ (с)':<12} {'Python (с)':<12}")

print("-" * 50)

for row in results:

    print(f"{row[0]:<10} {row[1]:<18,} {row[2]:<12.6f} {row[3]:<12.6f}")

 
if results:

    avg_ratio = sum(r[3]/r[2] for r in results if r[2] > 0) / len(results)

    faster = "C++" if avg_ratio > 1.0 else "Python"

    print(f"Среднее отношение времени выполнения (Python/C++): {avg_ratio:.2f}")

    print(f"Модуль на C++ быстрее в {avg_ratio:.2f} раз.")

else:

    print("Нет данных для вывода.")
