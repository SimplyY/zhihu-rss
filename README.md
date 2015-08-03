# zhihu-rss

知乎rss开发

you can rss any zhihu's user in it

## 功能演示

![](http://img-storage.qiniudn.com/15-7-28/94436942.jpg)

## 功能：
最棒的功能是：第三个

1. minibrowser
2. 在用户名的右边, 显示未读数 ，未阅读显示为加粗的标题。
3. 自定义关注方式：用户名上右键点击，然后弹出一个对话框，让用户打勾
4. 关注时可以选择导入动态数量，确定后弹出一个窗口，来显示爬虫进度
5. 右键删除关注者
6. 后台更新功能

## 关于字体
推荐去下载'Helvetica Neue',Helvetica ，还有 Times New Roman

## zhihurss 推荐列表

https://github.com/SimplyY/zhihu-rss/blob/master/zhihurss%20list.md

## 使用
非常感谢 [7神](https://github.com/7sDream) 在 win 下的打包

win 下压缩包：
百度云盘 http://pan.baidu.com/s/1dDe0eUd
github releases https://github.com/SimplyY/zhihu-rss/releases/tag/v1.0


linux ，请自行编译，以下是所需依赖，有任何问题可以开issue， 或者加qq群：zhihu&github 交流群 478786205 来讨论。


## 依赖：


本项目依赖于 zhihu，requests ，BeautifulSoup4， html2text， pyqt5， qt quick的各种东西比如qt webkit（装qt即可？）

1. zhihu 前往 [zhihu-py3](https://github.com/7sDream/zhihu-py3)
2.  requests 、BeautifulSoup4、html2text 使用前请先安装
3. [qt](https://www.qt.io/zh-hans/download-open-source/)  在线安装的时候不需要安装安卓相关（安卓相关几个g...）

> html2text 只在导出为 markdown 格式功能被使用时才会被 import，如果没有此模块其他功能也能正常完成。

```
pip install requests
pip install beautifulsoup4
pip install html2text
```
Linux下同时安装了Python2和3的用户请使用pip3 install xxx代替（应该不用我说……）


## 感谢：

爬虫方面全部使用7sDream的[zhihu-py3](https://github.com/7sDream/zhihu-py3), 非常感谢
