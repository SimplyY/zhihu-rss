# zhihu_rss

知乎rss开发

you can rss any zhihu's user in it

开发者预览版
![image](https://cloud.githubusercontent.com/assets/8455579/8877985/1408786a-325b-11e5-8d2c-ecc35cf63ead.png)

![image](https://cloud.githubusercontent.com/assets/8455579/8877987/1703d6d6-325b-11e5-9348-61bd28fc5db4.png)

## 功能：
- [x] minibrower
- [ ] 关注回答、文章，显示单个关注者的所有最近回答、文章。
- [ ] 关注动态，显示单个关注者的所有最近所有动态。

## 使用
目前在委托[7sDream](https://github.com/7sDream/)和[CodeFalling](https://github.com/CodeFalling)在win和linux下编译，过些时日能出安装包，敬请期待。


如果等不及想试用，在稳定版安装程序出来之前，请自行编译，以下是所需依赖，有任何问题可以开issue， 或者加qq群：478786205 来讨论。


## 依赖：


本项目依赖于 zhihu，requests ，BeautifulSoup4， html2text， pyqt5， qt quick的各种东西比如qt webkit（装qt即可？）

1. zhihu 前往 [zhihu-py3](https://github.com/7sDream/zhihu-py3)
2.  requests 、BeautifulSoup4、html2text 使用前请先安装
3. [https://www.qt.io/zh-hans/download-open-source/](qt)  在线安装的时候不需要安装安卓相关（安卓相关几个g...）

> html2text 只在导出为 markdown 格式功能被使用时才会被 import，如果没有此模块其他功能也能正常完成。

```
pip install requests
pip install beautifulsoup4
pip install html2text
```
Linux下同时安装了Python2和3的用户请使用pip3 install xxx代替（应该不用我说……）


## 感谢：

爬虫方面全部使用7sDream的[zhihu-py3](https://github.com/7sDream/zhihu-py3), 非常感谢
