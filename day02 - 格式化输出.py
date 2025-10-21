#% 占位符

# %s 字符类
name = "six"
print("name: %s" % name)

# %d  整数类型
age = 18
print("age: %d" % age)
# %3d 表示占用3位整数，不足的默认使用空格占用
print("age: %3d" % age)
print("age: %03d" % age) # 不足3位的部分使用0占用

# %f  浮点数类型 默认有6位占位符
height = 176.5678
id = 10
print("height: %f , 学号: %d" % (height,id))
# %.4f 表示占用小数点后4位数字，不足的使用0表示,会四舍五入
print("height: %.4f" % height)
print("height: %.2f" % height)

# f格式化输出
name1 = '黎明'
age1 = 22
print(f"我的名字是{name1},我今年{age1}岁")