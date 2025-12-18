#include "pch.h"
#include "median.h"
#include <algorithm>
#include <cmath>
#include <ctime>
MEDIANLIB_API double calculate_median(const double* arr, int size) {
   clock_t start_time = clock();
   if (size <= 0 || arr == nullptr) {

       return 0.0;
   }
   double* data = new double[size];
   std::copy(arr, arr + size, data);
   std::sort(data, data + size);
   double median = 0.0;
   int mid = size / 2;

   if (size % 2 == 0) {

       median = (data[mid - 1] + data[mid]) / 2.0;
   }
   else {
       median = data[mid];
   }
   delete[] data;
   clock_t end_time = clock();
   double elapsed_time = static_cast<double>(end_time - start_time) / CLOCKS_PER_SEC;
   return elapsed_time;

}
