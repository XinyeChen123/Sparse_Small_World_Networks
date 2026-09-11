'''
from datetime import datetime

now = datetime.now()
time_string = now.strftime("%H:%M:%S")
print("Formatted Time:", time_string)
sec = now.strftime("%S")
min = now.strftime("%M")
hr = now.strftime("%H")
print((int(sec) / int(min) * int(hr)) + int(sec))
'''
import numpy as np
from datetime import datetime
p = 0.5
now = datetime.now()
time_string = now.strftime("%H:%M:%S")
sec = now.strftime("%S")
min = now.strftime("%M")
hr = now.strftime("%H")
random_seed = int((int(sec) / int(min) * int(hr)) + int(sec))
r = np.random.default_rng(seed=random_seed)
a = r.random()
print(a)
if a < p:
    print("r is less than P")