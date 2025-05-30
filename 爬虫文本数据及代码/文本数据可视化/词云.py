import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
from PIL import Image

# 读取文本文件
with open('B-21翻译.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 添加自定义词典（这里直接在代码中添加）
jieba.add_word('B-21')

# 读取停用词，并添加"表示"
stopwords = set()
with open('cn_stopwords.txt', 'r', encoding='utf-8') as file:
    for line in file:
        stopwords.add(line.strip())
stopwords.add('表示')
stopwords.add('没有')
stopwords.add('可能')
stopwords.add('我们')
stopwords.add('架飞机') # 直接在代码中添加"表示"到停用词

# 使用jieba进行中文分词
words = jieba.lcut(text)

# 过滤停用词
filtered_words = [word for word in words if word not in stopwords and len(word) > 1]

# 统计词频
word_counts = Counter(filtered_words)

# 打开背景图片
color_mask = np.array(Image.open('bg.png'))
# 生成词云
wordcloud = WordCloud(font_path='simhei.ttf',  # 指定字体路径，避免乱码
                      background_color='white',
                      width=800,
                      height=400,
                      mask=color_mask).generate_from_frequencies(word_counts)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()