import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题
# 定义数据
labels = ['军用飞机系统', '综合作战管理系统等', '雷达、电子战/高级电子产品', '卫星和导弹系统']
sizes = [108, 59, 109, 139]  # 单位为亿美金
total_budget = sum(sizes)  # 计算总预算
sizes_percent = [size / total_budget * 100 for size in sizes]  # 计算每个部分的百分比

# 创建一个图形和一个轴
fig, ax = plt.subplots(figsize=(10, 8))

# 绘制饼图
wedges, texts, autotexts = ax.pie(sizes_percent, autopct='%1.1f%%', startangle=140,
                                  wedgeprops=dict(width=0.3, edgecolor='w'),
                                  textprops=dict(color="w"))

# 设置饼图的颜色
colors = ['#FFD700', '#90EE90', '#ADD8E6', '#FFB6C1']
for wedge, text, autotext in zip(wedges, texts, autotexts):
    wedge.set_facecolor(colors.pop(0))  # 为每个扇区设置颜色
    text.set_color('black')  # 设置标签颜色
    autotext.set_color('black')  # 设置百分比标签颜色

# 设置图例
ax.legend(labels, loc="upper right", bbox_to_anchor=(1.1, 1.05), title="项目类别")

# 设置标题和轴标签
ax.set_title('军事项目预算占比')
plt.axis('equal')  # 确保饼图是圆形的

# 显示图形
plt.show()