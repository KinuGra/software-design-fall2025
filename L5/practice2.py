import time

N = 1000
M = 1000
array = list(range(0, N * M + 1))

time_sta = time.perf_counter()
array.sort(reverse=True)
time_end = time.perf_counter()
time = time_end - time_sta
print(time)
