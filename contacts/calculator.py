class Calculator:
    def __init__(self, num1,num2):  
        #생성자 함수 --> 인스턴스(객체)  _(언더스코어) 2개를 사용하면 접근제한 private
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def divided(self):
        return self.num1 // self.num2

    def cross(self):
        return self.num1 * self.num2

    def minus(self):
        return self.num1 - self.num2

    
if __name__ == '__main__':
    calc = Calculator(6,2) # num1 = 6, num2 = 2
    sumResult = calc.sum()
    diResult = calc.divided()
    crResult = calc.cross()
    miResult =calc.minus()
    print('덧셈결과{}'.format(sumResult))
    print('나눗셈결과{}'.format(diResult))
    print('곱셈결과{}'.format(crResult))
    print('뺄셈결과{}'.format(miResult))


# 결론: 객체지향은 속성이 존재해야한다. 그리고 속성을 정의하는 곳은 __init__(속성파라미터)이다.

#self 는 객체 내부의 속성에 접근하는 키워드
#속성은 은닉화 때문에 반드시 self. 로만 근접할 수 있다.
#이는 보안의 기본처리이다. __init__은 클래스 내부에서만 접근한다.

