#include "median.h"
#include <vector>
#include <algorithm>

MEDIAN_API double array_median(const double* arr, int size)
{
    if (size <= 0 || arr == nullptr) {
        return 0.0;
    }

    std::vector<double> data(arr, arr + size);
    std::sort(data.begin(), data.end());

    if (size % 2 == 1) {
        return data[size / 2];
    }
    else {
        return (data[size / 2 - 1] + data[size / 2]) / 2.0;
    }
}

MEDIAN_API double array_median_n_times(const double* arr, int size, int iterations)
{
    if (iterations <= 0) {
        return 0.0;
    }

    double total = 0.0;
    for (int i = 0; i < iterations; i++) {
        total += array_median(arr, size);
    }

    return total;
}
