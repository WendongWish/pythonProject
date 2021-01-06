import sys
import jieba.analyse
import jieba.posseg as psg
from importlib import reload
import os
from wordcloud import WordCloud
import jieba
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import csv

reload(sys)

# 1.生成CSV文件
# ☆☆☆☆☆--此处填写分词后生成excel的文件名--☆☆☆☆☆
f = open('option.csv', 'w', newline='')  # 生成词频文件
chara_word = open('chara_option.csv', 'w', newline='')  # 生成词性文件
csv_writer = csv.writer(f)
csv_chara_word = csv.writer(chara_word)


# 2.对文本进行操作部分
# ☆☆☆☆☆--此处填写需要分词的文件名--☆☆☆☆☆
# 如样例给出的文件名为 tianKongCaiLiao.txt ,可修改为想要分词的文件名，注意要在 '' 内输入
comment_text = open('gapFillingOption.txt', 'r', encoding='utf-8').read()
# 正常值 用于生成词云图
cut_text = " ".join(jieba.cut(comment_text))

# 词性标注部分
seg = psg.cut(comment_text)
for word in seg:
    csv_chara_word.writerow(word)  # 写入excel词性
# 带权值 用于输出词频
tags = jieba.analyse.extract_tags(comment_text, topK=1000, withWeight=True)
# 打印文本，包括写入csv
for word, flag in tags:
    csv_writer.writerow([word, flag])  # 写入excel词频
    # print('%s %s' % (word, flag))  # 打印词频


# 3.生成云图部分
# 生成背景图
current_dir = os.path.dirname(__file__)
mask_img = os.path.join(current_dir, 'wordCloudBG.jpg')
color_mask = np.array(Image.open(mask_img))
cloud = WordCloud(
    # 设置背景色
    background_color='white',
    # 词云形状
    mask=color_mask,
    # 允许最大词汇
    max_words=2000,
    # 设置字体，不设置可能出现乱码
    font_path="msyhbd.ttf",
    # 最大号字体
    max_font_size=100,
)
# 产生词云
word_cloud = cloud.generate(cut_text)
# 保存图片 :表示保存的云图存放时的文件名
word_cloud.to_file('back.jpg')
# 显示词云图片
# plt.imshow(word_cloud)
plt.show()
# 关闭流
f.close()
