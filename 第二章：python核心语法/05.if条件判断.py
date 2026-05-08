# if条件判断
# 案例1：如果分数超过680，我就去清华读书
# score = float(input("请输入你的分数："))
# if score > 680:
#     print("欢迎来到清华读书")
# else :
#     print("抱歉，你的分数不能到清华读书")
from html.parser import interesting_normal

from fontTools.misc.cython import returns

# 案例2：完成B站登录功能的实现（正确账号和密码为：zengyun/66688）
# 1.提示用户输入账号和密码
# acc = (input("请输入您的账号："))
# pwd = (input("请输入您的密码："))
# # 2.判断账号和密码是否正确，都正确，则登录成功，进入B站首页
# if acc == "zengyun" and pwd == "66688":
#     print("登录成功，欢迎进入B站首页！")
# # 3.如果账号和密码有一个错误，则登录失败，提示错误信息
# else:
#     print("您的账号和密码输入有误，请重新输入")

# 案例3：根据用户输入的年份，判断这一年是闰年还是平年（非整百年份，能被4整除的年份是闰年，整百年份（如1900、2000）能被400整除的是闰年）
# year = int(input("请输入需要判定的年份："))
# 非整百年份，且能被4整除的年份是闰年；整百年份，能被400整除的年份也是闰年
# if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
#     print(f"{year}年为闰年")
# else:
#     print(f"{year}年为平年")

########################################################
# 练习1：根据用户输入的数字，判断该数字是奇数还是偶数
# num = int(input("请输入数字："))
# if num % 2 == 0:
#     print(f"{num}为偶数")
# else:
#     print(f"{num}为奇数")
# 练习2：根据用户输入的年龄，判断该用户是否已经成年（>=18则成年，否则，未成年）
# age = int(input("请输入您的年龄："))
# if age >= 18:
#     print("您已成年，欢迎进入大人的世界！")
# else:
#     print("很抱歉，您未成年")
# 练习3：根据用户输入的数字，判断该数字是正数还是负数（不用考虑0）
# num = int(input("请输入数字："))
# if num > 0:
#     print(f"{num}为正数")
# else:
#     print(f"{num}为负数")
# 练习4：根据用户输入的考试分数，判断该分数是否及格了（>=60即为及格）
# score = float(input("请输入您的分数："))
# if score >= 60:
#     print("恭喜！您的分数及格啦！")
# else:
#     print("很抱歉，您的分数未能及格")

##################################################
# if条件判断进阶：多个条件判断---> if...elif...else

# 案例1：根据用户输入的数字，判断该数字是正数还是负数，还是0？
# num = int(input("请输入数字："))
# if num > 0:
#      print(f"{num}为正数")
# elif num < 0:
#     print(f"{num}为负数")
# else:
#     print(f"{num}是0")

# 案例2：根据输入的用户名和密码进行系统登录
# username = input("请输入用户名：")
# password = input("请输入密码：")
# if username == "admin" and password == "666888":
#     print("登录成功1")
# elif username == "root" and password == "547327":
#     print("登录成功2")
# elif username == "zhangsan" and password == "123456":
#     print("登录成功3")
# else:
#     print("登录失败，用户名或密码错误")

################################################################
# 练习1：根据输入的考试成绩，判断成绩等级（ >=85为优秀；60-85为及格；否则为不及格）
# score = int(input("请输入成绩："))
# if score >= 85 :
#     print(f"您的成绩{score}分为优秀")
# elif score >= 60 :
#     print(f"您的成绩{score}分为及格")
# else:
#     print(f"您的成绩{score}分为不及格")

# 练习2：购物折扣计算，根据输入的购物车的商品总额，以及以下折扣规则，计算实付金额（规则：金额>=500，8折；300<=金额<500，9折；100<=金额<300，95折；金额<100，无折扣）
# total_price = float(input("请输入购物车的商品总额："))
# if total_price >= 500:
#     print(f"您的消费金额为:{total_price}元，打8折，实付金额为：{total_price*0.8}元")
# elif total_price >= 300:
#     print(f"您的消费金额为:{total_price}元，打9折，实付金额为：{total_price * 0.9}元")
# elif total_price >= 100:
#     print(f"您的消费金额为:{total_price}元，打95折，实付金额为：{total_price * 0.95}元")
# else:
#     print(f"您的消费金额为:{total_price}元，无折扣，请支付：{total_price}元")

"""
案例——if的嵌套：三角形类型的判断——根据输入的三个边的边长（正整数），判定是等边三角形、等腰三角形、普通三角形还是不能构成三角形
  1、构成三角形的条件：两边之和大于第三边
  2、三角形判定规则：
     三边相等：等边三角形
     两边相等：等腰三角形
     三边都不相等
"""

# 1、接收三角形的三个边长
# a = int(input("请输入第一个边的边长："))
# b = int(input("请输入第二个边的边长："))
# c = int(input("请输入第三个边的边长："))
#  2、判断三角形的类型
# if a+b>c and a+c>b and b+c>a:
#     if a == b and b == c:
#         print(f"{a} {b} {c}三个边长构成等边三角形")
#     elif a == b or b == c or a == c:
#         print(f"{a} {b} {c}三个边长构成等腰三角形")
#     else:
#         print(f"{a} {b} {c}三个边长构成普通三角形")
# else:
#     print(f"{a} {b} {c}三个边长不构成三角形！！！")

# 可以以断点调试的方式跟踪程序的执行过程，
# 点击想要跟踪的代码所在行的断点，然后点击调试，代码自动执行到断点所在行时会停下，等待输入指令才会继续执行，
# 然后点“步入F8”,则会继续执行下一行代码


# 练习：
# 北京市居民年度用电电费计算：根据输入的用电度数，计算电费
# 北京市居民电费采用阶梯电价计价方式，所谓阶梯电价是指按照用户消费的电量分段定价，用电价格随用电量增加呈阶梯状逐级递增的一种电价定价机制。
# - 阶梯电价规则：
#   1. 第一档：2880度以下，电费单价0.4883元/度
#   2. 第二档：2880-4800度，电费单价0.5383元/度
#   3. 第三档：4800度以上，电费单价0.7883元/度

# 1、输入用电度数：
usage_elec = int(input("请输入您的用电度数："))
# 2、定义阶梯电价和总电费：
first_max = 2880 # 第一档度数
second_max = 4800 # 第二档度数

first_price = 0.4883 #第一档单价
second_price = 0.5383 #第二档单价
third_price = 0.7883 #第三档单价

total_cost = 0.0 #总电费
# 3、判断所在档位：
if usage_elec <= first_max: #档位在第一档
    total_cost = first_price * usage_elec #档位在第一档时的总电费
elif usage_elec <= second_max: #档位在第二档
    first_cost = first_price * usage_elec #第一档部分的电费
    second_usage = second_max - first_max #第二档部分的度数
    second_cost = second_usage * second_price #第二档部分的电费
    total_cost = first_cost + second_cost #总电费
else:
    first_cost = first_price * usage_elec  # 第一档部分的电费
    second_usage = second_max - first_max  # 第二档部分的度数
    second_cost = second_usage * second_price  # 第二档部分的电费
    third_usage = usage_elec - second_usage  # 第三档部分的度数
    third_cost = third_usage * third_price # 第三档部分的电费
    total_cost = first_cost + second_cost + third_cost  # 总电费
print(f"{usage_elec}度的电费为：{total_cost}元")