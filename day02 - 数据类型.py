#1. int型：所有的整数
num1 = 10
num2 = -10
num3 = 0
print(type(num1), type(num2),type(num3))

#2. 浮点数类型 ：所有的小数
num4 = 1.5
print(type(num4))

#3. 布尔类型 ：只有True,False两种，且严格区分大小写
#布尔类型可以被当作整数类型计算，True=1 False = 0
print(type(True),type(False))
print(True+1)

#4. 复数类型 固定格式为 a+bj
num5 = 1+2j
num6 = 2+3j
print(type(num5), type(num6))
print(num5+num6)

#5. 字符串类型：用引号引起来的部分都属于字符串
name = "hello"
name1 = 'world'
#多行文本可以用三引号
name3 = """hello
 world"""