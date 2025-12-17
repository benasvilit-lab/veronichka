#pragma once

#ifdef _WIN32
#ifdef MEDIAN_EXPORTS
#define MEDIAN_API __declspec(dllexport)
#else
#define MEDIAN_API __declspec(dllimport)
#endif
#else
#define MEDIAN_API
#endif

extern "C" {
    MEDIAN_API double array_median(const double* arr, int size);
    MEDIAN_API double array_median_n_times(const double* arr, int size, int iterations);
}
