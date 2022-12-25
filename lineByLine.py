# _*_ coding :utf-8 _*_
# @Time   : 2022/12/19 12:10
# @Author : ataobiu
# @File   : lineByLine
# @Project: 川信纸手写模拟
# 免费字体库：https://www.fonts.net.cn/fonts-zh/tag-shouxie2-1.html
# A4纸长21cm，宽29.7cm（210mm×297mm）

from PIL import Image, ImageFont, ImageDraw
import textwrap
import json


with open("config2.json", "r") as J:  # 加载配置文件json
    jsonArr = json.load(J)
    config = jsonArr["config"]
    fontStyle = config["fontStyle"] # 选择字体样式
    fontSize = config['fontSize']  # 文字大小 推荐 62
    pageWidth = config['pageWidth']  # 文本绘制宽度 推荐21
    pageLine = config['pageLine']  # 页面行数 推荐 15
    J.close()
font = ImageFont.truetype("./fout/" + fontStyle + ".TTF", fontSize)  # 加载字体，设置文字大小
with open(file='./src/test.txt', mode='r', encoding='utf-8') as fp:  # 加载文本内容
    txt = fp.read()
    fp.close()

width = pageWidth  # 设置文本绘制宽度
lines = textwrap.wrap(txt, width)
# print(lines)    # 效果

start_x = 220
start_y = 370

len_text = len(lines)
page = 1
rows = 0

while rows < len_text:
    img = Image.open("./src/template.jpg")  # 打开背景图片
    draw = ImageDraw.Draw(img)  # 需要绘制的图片
    for x in range(len_text):
        x = rows
        draw.text(xy=(start_x, start_y), text=lines[x], font=font, fill=(0, 0, 0))
        start_y += 120
        rows += 1
        if (rows % pageLine) == 0:
            start_y = 370
            break
        if x == len_text - 1:
            break

    img.show()
    img.save("./out2/" + str(page) + ".png")
    page += 1
