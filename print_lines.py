import time
import os

with open('README.md', 'r') as f:
	for line in f.readlines():
		print(line)
		time.sleep(1)