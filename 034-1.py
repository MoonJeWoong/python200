from time import sleep
for i in range(100):
    msg = 'Loading%d%%'%(i+1)
    print(msg,end='')
    print('\r',end='')
    print('*'*(i+1),end='')
    sleep(0.1)
