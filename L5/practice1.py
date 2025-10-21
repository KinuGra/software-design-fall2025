import time

N = 100000
array = list(range(0, 100001))

time_sta = time.perf_counter()
array.sort(reverse=True)
time_end = time.perf_counter()
time = time_end - time_sta
print(time)
