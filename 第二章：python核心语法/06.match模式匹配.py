# 结构模式匹配（match...case）：用一个清晰的模板去精准匹配数据的结构和内容，匹配成功则执行响应
# 案例：工作日程安排
# day = int(input("请输入星期几："))
# match day:
#     case 1:
#         print("周一：工作会议日")
#     case 2:
#         print("周二：学习培训日")
#     case 3:
#         print("周三：项目开发日")
#     case 4:
#         print("周四：代码审查日")
#     case 5:
#         print("周五：总结规划日")
#     case 6 | 7:
#         print("周末：休息放松")
#     case _:
#         print("输入有误！！")

# 案例：基于match...case实现一个简易计算器，可以实现+ - * /的运算，用户输入要运算的两个数和运算符，就可以进行运算
# 1、输入第一个数：
# num1 = float(input("请输入第一个数："))
# num2 = float(input("请输入第二个数："))
# oper = input("请输入运算符：")
# match oper:
#     case "+":
#         print(f"{num1} + {num2} = {num1 + num2}")
#     case "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     case "*":
#         print(f"{num1} * {num2} = {num1 * num2}")
#     case "/" if num2 != 0: # 除数不能为0，才能继续执行
#         print(f"{num1} / {num2} = {num1 / num2}")
#     case _:
#         print("操作不支持")

# 练习：编写一个游戏角色移动控制系统，根据玩家输入的不同指令，控制游戏角色执行相应操作（输出控制台）
instr = input("玩家请输入指令：")
match instr:
    case "上"|"W"|"w":
        print("角色向上移动")
    case "下" | "S" | "s":
        print("角色向下移动")
    case "左" | "A" | "a":
        print("角色向左移动")
    case "右" | "D" | "d":
        print("角色向右移动")
    case "跳" | " ":
        print("角色跳跃")
    case "攻击" | "J" | "j":
        print("角色发动攻击")
    case "退出" | "ESC" | "esc":
        print("角色退出游戏")
    case _:
        print("非法操作，不支持！！")