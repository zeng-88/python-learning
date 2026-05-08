"""
案例2：猜数字游戏
    1、系统随机生成一个随机数 （使用 random 来生成一个随机数）
    2、用户根据提示猜数字，并将所猜数字输入系统
    3、如果猜错了，系统提示数字猜大了，还是猜小了，然后继续输入猜的数字
    4、如果猜对，系统自动退出，游戏结束
"""
# import random
# random_num = random.randint(1,100) #随机生成一个数字并将这个变量命名为random_num
# while True:
#     num = int(input("请输入一个数字："))
#     if num > random_num:
#         print("您输入的数字太大了！")
#     elif num < random_num:
#         print("您输入的数字太小了！")
#     else:
#         print("恭喜您，猜对了！")
#         break  #猜对后跳出循环
# print("随机生成的数字为：",random_num)



# 练习1：将1-1000之间（包含1000）所有5的倍数的数字累加起来
# total = 0
# for i in range(1,1001):
#     if i % 5 == 0:
#         total += i
# print("1-1000之间（含1000）所有5的倍数的数字之和为：",total)


# 练习2：统计字符串 "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd" 字符串中有多少个a和k。
total = 0
for i in "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd":
    if i == "a" or i == "k":
        total += 1
print("字符串中a和k出现的次数为：",total)