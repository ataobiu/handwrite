# *川信纸手写模拟*

<img src="https://i.328888.xyz/2022/12/25/DXWpU.png">

### *目录：*

- **src**：在**test.txt**里添加文本
- **fout**：存放你的字体文件
- **out**：运行**oneByOne.exe**后输出图片的存放路径
- **out2**：运行**lineByLine.exe**后输出图片的存放路径

### *oneByOne.py*

oneByOne：顾名思义，将文本字符，一个接一个打印输出

修改**config.json**获得你想要的效果

- ​    **fontStyle**：选择字体样式 [免费字体库](https://www.fonts.net.cn/fonts-zh/tag-shouxie2-1.html)
- ​    **fontSize**：  文字大小 推荐 75
- ​    **pageLine**：页面行数 推荐 15
- ​    **numLine**":  每行字符数 推荐 23

### *lineByLine.py*

lineByLine：将文本字符按照绘制宽度进行切割，一行接一行打印输出

修改**config2.json**获得你想要的效果

- ​	**fontStyle**：选择字体样式 [免费字体库](https://www.fonts.net.cn/fonts-zh/tag-shouxie2-1.html)
- ​    **fontSize**：文字大小 推荐 62
- ​    **pageWidth**：文本绘制宽度 推荐21
- ​    **pageLine**：页面行数 推荐 15
