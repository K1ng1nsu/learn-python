"""
f-string
Raw String
파이썬 타입
기본형 8
기본 컬렉션 4
네이밍 컨벤션
맹글링
주석
"""

"""
변수명 lower_snake_case
상수명 UPPER_SNAKE_CASE
함수명 lower_snake_case
클래스명 PascalCase
모듈명 lower_snake_case
패키지명 lower_snake_case
private 멤버 _lower_snake_case 언더스코어로 시작
맹글링 __lower_snake_case 언더스코어 두 개로 시작
"""

"""
맹글링이란? 
class Base:
    def __init__(self):
        self.__value = 10  # 이름 맹글링
        
base = Base()

print(base.__value)  # AttributeError 어트리뷰트가 없다고 나옴
# __value로는 접근이 불가능 맹글링이 되었기 때문에, 접근하기 위해서는 _Base__value로 가야함 (속성 이름이 바뀜)
# 단 클래스 내에서는 __value로 접근 가능


맹글링은 언제?
1. 하위 클래스가 상속 받을때의 오버라이딩을 못하게할 의도로 사용됨
2. 캡슐화 (사실 그냥 단일 언더스코어로 하면 됨) - deprecated

"""


# print("Welcome to the Band Name Generator.")

# cityName = input("What's the name of the city you grew up in?\n")

# petName = input("What's your pet's name? \n")

#### f-string ####
# print(f"Your band name could be {cityName} {petName}")

# recipe = """1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
# # 2. Knead the dough for 10 minutes.
# # 3. Add 3g of Salt.
# # 4. Leave to rise for 2 hours.
# # 5. Bake at 200 degrees C for 30 minutes."""

# print(recipe)

#### Raw String ####
# raw_string = r"C:\Users\Name\Documents"  # 이스케이프 문자가 무시됨
# print(raw_string)  # 출력: C:\Users\Name\Documents


#### 기본 타입 8개 ####
# print(type("insu"))  # str

# print(type(True))  # bool

# print(type(27))  # int
# print(type(27.7))  # float
# print(type(1 + 2j))  # complex 복소수

# print(type(b"hello"))  # bytes -> 불변 바이트 시퀀스
# print(type(bytearray(b"hello")))  # bytearray -> 가변 바이트 시퀀스

# print(type(None))  # NoneType  --> null에 대항한다고 보면됨


#### 기본 컬렉션 타입 4개 ####

# print(type([1, 2, 3, 4]))  # list 가변적, 순서가 있으며 중복 허용
# print(type((1, 2, 3, 4)))  # tuple 불변, 순서가 있으며 중복 허용
# print(type({1, 2, 3, 4}))  # set 중복을 허용하지 않으며 순서가 없음
# print(type({"test": 1}))  # dict 키-값 쌍으로 저장


#### 타입 변환 ####
### int('1212') float('1.23') str(131241)

# text = "10"
# num = 123
# isNumber = False

# print(float(text), type(float(text)))
# print(type(str(123132)))
