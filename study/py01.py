# print("hello world")
# python严格控制缩进
# 字符串必须加单引号或者双引号
# print('hhhhh')
# print("jjjjj")
# num1=3
# print(type(num1))#查看变量类型



# bool型True False!!!!!!!!区分大小写
# True=1.False=0 通常用于判断
# 字符串包含多行内容时可以使用三引号
# name="""hhhh
# xixixi
# """
# print(name)


# 格式化输出
# 占位符
# %s 字符串（常用）  %d 整型
# name="bingbing"
# age=18
# print("my name is ",name)
# print("my age is ",age)
#
# print("my name is %s  my age is %d" %(name,age))

# %4d 整数  数字设置位数，不足前面补空白
# %05d 整数 不足前面补0
# a=123
# print("%6d" %a)
# print("%06d" %a)
# print("%16d" %a)

#out
#   123
# 000123
#              123



# %f 小数(浮点数）占位符  默认后六位小数，若本身超出，则会遵循四舍五入原则，只保留六位
#若要自定义，则要在前面加上点！！！！
b=1.2
# print("%f" %b)
# print("%.4f" %b)
# print("%.8f" %b)

# print("woshi %f jjjj %%" %b)#out: woshi 1.200000 jjjj %


# f格式化   f"{表达式}”
# name="bing bing"
# age=18
# print(f"my name is {name} ,my age is {age} years old")

#运算符
# 商一定是浮点数
# print(2/1)
# print(1+1)
# # //取整除，取商的整数部分，向下取整，另：若其中有浮点数，则结果也会用浮点数表示
# print(3//2)
# # %取余
# #**幂5**2=25
# print(5.0**2)

#input()输入函数
# prompt是提示，会在控制台中显示
# age=input("请输入你的年龄：")
# print(age)



#转义字符
#\t制表符（缩进符）\n换行符，将当前位置移到下一行开头
# \r回车表示将当前位置移到本行开头
print("age\tname\tgender")
print("hhh\nxxxx")
print("lllllll\rloooooo")