# 获取键盘上输入的数据---> input(提示信息)
# name = input("请输入您的姓名：")
# age = input("请输入您的年龄：")
# print(f"您的姓名为：{name},年龄为：{age}")

# 案例：银行卡ATM取款
# 总金额
# total = 10000
# # 1、输入密码
# password = input("请输入您的银行卡密码：")
# print(f"密码正确，{password}")
# # 2、输入取款金额
# num = input("请输入您的取款金额：")
# # 3、计算余额并输出
# print(f"取款后银行卡余额为：{total-int(num)}") #由于num为字符串类型，而total为int型，两者不能直接运算，要将num转成int型

# 练习题--->根据用户输入的两个数字，计算两个数之和，并将其输出到控制台
# num1 = input("请输入数字1：")
# num2 = input("请输入数字2：")
# print(f"两者之和为：{int(num1)+int(num2)}")

# 答案：
num1 = int(input("请输入第一个数字: "))  #先将两个变量的类型转为int，然后再进行运算
num2 = int(input("请输入第二个数字: "))
print(f"{num1} + {num2} = {num1 + num2}")