#运算符
# f=float(input("请输入一个华氏温度："))
# a=(f-32)/1.8
# print("%.1f华氏度=%.1f摄氏度"%(f,a))
# print(f"{f:.1f}华氏度={a:.1f}摄氏度")
import random

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
# sum=0
# i=2
# while i<=100:
#     sum+=i
#     i+=2
# print(sum)


#todo 08常用数据结构之列表
#将一颗色子投掷6000次，统计每种点数出现的次数
#传统写法
# count1=0
# count2=0
# count3=0
# count4=0
# count5=0
# count6=0
#
# for i in range(1,6001):
#     face =random.randrange(1,7)#从指定范围内返回一个随机整数
#     if face==1:
#         count1+=1
#     elif face==2:
#         count2+=1
#     elif face==3:
#         count3+=1
#     elif face==4:
#         count4+=1
#     elif face==5:
#         count5+=1
#     elif face==6:
#         count6+=1
#
# print(f'1点出现了{count1}次')
# print(f'2点出现了{count2}次')
# print(f'3点出现了{count3}次')
# print(f'4点出现了{count4}次')
# print(f'5点出现了{count5}次')
# print(f'6点出现了{count6}次')
#

#使用列表
#
# item1 = ['python','101','hahah']
# print(item1)#['python', '101', 'hahah']
# print(type(item1))#<class 'list'>
#
#
# #python内置的list函数将其他序列变成列表
#
# item=list(range(1,10))
# # print(item)
# # print(type(item))
# # print(type(range(1,10)))
#
#
# item2=['hello','xixi']
# item1+=item2
# print(item1)#实现列表的合并
# print(item1*2)#实现列表的重复运算
#
# # #用in 或者not in判断元素是否在列表中
# # print('xixi' in item1)#True
# # print('hhhhhhh'in item1)#False
# # print ('hhhhhhhhh' not in item1)#True
#
# #[]的元素位置可以是从0-N-1的整数，也可以是-1到-N的整数，分别称为正向索引和反向索引
# print(item1[0])
# print(item1[-5])
# #[start:end:stride]
# print(item1[0:5:2])
#
# print(item1[-2:-6:1])#如果是反向索引，那么就要全都表示为反向索引，不要掺杂着
#
# print(item1[:5:2])#start=0,end=N.stride=1,这些值都可以省略
#
# item1[1:3]=['x','o']
# print(item1)

#遍历元素
languages = ['Python', 'Java', 'C++', 'Kotlin']

#通过索引运算，遍历列表元素
for index in range(len(languages)):
    print(languages[index])


#直接对列表做循环，循环变量就是列表元素的代表
for language in languages:
    print(language)