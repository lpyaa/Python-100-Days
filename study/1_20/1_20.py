#运算符
# f=float(input("请输入一个华氏温度："))
# a=(f-32)/1.8
# print("%.1f华氏度=%.1f摄氏度"%(f,a))
# print(f"{f:.1f}华氏度={a:.1f}摄氏度")

#计算圆的周长和面积
# import math
#
# r=float(input('请输入圆的半径： '))
# perimeter=2*math.pi*r
# area=math.pi*r*r
# print(f"半径为{r:.3f}圆的周长为{perimeter:.3f},面积为{area:.3f}")#先保留三位小数，然后转为字符串输出


# #判断闰年
# year=int(input("请输入年份： "))
# is_leap=((year%4==0 and year%100 !=0 ) or year%400==0)#闰年，能被四整除，但是不能被100整除的是闰年，或者能被400整除的是闰年
# print(f'{year}年{is_leap}闰年')#直接转为字符串输出

# #判断超没超重
# height=float(input("请输入身高："))
# weight=float(input("请输入体重(kg)： "))
# bmi=weight/(height/100)**1742
# print(f'bmi={bmi:.2f}')
# if 18.5<=bmi<24:
#     print("正常")
# elif bmi>24:
#     print('超重')
# else:
#     print('偏瘦')


#判断响应码
# status_code=int(input('请输入响应状态码: '))
# match status_code :
#     case 400:
#         description='bad request'
#     case 401:
#         description='unauthorized'
#     case 402:
#         description='payment required'
#     case 403:
#         description = 'Forbidden'
#     case 404:
#         description = 'Not Found'
#     case 405:
#         description = 'Method Not Allowed'
#     case 418:
#         description = 'I am a teapot'
#     case 429:
#         description = 'Too many requests'
#     case _:
#         description='unknown'
# print(f'{status_code}:{description}')



#todo 06循环结构

#明确知道循环执行次数，推荐用for-in循环
# import time
# for i in range(3600):#range(3600)--[0,3600)左闭右开
#     print("hello world")
#     time.sleep(1)

# #从1-100的整数求和
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)

#从1-100的偶数求和
# sum=0
# for i in range(2,101,2):
#     sum+=i
# print(sum)
#更简单
# print(sum(range(2,101,2)))


#while循环

# #1-100的整数求和
# sum=0
# i=1
# while i<=100:
#     sum+=i
#     i+=1
# print(sum)

#1-100的偶数求和
sum=0
i=2
while i<=100:
    sum+=i
    i+=2
print(sum)