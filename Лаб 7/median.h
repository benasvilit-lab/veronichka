#pragma once
#ifdef MYLIBRARY_EXPORTS
#define MYLIBRARY_API __declspec(dllexport)  // Для компиляции библиотеки
#else
#define MYLIBRARY_API __declspec(dllimport) // Для использования библиотеки
#endif

extern "C" {
    MYLIBRARY_API int add_int(int num1, int num2);   // Функция для сложения целых чисел
    MYLIBRARY_API float add_float(float num1, float num2);  // Функция для сложения чисел с плавающей точкой
    MYLIBRARY_API float compute_sin(int N);  // Функция вычисления синуса для N случайных чисел
}