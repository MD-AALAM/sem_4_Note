import os

os.mkdir("os_module/data")
for i in range(0,10):
    os.mkdir(f"os_module/data/day{i+1}")

#agar os_module name ka folder already majood ho to waha pe hm check laga sakte hai
# os.mkdir("data") ke uper
# if(not os.path.exist("os_module/data")):
    # os.mkdir(f"os_module/data/day{i+1}")