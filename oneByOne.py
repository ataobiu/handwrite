# _*_ coding :utf-8 _*_
# @Time   : 2022/12/13 10:41
# @Author : ataobiu
# @File   : startWrite
# @Project: 川信纸手写模拟
# 免费字体库：https://www.fonts.net.cn/fonts-zh/tag-shouxie2-1.html
# A4纸长21cm，宽29.7cm（210mm×297mm）

from PIL import Image, ImageFont, ImageDraw

# print(img.format, img.size, img.mode) # 打印图片信息
# img = img.resize((2100, 2970)) # 像素意义上的宽和高

import json

with open("config.json", "r") as J:  # 加载配置文件json
    jsonArr = json.load(J)
    config = jsonArr["config"]
    fontStyle = config["fontStyle"] # 选择字体样式
    fontSize = config['fontSize']  # 文字大小 推荐 75
    pageLine = config['pageLine']  # 页面行数 推荐 15
    numLine = config['numLine']  # 每行字符数 推荐 23
    J.close()

font = ImageFont.truetype("./fout/" + fontStyle + ".TTF", fontSize)  # 加载字体，设置文字大小
with open(file='./src/test.txt', mode='r', encoding='utf-8') as fp:  # 加载文本内容
    txt = fp.read()
    fp.close()

len_text = len(txt)
page = 1
txt_flag = 0
while txt_flag < len_text:
    img = Image.open("./src/template.jpg")  # 打开背景图片
    draw = ImageDraw.Draw(img)  # 需要绘制的图片
    # 定义行数
    for y in range(pageLine):
        # 定义 每行字符数
        for x in range(numLine):
            if txt_flag >= len_text:
                break
            if txt[txt_flag] == '\n':
                txt_flag += 1
                break
            draw.text(xy=(220 + 55 * x,
                          370 + 120 * y),
                      text=txt[txt_flag],
                      font=font,
                      fill=(0, 0, 0))
            txt_flag += 1
        if txt_flag >= len_text:
            break
    img.save("./out/" + str(page) + ".png")
    img.show()
    page += 1
