import pandas as pd
import matplotlib.pyplot as plt
# 创建DataFrame
data = {
    'Quarter': ['2020Q1', '2020Q2', '2020Q3', '2020Q4', '2021Q1', '2021Q2', '2021Q3', '2021Q4',
                '2022Q1', '2022Q2', '2022Q3', '2022Q4', '2023Q1', '2023Q2', '2023Q3', '2023Q4',
                '2024Q1', '2024Q2'],
    'Sales': [86, 89, 91, 102, 92, 92, 87, 86, 88, 88, 90, 100, 93, 96, 98, 106, 101, 102],
    'EPS': [5.15, 6.01, 5.89, 6.59, 6.57, 6.42, 6.63, 11.14, 6.86, 6.06, 5.89, 7.50, 5.50, 5.34, 6.18, 13.53, 6.32,
            6.36]
}
df = pd.DataFrame(data)
# 转换季度为日期时间格式（可选，用于美化x轴）
df['Quarter'] = pd.to_datetime(df['Quarter'] + '-01', format='%YQ%m-%d')
# 创建一个图形和一个轴
fig, ax1 = plt.subplots(figsize=(10, 6))
# 绘制销售额折线图（主要y轴）
color = 'tab:red'
ax1.set_xlabel('Quarter')
ax1.set_ylabel('Sales', color=color)
ax1.plot(df['Quarter'], df['Sales'], color=color, marker='o', linestyle='-', label='Sales')
ax1.tick_params(axis='y', labelcolor=color)
ax1.legend(loc='upper left')
# 创建第二个y轴来绘制每股收益
ax2 = ax1.twinx()  # 共享x轴
color = 'tab:blue'
ax2.set_ylabel('EPS', color=color)  # 我们也修改了y2轴的颜色
ax2.plot(df['Quarter'], df['EPS'], color=color, marker='s', linestyle='--', label='EPS')
ax2.tick_params(axis='y', labelcolor=color)
ax2.legend(loc='upper right')
# 设置标题
fig.suptitle('Sales and EPS Over Time')
# 显示网格
plt.grid(True)
# 显示图形
plt.show()