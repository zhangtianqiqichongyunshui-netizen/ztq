#Input函数的格式 input("提示文字")

num = input("请输入你的名字:")
'input()函数会默认转成字符串类型，如果需要转成int型需要使用内置函数int()'
print("你的名字是："+num)
number = int(input("输入一个数字:"))
print("输入的数字是:",number)