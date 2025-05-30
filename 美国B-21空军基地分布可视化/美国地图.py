from pyecharts.charts import Geo
from pyecharts.datasets import register_url
from pyecharts.options import VisualMapOpts, TitleOpts, InitOpts
from pyecharts import options as opts  # 导入 opts 模块
import pandas as pd
# 绘制美国地区销量分布图
def draw_usa_map1():
    try:
        register_url("https://echarts-maps.github.io/echarts-countries-js/")
    except Exception:
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
        register_url("https://echarts-maps.github.io/echarts-countries-js/")

    df21 = pd.read_excel('./states_coordinates.xlsx', sheet_name='Sheet1', header=0)
    states1 = df21['State'].tolist()  # pandas转list
    sales21 = df21['score'].tolist()
    list21 = [[states1[i], sales21[i]] for i in range(len(states1))]  # 合并两个list为一个list
    maxsales2 = max(sales21)  # 计算最大销量值，用作图例的上限

    geo = (
        Geo(init_opts=InitOpts(width="1200px", height="600px", bg_color='#EEEEE8'))
        .add_schema(maptype="美国", itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"))

        .add_coordinate('UT', -112.50, 41.20)

        .add_coordinate('SD', -102.52, 44.72)
        .add_coordinate('OK', -97.13, 35.42)
        .add_coordinate('TX', -99.80, 33.30)

        .add_coordinate('MO', -93.57, 38.48)

        .add_coordinate('GA', -83.22, 32.59)

        .add("B-21", list21, type_="scatter")
        .set_global_opts(
            title_opts=TitleOpts(title="xxxxxxxxxB-21空军基地分布图"),
            visualmap_opts=VisualMapOpts(max_=maxsales2),

        )
        .render("./B-21.html")
    )

    draw_usa_map1()
draw_usa_map1()