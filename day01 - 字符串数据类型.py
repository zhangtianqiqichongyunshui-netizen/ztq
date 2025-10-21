#字符串类型即连续的字符序列，界定符为单引号，双引号，三引号
city = "天津"
address = "天津市东丽区津北公路2898号"
print(city,address)

#多行字符串
info = """姓名：张天骐
          地址：天津市东丽区津北公路2898号中国民航大学
          联系电话：15903099256"""
print(info)

#转义字符
print("天\n津\n欢\n迎\n您")

print("helloworld")
print("hello\tworld") #\t后退一个制表位，因为一个制表位占八个字符，除去前面的5个还剩三个字符

print("老师说：\'要认真学习\'")

print(r"天\n津\n欢\n迎\n您") # r是原字符，使转义字符失效

#字符串的常用操作
string = "HELLOWORLD"
print(string[0],string[-10])
print("hello"[1])
print(string[2:7])
print(string[2:])
print(string[:-2])

print("天津"+"上合峰会")
print("天津"*10)
print("hello" in string)
print("HELLO" in string)