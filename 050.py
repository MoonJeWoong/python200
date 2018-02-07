class MyClass:
    var='Hello!!'
    def sayHello(self):
        param1= 'hello~'
        self.param2 = 'Hi'
        print(param1)
        print(self.var)

obj = MyClass()
print(obj.var)
obj.sayHello()

# 클래스에서 선언되는 변수에는 클래스멤버와 인스턴스 멤버가 있다.
# 클래스멤버는 클래스 메소드 바깥에서 생성되고 인스턴스 멤버는 클래스의 메소드안에서 self인자와 함께 실행이되는 변수이다.
# self.var 변수가 초기화되는 시점은 sayHello가 호출되는 시점이다.
# 따라서 인스턴스 멤버들은 클래스 생성자에서 선언되는 것이 일반적이다.
