#pragma once
#ifdef MEDIANLIB_EXPORTS
#define MEDIANLIB_API __declspec(dllexport)
#else
#define MEDIANLIB_API __declspec(dllimport)
#endif
extern "C" {
   MEDIANLIB_API double calculate_median(const double* arr, int size);

}

 


