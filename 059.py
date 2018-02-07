import time
count=1
try:
    while True:
        print(count)
        count += 1
        time.sleep(0.5)
except KeyboardInterrupt:
    print('program was stopped by user')
