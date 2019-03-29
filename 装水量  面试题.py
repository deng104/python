# 思路：
# 宽度为n的台阶列表表示step_array = [a0,a1,a2,a3,...a(n-2),a(n-1)]
# 宽度为n(n>=3)的台阶能装水的条件:
#                           中间的任意一个台阶都不能高于两头较低的那一个
#                           [a1,a2,...,a(n-2)]中的最大值 < min(a0,a(n-1))
# 求解装水的容量：
#               除了两头之外的正方形体积-除了两头之外的太台阶总和
#               (n-2)*min(a0,a(n-1))-sum([a1,a2,...,a(n-2)])

# 方案一
# step_array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# 假设切片台阶的宽度为n
# total_volumn = 0
# for n in range(3, step_len + 1):
#     # 从step_array中切出宽度为n的台阶列表 索引的开始位置到step_len-n
#     for i in range(step_len - n + 1):
#         son_array = step_array[i:i + n]
#         print(son_array)
#         # son_array就是切片切出来的从宽度为3的[0, 1, 0]一直到宽度为n的[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#         # 求解son_array的盛水量 son_array的宽度是n
#         # 1, 能盛水的条件是中间的任意一个台阶都不能高于两头较低的那一个
#         if max(son_array[1:n-1]) < min(son_array[0],son_array[n-1]):
#             # 求解盛水量 除了两头之外的正方形体积-除了两头之外的台阶总和
#             son_volumn = (n-2)*min(son_array[0],son_array[n-1])-sum(son_array[1:n-1])
#             print(son_volumn)
#             total_volumn += son_volumn
# print(total_volumn)
# 但是这里有个坑 n=3 n=5重复计算了一次
# 思路重新调整
# 切片台阶的宽度从最宽的n 递减的且到3
# 只要能找到满足盛水的条件 的切片台阶 求出盛水量之后立马从列表中剔除，这样做不会影响水量，有可以防止下一次重复计算
# 假设切片台阶的宽度为n
# step_array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# step_len = len(step_array)
# total_volumn = 0
# for n in range(step_len + 1, 2,-1):
#     # 从step_array中切出宽度为n的台阶列表 索引的开始位置到step_len-n
#     for i in range(step_len - n + 1):
#         son_array = step_array[i:i + n]
#         print(son_array)
#         # son_array就是切片切出来的从宽度为3的[0, 1, 0]一直到宽度为n的[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#         # 求解son_array的盛水量 son_array的宽度是n
#         # 1, 能盛水的条件是中间的任意一个台阶都不能高于两头较低的那一个
#         if max(son_array[1:n-1]) < min(son_array[0],son_array[n-1]):
#             # 求解盛水量 除了两头之外的正方形体积-除了两头之外的台阶总和
#             son_volumn = (n-2)*min(son_array[0],son_array[n-1])-sum(son_array[1:n-1])
#             print(son_volumn)
#             # son_array满足盛水的条件计算水水量之后从列表中剔除防止，后续重复计算
#             # for j in range(i+1,i+n):
#             #     step_array.pop(j)
#             # print("这是剔除之后的原台阶"+str(step_array))
#             total_volumn += son_volumn
# print(total_volumn)


# 方案二
# 但是这里面有由一个坑 对列表进行循环的时候 不要改变列表长度
import numpy as np
import matplotlib.pyplot as plt
# step_array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
step_array = [1,0,1,11,2,1,2,]


def step_sum_volum(step_array):
    """
    这是一个计算给定台阶列表后 计算台阶盛水量的函数
    :param step_array: 台阶高度列表作为函数的输入
    :return: 输出盛水量
    """
    volumn_list = []
    for n in range(len(step_array) + 1, 2,-1):
        # 从step_array中切出宽度为n的台阶列表 索引的开始位置到step_len-n
        for i in range(len(step_array) - n + 1):
            son_array = step_array[i:i + n]
            print(son_array)
            # son_array就是切片切出来的从宽度为3的[0, 1, 0]一直到宽度为n的[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
            # 求解son_array的盛水量 son_array的宽度是n
            # 1, 能盛水的条件是中间的任意一个台阶都不能高于两头较低的那一个
            height = min(son_array[0], son_array[n - 1])
            if max(son_array[1:n-1]) < height:
                # 求解盛水量 除了两头之外的正方形体积-除了两头之外的台阶总和
                son_volumn = (n-2)*min(son_array[0],son_array[n-1])-sum(son_array[1:n-1])
                # son_array满足盛水的条件计算水水量之后，将除了两头之外的台阶全部填充，防止下次计算重复计算水量
                step_array = step_array[0:i+1]+[height for i in range(n-2)]+step_array[i+n-1:]
                volumn_list.append(son_volumn)
    return volumn_list

ret_list = step_sum_volum(step_array)


# 计算结果的可视化
# 设置横轴标签
plt.xlabel('position')
# 设置纵轴标签
plt.ylabel('height')
# 添加纵横轴的刻度
plt.xticks(np.arange(0, len(step_array), 1))
plt.yticks(np.arange(0, 80, 1))
# 设置标题
plt.title("total:"+str(sum(ret_list)))
plt.bar(x=range(len(step_array)),height=step_array,width=1,align="edge",)
plt.show()

print("盛水量是："+str(sum(ret_list)))


