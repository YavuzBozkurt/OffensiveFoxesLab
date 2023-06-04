import time

start_time = time.time()

def ellapsed_time(st):
    et = time.time() - st
    return et

while True:
    if (ellapsed_time(start_time)< 30):
        print(ellapsed_time(start_time))
        time.sleep(7)
    else:
        print(ellapsed_time(start_time))
        start_time = time.time()