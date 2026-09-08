from datetime import datetime

now = datetime.now()
time_string = now.strftime("%H:%M:%S")
print("Formatted Time:", time_string)
sec = now.strftime("%S")
min = now.strftime("%M")
hr = now.strftime("%H")
print((int(sec) / int(min) * int(hr)) + int(sec))