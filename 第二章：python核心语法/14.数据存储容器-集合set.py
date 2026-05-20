# set 的应用场景：存储一些唯一的、不会重复的数据，比如手机号、银行卡号、身份证号等
# 集合set的特点：是一种无序的、不可重复、可修改的数据容器
# 定义集合
s1 = {"a","b","r",11,21,3,3,4,4}
print(s1)  # 输出时，若集合中有重复的元素，会自动去除重复元素，且以无序的形式输出
print(type(s1))
# 定义空集合：
s2 = set()
s3 = {}
print(s2)
print(s3)
print(type(s3))  # s3的类型为字典，<class 'dict'>
"""
注意：空集合的定义不可使用{}，{}表示的是空的字典；由于集合是无序的，因此不支持索引访问
"""

# 集合的常见方法：

# add():添加元素到集合里
s = {11,4,3,5,7,9,35,77,800,101}
s.add(90)
print(s)

# remove():移除集合中的指定元素（指定元素不存在将报错）
s.remove(11)
print(s)

# pop():随机删除集合中的元素并返回
s.pop()
print(s)

# clear():清空集合
s.clear()
print(s)

# difference():求取两个集合的差集（包含在第一个集合但不包含在第二个集合的元素）
s1 = {"a","b","c","t","g","q"}
s2 = {"a","b","t","k","l"}
print(s1.difference(s2))  # 包含在s1中，不包含在s2中的元素,要注意s1和s2的顺序

# union():求取两个集合的并集
print(s1.union(s2))   # s1、s2放在哪个位置，输出都一样
print(s2.union(s1))

# intersection():求取两个集合的交集
print(s1.intersection(s2))  # s1、s2放在哪个位置，输出都一样
print(s2.intersection(s1))


# 案例1：根据提供的班级学生的选课情况，完成如下需求
# 选修足球学生名单：
football_set = {"王琳","王小雨","曾韵","吴嘉里","王立新","马小玲","吴青峰","李逵","张三"}
# 选修篮球学生名单:
basketball_set = {"王小雨","曾韵","马小玲","王立新","李红","张无忌","王小利"}
# 选修法语学生名单:
french_set = {"马小玲","王立新","曾韵","吴嘉里","王立新","吴青峰","刘洪","刘丽","韩信","张无忌","王力宏"}
# 选修艺术学生名单:
art_set = {"吴青峰","曾韵","吴嘉里","张三","李红","王立新","兰溪","吴丽丽","乌拉拉","李莉莉","李白"}

# 1.找出同时选修法语和艺术的学生
# 方式一: 调用intersection()求交集
fa_set = french_set.intersection(art_set)
print(f"同时选修法语和艺术的学生为:{fa_set}")

# 方式二: 使用 "&" 运算符求交集
fa_set2 = french_set & art_set
print(f"同时选修法语和艺术的学生为:{fa_set2}")

# 2.找出同时选修了四门课的学生
all_set = football_set & basketball_set & french_set & art_set
print(f"同时选修了四门课的学生为:{all_set}")

# 3.找出选修了足球但没有选修篮球的学生
# 方式一: 调用difference()求差集
fb_set = football_set.difference(basketball_set)
print(f"选修了足球但没有选修篮球的学生为:{fb_set}")

# 方式二: 使用 "-" 运算符求差集   (最简便)
fb_set2 = football_set - basketball_set
print(f"选修了足球但没有选修篮球的学生为:{fb_set2}")

# 方式三: 使用集合推导式 ---> {要往集合中添加的数据 for s in set if 条件}
fb_set3 = {s for s in football_set if s not in basketball_set}
print(f"选修了足球但没有选修篮球的学生为:{fb_set3}")

# 4.统计每个学生选修的课程数量
# 4.1 获取学生名单 ---> 并集,可使用"|"运算符
all_set = football_set | basketball_set | french_set | art_set
# 解题思路: 要获取每个学生的选课数量,也就是学生的名字出现在所有课程中的次数,到all_set这一步,只是拿到了学生名单,并不知道学生的名字出现了多少次,要允许存在重复元素,可定义一个list来存储
# 4.2 获取每个学生选修的课程数量
all_list = [*football_set,*basketball_set,*french_set,*art_set]  # 对每个集合进行扩展解包,放到一个新列表中
for i in all_set:
    print(f"'{i}'选修了 {all_list.count(i)} 门课")