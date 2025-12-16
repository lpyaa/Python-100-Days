print(1.23456e2)#科学计数法
print(123.456)
print(2**3)#幂运算

a=10
b=2
a+=b#12
a*=a+2#12*14
print(a)#168

# SyntaxError: invalid syntax
# print((a = 10))

# `print(a = 10)`，会看到`TypeError: 'a' is an invalid keyword argument for print()`
#相当于a=10是int a=10,那print怎么可以打印这个呢，因为a压根就没有被定义过

print((a:=10))

