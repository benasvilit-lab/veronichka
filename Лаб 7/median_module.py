import time

def calculate_median(arr) :
    if len(arr) == 0 :
        return 0.0

        data = sorted(arr)
        n = len(data)

        if n % 2 == 1:
            return data[n // 2]
        else:
            return (data[n // 2 - 1] + data[n // 2]) / 2


    def calculate_median_n_times(N, arr):
        start_time = time.perf_counter()
        total = 0.0
        for i in range(N) :
            result = calculate_median(arr)
            total += result

            dummy = total  

            end_time = time.perf_counter()
            return end_time - start_time
