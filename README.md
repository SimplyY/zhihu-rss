# zhihu-rss

you can rss any zhihu's user in it
(非官方的跨平台客户端)


**可以将知乎的任何 user 的动态做成 rss，只需几步操作**，并且可以**定制 rss 内容**（回答 or 提问 or 文章等等）

(使用帮助看功能列表和演示部分)

## 效果图
![image](https://cloud.githubusercontent.com/assets/8455579/8877985/1408786a-325b-11e5-8d2c-ecc35cf63ead.png)



## 功能：
最棒的功能是：自定义关注方式

1. minibrowser
2. 自定义关注方式、删除关注者：用户名上右键
3. 添加关注
4. 后台更新功能，点击已读（标题颜色变淡就像 rss 一样）
5. 支持对站外不可见用户的关注（http://www.zhihu.com/settings/profile 这里的隐私保护打了勾），支持设置代理。



## 功能演示
(为了图片小点av画质了，，实际上 retina 屏幕效果如上面的效果图)
![](http://img-storage.qiniudn.com/15-7-28/94436942.jpg)


## 特别提醒

2. 然后最好**不用zhihurss 爬大量数据**（上万条），不然会被封 ip，不过提供代理功能，见[设置登陆状态和代理](https://github.com/SimplyY/zhihu-rss#设置登陆状态和代理)
3. 老用户，或者突然程序有问题，一般是你 rss 的人**改了个性域名**，解决方法见 [知乎的设置引起的bug](https://github.com/SimplyY/zhihu-rss#知乎的设置引起的bug)
4. 最好阅读一下 [知乎的设置引起的bug](https://github.com/SimplyY/zhihu-rss#知乎的设置引起的bug)




## zhihurss 推荐列表

https://github.com/SimplyY/zhihu-rss/blob/master/zhihurss%20list.md

## 使用
非常感谢 [7神](https://github.com/7sDream) 在 win 下的打包

### win 下压缩包：
百度云盘 http://pan.baidu.com/s/1o68BOqm
github releases https://github.com/SimplyY/zhihu-rss/releases

下载后,解压，双击 exe 即可运行。

### Mac OS X

1. 安装[`homebrew`](http://brew.sh/)
2. 安装pyqt5：`brew install pyqt5 --with-python3`
3. git clone https://github.com/SimplyY/zhihu-rss
4. pip install requirements.txt
5. 在程序目录（clone 的目录）下开启终端，执行`./entry.py` **或者** 在 finder 里双击`osx-launcher`运行程序

### linux

linux ，请自行编译，以下是所需依赖，有任何问题可以开issue， 或者加qq群：zhihu&github 交流群 478786205 来讨论。

#### 依赖：

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

### 设置登陆状态和代理：
在 config 文件夹里面的 config.json文件可以设置是否登录，代理设置（一个 str）

（ config.json example：`{"is_sign": true,"proxy": "http://127.0.0.1:10025"}`以及proxy那个一定别设置错了, 不然 network timeout）

### 知乎的设置引起的bug

（最新版已解决，但是其实是和知乎的制度有关的，最好看一看）


1. 由于**知乎竟然可以更改自己的个性网址**：
    - (这个页面 http://www.zhihu.com/settings/profile )，引起了这个紧急 bug（老用户注意：好多大v 都改了自己的。）
    - 解决办法是取消关注，然后重新关注（输入正确的 url）,以及 添加关注的默认的url 后几个字母 yuwei-80（也就是我的)，我作死的改成了 SimplyY（知乎规定一个月改不回来。。）大家也帮忙改一下。。
2. 隐私保护打了勾：
    - 还有一个是早就有了的，也是那个页面，对隐私保护打了勾，造成无法添加其关注，而且无法更新所有动态，
    - 解决方法见下面的特别提醒

## 感谢：

爬虫方面全部使用7sDream的[zhihu-py3](https://github.com/7sDream/zhihu-py3), 非常感谢
