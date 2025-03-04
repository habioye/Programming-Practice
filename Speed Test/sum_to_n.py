#!/usr/bin/env python3

# Python code
import time

def sum_python(n):
	result = 0
	for i in range(1, n + 1):
		result += i
	return result

n = 10000000
start_time = time.time()
sum_python(n)
end_time = time.time()
print(f"Python: Sum of 1 to {n} is {sum_python(n)} calculated in {end_time - start_time:.4f} seconds")
