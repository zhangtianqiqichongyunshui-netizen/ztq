s = '3.14+3'
print(s,type(s))
#eval函数可以去掉两边的引号，并执行去掉引号后的操作
s = eval(s)
print(s,type(s))

#eval函数经常和input函数配合使用，用来将接收的字符串型数值转换成int型数值
age = eval(input("输入你的年龄:"))
print(age,type(age))

hello = "天津欢迎你"
print(hello)
print(eval('hello'))