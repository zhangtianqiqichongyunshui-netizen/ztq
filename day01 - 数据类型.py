#整数类型 即没有小数部分的数字，包括正整数、负整数、0
#整数数据类型可以由十进制、二进制、八进制、十六进制表示
num1 = 123
num2 = 0b101010
num3 = 0o765
num4 = 0x78A2
print(num1)
print(num2)
print(num3)
print(num4)

#浮点数类型 即包含小数部分的数字
height = 178.9
print(type(height))
number = 1.2E10
print(number,type(number))

#浮点数的尾数可能不确定
print(0.2+0.1)
print(round(0.2+0.1,1)) # round函数可以保留浮点数计算的位数

#浮点数类型也包括虚数
x = 123+456j
print("x的实部：",x.real)
print("x的虚部：",x.imag)