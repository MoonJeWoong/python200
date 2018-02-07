class MyClass():
    def __del__(self):
        print('MyClass 인스턴스 객체가 메모리에서 제거됩니다')

obj=MyClass()
del obj

# 클래스 소멸자
# 클래스 인스턴스를 메모리에서 제거할 때 쓰이는 키워드
