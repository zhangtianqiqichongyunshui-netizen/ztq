#隐式转换
x=10
y=3
z = x/y
print(z,type(z))

#float类型转换成int型,只保留整数部分
print("float类型转换成int型",int(3.14))
print("float类型转换成int型",int(3.5734))
print("float类型转换成int型",int(-3.14))
print("float类型转换成int型",int(-3.3241))
print("int型转成str类型：",str(3))

print("将十进制转成十六进制:",hex(123))
print("将十进制转成八进制:",oct(123))
print("将十进制转成二进制:",bin(123))