import ctypes
import time
import random
from datetime import datetime


#Python реализация

def py_array_median(arr):
    """Python реализация медианы массива"""
    if len(arr) == 0:
        return 0.0

    data = sorted(arr)
    n = len(data)

    if n % 2 == 1:
        return data[n // 2]
    else:
        return (data[n // 2 - 1] + data[n // 2]) / 2


def py_median_n_times(arr, iterations):
    if iterations <= 0:
        return 0.0, 0.0

    start = time.perf_counter()
    total = 0.0
    for _ in range(iterations):
        total += py_array_median(arr)
    end = time.perf_counter()

    return end - start, total


#C++ реализация

def cpp_median_n_times(lib, arr, iterations):
    if lib is None or iterations <= 0:
        return 0.0, 0.0

    n = len(arr)
    c_arr = (ctypes.c_double * n)(*arr)

    start = time.perf_counter()
    total = lib.array_median_n_times(c_arr, n, iterations)
    end = time.perf_counter()

    return end - start, total


#Загрузка DLL

def load_cpp_library():
    try:
        lib = ctypes.CDLL("median.dll")
        lib.array_median.argtypes = (ctypes.POINTER(ctypes.c_double), ctypes.c_int)
        lib.array_median.restype = ctypes.c_double

        lib.array_median_n_times.argtypes = (
            ctypes.POINTER(ctypes.c_double),
            ctypes.c_int,
            ctypes.c_int
        )
        lib.array_median_n_times.restype = ctypes.c_double

        return lib
    except Exception as e:
        print("Ошибка загрузки DLL:", e)
        return None


#Тестирование

VECTOR_SIZE = 1000
TESTS = [
    (10000, "10000 итераций"),
    (50000, "50000 итераций"),
    (100000, "100000 итераций")
]


def compare_performance():
    print("=" * 80)
    print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ: C++ DLL vs PYTHON")
    print("Задача: вычисление медианы массива")
    print("=" * 80)

    cpp_lib = load_cpp_library()

    random.seed(42)
    arr = [random.uniform(0, 100) for _ in range(VECTOR_SIZE)]

    print("\n[ПРОВЕРКА КОРРЕКТНОСТИ]")
    py_result = py_array_median(arr)

    if cpp_lib:
        n = len(arr)
        c_arr = (ctypes.c_double * n)(*arr)
        cpp_result = cpp_lib.array_median(c_arr, n)

        if abs(py_result - cpp_result) < 0.0001:
            print(f"✅ Результаты C++ ({cpp_result:.6f}) и Python ({py_result:.6f}) совпадают.")
        else:
            print("⚠️  Результаты различаются!")
    else:
        print(f"Python результат: {py_result:.6f}")

    results = []

    print("\n" + "=" * 80)
    print("ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ")
    print("=" * 80)

    for iterations, desc in TESTS:
        print(f"\n--- Тест: {desc}, размер массива {VECTOR_SIZE} ---")

        py_time, py_total = py_median_n_times(arr, iterations)
        print(f"Python общее время: {py_time:.2f} c")

        if cpp_lib:
            cpp_time, cpp_total = cpp_median_n_times(cpp_lib, arr, iterations)
            print(f"C++ общее время: {cpp_time:.3f} c")

            speedup = py_time / cpp_time if cpp_time > 0 else 0
            print(f"Ускорение C++ над Python: {speedup:.2f}x")
        else:
            cpp_time = 0
            speedup = 0

        results.append((iterations, cpp_time, py_time, speedup))

    print("\n" + "=" * 80)
    print("ИТОГОВАЯ ТАБЛИЦА РЕЗУЛЬТАТОВ")
    print("=" * 80)
    print(f"{'№':<3} {'Итерации':<12} {'C++ (с)':<10} {'Python (с)':<12} {'Ускорение':<10}")
    print("-" * 80)

    for i, r in enumerate(results, 1):
        print(f"{i:<3} {r[0]:<12} {r[1]:<10.2f} {r[2]:<12.2f} {r[3]:<10.2f}")

    print("\n" + "=" * 80)
    print(f"Тестирование завершено: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)


if __name__ == "__main__":
    compare_performance()
