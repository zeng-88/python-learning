"""
案例1：
根据输入的用户名密码执行登录操作，具体要求如下：
1.正确的用户名和密码为admin/666888、zhangsan/123456、taoge/888666
2.输入用户名和密码进行登录，直到登录成功，程序结束运行;如果登录失败，则继续输入用户名和密码进行登录
3.输入的用户名和密码不能为空！
4.登录成功：输出"登录成功，进入B站首页~"
5.登录失败：输出"用户名或密码错误,请重新输入!"

关键字：
    break : 只能出现在循环中，表示结束和跳出循环（break跳出循环时，while后面的else中的代码将不会执行）
    continue : 只能出现在循环中，表示中断本次循环，直接进入下一次循环
"""

# 思考：案例需要用到while循环，因为知道了循环结束的条件是“登录成功，程序结束运行”
# while True:
# 注意，此处因为没有指定循环的次数，所以用True来表示，如果条件一直为True，则一直进行循环;但是要求登录成功则结束循环，此时需要用到“break”来表示结束或跳出循环
    # 1、接收输入的用户名和密码：
    # username =input("请输入正确的用户名：")
    # password =input("请输入正确的密码：")
    # 2、校验：用户名或密码是否为空，若为空则重新输入
    # if username == "" or password == "":
    #     print("用户名和密码不能为空，请重新输入！")  #当提示“用户名和密码不能为空，请重新输入！”时，后面的if代码不再执行，重新进入下一次循环，用到“continue”
    #     continue  # 结束当前循环，直接进入下一轮循环
    # 3、判断输入的用户名和密码的正确性，执行登录操作
    # if username == "admin" and password == "666888":
    #     print("登录成功，进入B站首页~")
    #     break   # 跳出循环
    # elif username == "zhangsan" and password == "123456":
    #     print("登录成功，进入B站首页~")
    #     break  # 跳出循环
    # elif username == "taoge" and password == "888666":
    #     print("登录成功，进入B站首页~")
    #     break  # 跳出循环
    # else:
    #     print("用户名或密码错误,请重新输入!")


# 练习：用户名密码登录，正确的用户名和密码为admin / 666888 、zhangsan / 123456、taoge / 888666, 5次登录机会，输入错误五次，不允许再操作了。
# 方法1————while循环
# i = 0
# while i < 5:
#     username =input("请输入正确的用户名：")
#     password =input("请输入正确的密码：")
#     if username == "admin" and password == "666888":
#         print("登录成功，进入B站首页~")
#         break   # 跳出循环
#     elif username == "zhangsan" and password == "123456":
#         print("登录成功，进入B站首页~")
#         break  # 跳出循环
#     elif username == "taoge" and password == "888666":
#          print("登录成功，进入B站首页~")
#          break  # 跳出循环
#     else:
#         print("登录失败")
#         i += 1
# print("输入错误5次，不允许再登录！")

# 方法2————for循环（更简洁，不用手动管理计数器）
for i in range(5):
    username =input("请输入正确的用户名：")
    password =input("请输入正确的密码：")
    if username == "admin" and password == "666888":
        print("登录成功，进入B站首页~")
        break   # 跳出循环
    elif username == "zhangsan" and password == "123456":
        print("登录成功，进入B站首页~")
        break  # 跳出循环
    elif username == "taoge" and password == "888666":
         print("登录成功，进入B站首页~")
         break  # 跳出循环
    else:
        print("用户名或密码错误，登录失败")
else:
    print("输入错误5次，不允许再登录！")