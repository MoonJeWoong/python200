try:
    print('hello')
    print(param)
except:
    print('there is an exception')
else:
    print('there is no exception')

try:
    print('Hello')
    print(param)
except:
    print('There is an Error')
finally:
    print('This code must be executed')

try:
    print(param)
except Exception as e:
    print(e)
