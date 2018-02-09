msg = input('input your message: ')
msglen = len(msg.encode())
#msglen = len(msg)
print('your message`s length is %d' %msglen)

#한글하고 영어하고 그냥 len을 실행시키면 길이는 같게 나오지만 encode를 쓰면 문자열이 유니코드형식이 아니라 바이트 객체로 변환되기 때문에 크기가 달라지게 된다.
