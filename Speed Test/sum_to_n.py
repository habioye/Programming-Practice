#!/usr/bin/env python3

# Python code
import time
import yaml

def sum_python(n):
	result = 0
	for i in range(1, n + 1):
		result += i
	return result

n = 10000000
start_time = time.time()
sum_python(n)
end_time = time.time()
duration = start_time-end_time
print(f"Python: Sum of 1 to {n} is {sum_python(n)} calculated in {duration:.4f} seconds")
with open("Speed.yaml","r+") as f:
	metric = yaml.load(f, Loader= yaml.FullLoader)
	print(metric)
	metric["Sum from 1 to 10000000 Speed(seconds)"]["Python"] = duration
	
	yaml.dump(metric,stream=f,default_flow_style=False, sort_keys=False)
	print(metric)