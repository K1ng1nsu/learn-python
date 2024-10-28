# 정확한 연산을 위해서는 Decimal class 사용
# Decimal 객체를 생성할 때는 """문자열"""로 숫자를 입력해야 합니다.
# #그렇지 않으면 부동 소수점 문제가 그대로 발생할 수 있습니다
from decimal import Decimal

a = 10
b = 3


def p(text):
    print(text)


# result = Decimal("10") / Decimal("3")
# p(result)

# p(a + b)  # 13
# p(a - b)  # 7
# p(a * b)  # 30
# p(a / 3)  # 3.3333335
# p(a // b)  # 3
# p(a**b)  # 1000
# p(a % b)  # 1

##############비교 연산자
# p(a == b)  # False
# p(a != b)  # True
# p(a > b)  # True
# p(a >= b)  # True
# p(a < b)  # False
# p(a <= b)  # False

# c = "10"
# p(a == c)  # False
##############

############## 논리 연산자
true = True
false = False

# p(true and false)  # False
# p(true or false)  # True
# p(not true)  # False
# p(true and not false)  # True
# p(a and b)  # 3     --> 자바스크립트 true && 'something' 이랑 같음
# p(False and b)  # False      -->
# p(a or b)  # 10     -->
# p(False or b)  # 3      --> 자바스크립트 False || 'something' 이랑 같음

# Falsy 값
# 빈 시퀀스 및 컬렉션: [], (), {}, set(), "", range(0)  --> 빈 시퀀스 및 컬렉션이 Falsy라는게 자바스크립트와의 차이점?인듯
# 숫자: 0, 0.0, 0j
# 상수: None, False

############## 멤버십 연산자(in, not in) 특정 값이 시퀀스에 포함되어 있는지 확인
############## 식별 연산자(is, is not)- 동일객체 참조 비교
arr = [1, 2, 3, 4, 5]
arr2 = arr
# p(arr)
# p(5 in arr)  # True
# p(6 not in arr)  # True

# p(arr is arr2)  # True
# p(arr is not arr2)  # False

############## 3항 연산자
# value_if_true if condition else value_if_false

# c = "짝수" if a % 2 == 0 else "홀수"
# p(c)  # 짝수


##############
############## 타입 연산
# p(not not 1)
# p(type(bool(1)))
