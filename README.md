## 由于 homebrew 在 qt5.6里面把我依赖的 qtwebkit 移出了，天坑，然后自己也早已转 js 了，总之无力维护这个仓库，为了能不漏喜欢的作者的文章，我自己的解决办法是，将需要看的回答、专栏放到书签里面。。。




# zhihu-rss
知乎非官方客户端， **可以将知乎的任何 user 的动态做成 rss，只需几步操作**，并且可以**定制 rss 内容**（回答 or 提问 or 文章等等）,以 rss 的形式显示（二维表，知乎是一维的），欢迎 star。

(非官方的跨平台客户端， 目前只支持 linux 和 osx)

> 使用帮助看功能列表和演示部分

## 效果图
![image](https://cloud.githubusercontent.com/assets/8455579/8877985/1408786a-325b-11e5-8d2c-ecc35cf63ead.png)

## 重大提醒（放弃对 win 的支持，如果出 bug 请更新zhihu-py3爬虫库）
由于知乎频繁改版（前端），导致爬虫库无法稳定，对于 win 平台需要客户端经常升级。。

于是win 下放弃，，，（由于 win 还是静态链接库。。维护太麻烦了，需要每次都要非常麻烦的再打包一次，我又没有 win 的机器，麻烦别人也不好。）

osx 和 linux 平台编译源码的老版本，如果出现 bug，请
(sudo)pip3 install zhihu-py3 --upgrade
就 ok 了





## 功能：
最棒的功能是：**自定义关注方式**

以及 zhihurss 配合 pocket 用简直神器，特别是你用了 pocket 的alfred插件后

1. minibrowser
2. 自定义关注方式、删除关注者：用户名上右键
3. 添加关注
4. 后台更新功能，点击已读（标题颜色变淡就像 rss 一样）
5. （这个功能有点小问题，以前好的，现在又不行了，和知乎改版可能有关）支持对站外不可见用户的关注（http://www.zhihu.com/settings/profile 这里的隐私保护打了勾），支持设置代理。




## 功能演示
(为了图片小点，画质渣了，，实际上 retina 屏幕效果如上面的效果图，还是非常好滴)
![](http://img-storage.qiniudn.com/15-7-28/94436942.jpg)


## 特别提醒

1. 然后最好**不用zhihurss 爬大量数据**（上万条），不然会被封 ip，不过提供代理功能，见[设置登陆状态和代理](https://github.com/SimplyY/zhihu-rss#设置登陆状态和代理)，（如果就和我一样正常使用，一次也就爬个几百条，嫌麻烦就不用设置代理了，肯定不会封 ip）
2. 老用户，或者突然程序有问题，一般是你 rss 的人**改了个性域名**，解决方法见 [知乎的设置引起的bug](https://github.com/SimplyY/zhihu-rss#知乎的设置引起的bug)
3. 最好阅读一下 [知乎的设置引起的bug](https://github.com/SimplyY/zhihu-rss#知乎的设置引起的bug)




## zhihurss 推荐列表

https://github.com/SimplyY/zhihu-rss/blob/master/zhihurss%20list.md

## 安装

### Mac OS X
osx下同时安装了Python2和3的用户请使用pip3 install xxx代替（应该不用我说……）

1. 安装[`homebrew`](http://brew.sh/)
2. 安装pyqt5.5及其依赖(homebrew 在 qt5.6里面把我依赖的 qtwebkit 移出了，天坑，所以步骤多了)：
```
brew install python3 d-bus sip xz
brew install homebrew/versions/qt55
brew install --ignore-dependencies pyqt5
ln -s /usr/local/opt/qt55 /usr/local/opt/qt5
```
3. git clone https://github.com/SimplyY/zhihu-rss
4. cd zhihu-rss
5. pip install $(cat requirements.txt)
6. 在程序目录（clone 的目录）下开启终端，执行`python3 ./entry.py`  **或者** 在 finder 里双击`osx-launcher`运行程序



### linux

linux ，请自行编译，以下是所需依赖，有任何问题可以开issue， 或者加qq群：zhihu&github 交流群 478786205 来讨论。

#### 依赖：

本项目依赖于 zhihu-py3(requests ，BeautifulSoup4， html2text)， pyqt5， qt quick的各种东西比如qt webkit（装qt即可）

Linux下同时安装了Python2和3的用户请使用pip3 install xxx代替（应该不用我说……）

1. (sudo)pip3 install zhihu-py3 --upgrade
2. [qt](https://www.qt.io/zh-hans/download-open-source/)  在线安装的时候不需要安装安卓相关（安卓相关几个g...）
3. 安装pyqt5
4. git clone https://github.com/SimplyY/zhihu-rss
5. python3 zhihu-rss/entry.py



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
