def getGradeByPoint(point):
    if point > 90:
        return "A"
    elif point > 80:
        return "B"
    else:
        return "C"


print(getGradeByPoint(80))

# dictionary Mapping 을 switch_case 대용으로 사용하는 방법


# 함수 정의
def apple():
    return "This is an apple."


def banana():
    return "This is a banana."


def cherry():
    return "This is a cherry."


def unknown():
    return "Unknown fruit."


# 딕셔너리 매핑 생성
fruit_switch = {"apple": apple, "banana": banana, "cherry": cherry}


# 함수 호출
def check_fruit(fruit_name):
    # get 메서드로 fruit_switch에서 함수를 가져오고, 기본값으로 unknown 설정
    return fruit_switch.get(fruit_name, unknown)()


print(check_fruit("apple"))  # 출력: This is an apple.
print(check_fruit("grape"))  # 출력: Unknown fruit.


# Match Case After 3.10
# case에 return이 없어도 저절로 break됨
def switch_example(value):
    match value:
        case "apple":
            return "This is an apple."
        case "banana":
            return "This is a banana."
        case "cherry":
            return "This is a cherry."
        case _:  # 기본 케이스 -> default
            return "Unknown fruit."


print(switch_example("banana"))  # "This is a banana."


# 변수 바인딩
def describe_fruit(fruit):
    match fruit:
        case "apple" | "banana" | "cherry" as fruit_name:
            return f"This is a {fruit_name}."
        case _:
            return "Unknown fruit."


print(describe_fruit("apple"))  # 출력: This is a apple.
print(describe_fruit("grape"))  # 출력: Unknown fruit.


# 튜플 매칭
def point_location(point):
    match point:
        case (0, 0):
            return "This is the origin."
        case (x, 0):
            return f"Point on the x-axis at {x}."
        case (0, y):
            return f"Point on the y-axis at {y}."
        case (x, y):
            return f"Point at ({x}, {y})."
        case _:
            return "Unknown location."


print(point_location((0, 0)))  # 출력: This is the origin.
print(point_location((3, 0)))  # 출력: Point on the x-axis at 3.
print(point_location((0, 4)))  # 출력: Point on the y-axis at 4.
print(point_location((3, 4)))  # 출력: Point at (3, 4).


# 딕셔너리 매칭
def check_user(user):
    match user:
        case {"name": name, "age": age}:
            return f"User {name} is {age} years old."
        case {"name": name}:
            return f"User {name}'s age is unknown."
        case _:
            return "Unknown user."


print(check_user({"name": "Alice", "age": 30}))  # 출력: User Alice is 30 years old.
print(check_user({"name": "Bob"}))  # 출력: User Bob's age is unknown.
print(check_user({"age": 25}))  # 출력: Unknown user.


# 클래스 매칭
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def greet(person):
    match person:
        case Person(name="Alice", age=30):
            return "Hello Alice!"
        case Person(name=name, age=age):
            return f"Hello {name}, age {age}!"
        case _:
            return "Unknown person."


person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(greet(person1))  # 출력: Hello Alice!
print(greet(person2))  # 출력: Hello Bob, age 25!
