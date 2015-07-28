# zhihu_rss

知乎rss开发

you can rss any zhihu's user in it

## 开发者预览版

![](http://img-storage.qiniudn.com/15-7-28/15352747.jpg)

### 为了图片小一点的渣画质的功能演示gif, 实际画质效果如上图


![](http://img-storage.qiniudn.com/15-7-28/94436942.jpg)

## 功能：
- [x] minibrower
- [x] 关注时可以选择导入动态数量，确定后弹出一个窗口
- [ ] 来显示爬虫进度
- [x] 删除关注者
- [x] 在用户名的右边, 显示未读数 ，未阅读，加粗标题，
- [x] 自定义关注方式：用户名上右键点击，然后弹出一个对话框，让用户打勾
- [ ] 后台更新功能

## 使用
目前在委托[7sDream](https://github.com/7sDream/)和[CodeFalling](https://github.com/CodeFalling)在win和linux下编译，过些时日能出安装包，敬请期待。


如果等不及想试用，在稳定版安装程序出来之前，请自行编译，以下是所需依赖，有任何问题可以开issue， 或者加qq群：478786205 来讨论。


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
