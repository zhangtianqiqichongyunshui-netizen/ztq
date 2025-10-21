age = 23
name = "张天骐"
print(type(name))
print(name+"的年龄是:",age)

#在python中可以通过给变量赋不同的值，来动态的改变变量的数据类型
name = 145
print(type(name))

#在python中允许多个变量赋同一值
number= sum = 145
print(id(number))
print(id(sum))

#在python中，大写的变量名表示常量
PI = 3.1415926535