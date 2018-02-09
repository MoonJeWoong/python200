h1 = hex(97)
h2 = hex(98)
ret1 = h1 +h2
print(ret1)
a = int(h1, 16)
b = int(h2, 16)
ret2 = a+b
print(hex(ret2))
print('%x' %a)
print('%X' %a) #16진수 대문자 소문자
a = 11
print('%02x' %a)
print('%02X' %a) #16진수 맨 앞에 0붙이기
