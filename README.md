# zhihu-rss

知乎rss开发

you can rss any zhihu's user in it

(使用帮助看功能列表和演示部分)

![image](https://cloud.githubusercontent.com/assets/8455579/8877985/1408786a-325b-11e5-8d2c-ecc35cf63ead.png)


## 紧急bug
1. 由于知乎竟然可以更改自己的个性网址(这个页面http://www.zhihu.com/settings/profile)，引起了这个紧急 bug（好多大v 都改了自己的，，），解决办法是取消关注，然后重新关注（输入正确的 url）,以及 添加关注的默认的url 后几个字母 yuwei-80（也就是我的)，我作死的改成了 SimplyY（知乎规定一个月改不回来。。）大家也帮忙改一下。。
2. 还有一个是早就有了的，也是那个页面，对隐私保护打了勾，造成无法添加其关注，而且无法更新所有动态，解决方法见下面的特别提醒

## 功能：
最棒的功能是：自定义关注方式

1. minibrowser
2. 自定义关注方式、删除关注者：用户名上右键
3. 关注时可以选择导入动态的数量，并显示爬虫进度
4. 后台更新功能
5. 在 config 文件夹里面的 config.json文件可以设置是否登录，代理设置（一个 str）
（ config.json example：{"is_sign": true,"proxy": "http://127.0.0.1:10025"}以及proxy那个一定别设置错了）

## 功能演示

![](http://img-storage.qiniudn.com/15-7-28/94436942.jpg)

## 特别提醒
有些用户无法关注，会程序崩掉。所以需要用功能5.
然后最好不用zhihurss 爬大量数据（上万条），不然会被封 ip，不过提供代理功能，见功能5

## zhihurss 推荐列表

https://github.com/SimplyY/zhihu-rss/blob/master/zhihurss%20list.md

## 使用
非常感谢 [7神](https://github.com/7sDream) 在 win 下的打包

### win 下压缩包：
百度云盘 http://pan.baidu.com/s/1dDe0eUd
github releases https://github.com/SimplyY/zhihu-rss/releases/tag/v1.0


### Mac OS X

- 安装[`homebrew`](http://brew.sh/)

- 安装pyqt5：`brew install pyqt5 --with-python3`

- 在程序目录下开启终端，执行`./entry.py` **或者** 双击`osx-launcher`运行程序

### linux

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
