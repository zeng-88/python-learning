# 字面量的写法
# print(100)#整数(int)
# print(3.14)#浮点数/小数(float)
# print(True)#布尔(bool)
# print(False)#布尔(bool)
# print("hello world")#字符串(str)
# print(None)#空值(NoneType)
# # 布尔本质也是整数类型，在进行运算时，True - 1，False - 0
# print(True+1) #2
# print(False-1) #-1
# (如果后面不想运行一整段代码，可以把前面的代码标为注释)

# 变量--->python是动态类型语言，一个变量是可以存储不同类型的数据的（但是项目开发中，推荐变量只存储一种类型的数据）
# num = 1000.11
# print(num)
#
# num = num+1 #变量的赋值发生变化时，原来的num可以参与到运算当中
# print(num)
#
# num = "ok"
# print(num)
#
# num = True
# print(num)
#
#  # 如果需要存储其他类型数据的需求，那可以重新定义一个变量就行
# a = True
# print(a)

# 案例
# base = 20.7 #视频的基础播放量
# incr = 50 #每一个月的新增播放量
# print("未来第一个月的总播放量：",base + incr)
# print("未来第二个月的总播放量：",base + incr + incr)

# 案例 - 升级：一次性可以定义多个变量，连续赋值
# base,incr = 20.7,50
# print("未来第一个月的总播放量：",base + incr)
# print("未来第二个月的总播放量：",base + incr + incr)

# 变量值的交换
# 案例1：现有两个变量，a = 10, b = 20,将a,b两个变量的值交换，然后输出到控制台
# 方法1：增加一个新的变量
# a,b = 10,20
# c = a  # c = 10
# a = b  # a = 20
# b = c  # b = 10
# print(a,b)
# # 方法2：同时赋值
# a = 10
# b = 20
# a,b = b,a
# print(a,b)

# 案例2：现有3个变量，a=100,b=200,c=300,将这3个变量交换，将a,b,c的值分别赋值给c,a,b,并输出到控制台
# 方法1：新增一个变量temp
a = 100
b = 200
c = 300
temp = a # temp = 100
a = b # a = 200
b = c # b = 300
c = temp
print(a)
print(b)
print(c)

# 方法2：同时赋值
a = 100
b = 200
c = 300
a,b,c = b,c,a
print(a,b,c)
