# print("Welcome to the tip calcultor!")
# total_bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people_num = int(input("How many people to split the bill? "))
# print(f"Each person should pay: ${(total_bill + total_bill*tip/100)/people_num:.2f}")

############ substring ############

# # str_num[a:b:c]    a부터 b전까지 c(def 1)씩
# # str_num[d]  === str_num[d:d+1]
# # quick guide
# # 뒤집기 p(str_num1[-1::-1])  # 9876543210
# # 특정 문자 포함 p(str_num1[index_of_0 : index_of_9 + 1])  # 0123456789

# str_num1 = "0123456789"
# index_of_0 = str_num1.index("0")
# index_of_9 = str_num1.index("9")


# def p(text):
#     print(text)


# p(str_num1[index_of_0 : index_of_9 + 1])  # 0123456789

# p(str_num1[0])  # 0

# p(str_num1[0:])  # 0123456789

# p(str_num1[:10])  # 0123456789

# p(str_num1[0:1])  # 0

# p(str_num1[-1])  # 9

# p(str_num1[-1::-1])  # 9876543210

# p(str_num1[-2:])  # 89

# p(str_num1[0::2])  # 02468


############ f-string format ############

# pi = 3.141592
# print(f"소수점 두 자리: {pi:.4f}")  # 출력: 소수점 두 자리: 3.14
# 4f 면 5번쨰에서 반올림함

# number = 42
# print(f"10칸 공백 채움: {number:10}")  # 출력: '        42'
# print(f"10칸 0 채움: {number:010}")  # 출력: '0000000042'

# name = "Alice"
# print(f"|{name:<10}|")  # 왼쪽 정렬, 출력: |Alice     |
# print(f"|{name:^10}|")  # 가운데 정렬, 출력: |  Alice   |
# print(f"|{name:>10}|")  # 오른쪽 정렬, 출력: |     Alice|

# value = 5
# print(f"중괄호 출력: {{{value}}}")  # 출력: 중괄호 출력: {5}
