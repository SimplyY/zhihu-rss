import QtQuick 2.0
import QtWebKit 3.0
import QtQuick.Controls 1.3
import QtQuick.Controls.Styles 1.3
import QtQuick.Layouts 1.0


ApplicationWindow {
    id: root
    width: 1155
    height: 700
    color: "#dedede"
    maximumWidth: 1500
    title: "zhihu rss "
    minimumWidth: 1100
    minimumHeight: 600
    maximumHeight: 1000

    signal sendClicked(string url)

    toolBar: ToolBar {
        id: navigationBar
        RowLayout {
            anchors.fill: parent
            spacing: 0


            Item { Layout.preferredWidth: 10 }
            ToolButton {
                objectName: "add_button"

                x:0
                y: 5
                width: 80
                height: 26
                text: qsTr("添加关注")
                z: 2
                style: ButtonStyle {
                    Text {
                        font.family: "Helvetica"
                        text: control.text
                    }
                }


            }
            Item { Layout.preferredWidth: 57 }

            ToolButton {
                id: updateButton
                objectName: "updateButton"
                width: 80
                text:  qsTr("更新动态")


                style: ButtonStyle {
                    Text {
                                font.family: "Helvetica"
                        text: control.text
                    }
                }
            }

            Item { Layout.preferredWidth: 80 }

            ToolButton {
                id: backButton
                tooltip: qsTr("Back")
                text: qsTr("后退")
//                iconSource: "images/left-32.png"
                onClicked: webView.goBack()
                enabled: webView.canGoBack
                Layout.preferredWidth: navigationBar.height
                style: ButtonStyle {
                    background: Rectangle { color: "transparent" }

                }
            }

            ToolButton {
                id: forwardButton
                tooltip: qsTr("Forward")
                text: qsTr("前进")
//                iconSource: "images/right-32.png"
                onClicked: webView.goForward()
                enabled: webView.canGoForward
                Layout.preferredWidth: navigationBar.height
                style: ButtonStyle {
                    background: Rectangle { color: "transparent" }

                }
            }

            ToolButton {
                id: reloadButton
                tooltip: webView.loading ? qsTr("Stop"): qsTr("Refresh")
                text: webView.loading ? qsTr("停止"): qsTr("刷新")

//                iconSource: webView.loading ? "images/stop-32.png" : "images/refresh-32.png"
                onClicked: webView.loading ? webView.stop() : webView.reload()
                Layout.preferredWidth: navigationBar.height
                style: ButtonStyle {
                    background: Rectangle { color: "transparent" }

                }
            }

            Item { Layout.preferredWidth: 15 }

            TextField {
                Layout.fillWidth: true
                id: urlField
                x: 370
                inputMethodHints: Qt.ImhUrlCharactersOnly | Qt.ImhPreferLowercase
                text: webView.url

                onAccepted: webView.url = text


                ProgressBar {
                    id: progressBar1
                    x: 1
                    anchors.bottom: parent.bottom
                    anchors.bottomMargin: -1
                    width: parent.width - 2
                    height: 2
                    visible: webView.loading
                    minimumValue: 0
                    maximumValue: 100

                    value: webView.loadProgress > 100 ? 0 : webView.loadProgress
                    style: ProgressBarStyle{

                        background: Rectangle{
                            border.width: 1;
                            border.color: "grey";
                            color:"lightgray";
                        }
                        progress: Rectangle{

                            color: "#2c6fe2"
                        }


                    }
                }
            }

            Item { Layout.preferredWidth: 15 }
            ToolButton {
                width: 120
                height: 26
                tooltip: qsTr("使用文档")
                text: qsTr("使用文档")
//                iconSource: "images/right-32.png"

                Layout.preferredWidth: 120
                style: ButtonStyle {
                    background: Rectangle { color: "transparent" }

                }
                onClicked: {
                    webView.url = "https://github.com/SimplyY/zhihu-rss"
                }
            }

            Item { Layout.preferredWidth: 10 }


        }
    }

    statusBar: StatusBar {
        id: statusBar
        visible: webView.loading && Qt.platform.os !== "ios"
        RowLayout {
            anchors.fill: parent
            Label { text: webView.loadProgress == 100 ? qsTr("Done") : qsTr("Loading: ") + webView.loadProgress + "%" }
        }
    }


    Rectangle {
        id: rectangle0
        border.width: 0

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom

        anchors.topMargin: 0




        Rectangle {
            id: rectangle1
            anchors.left: parent.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            width: 140

            color: "#ebebeb"
            anchors.bottomMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0
            antialiasing: true
            border.color: "#b0aeb0"
            border.width: 0
            objectName: "rect"

            function add_new_feedslist(args){
                var feeds_list = args["feeds_list"]

                var model = noticers1_model
                model.append({"name": feeds_list["name"], "feedslist": feeds_list})

                var feeds = feeds_list["feeds"]

                for(var i in feeds){
                    feeds_list_model.append({"action": feeds[i]["action"], "url": feeds[i]["url"], "is_read": feeds[i]["is_read"]})
                }
            }


            function updateNoticersList(args){
                noticers1_model.clear()

                var names = args["names"]
                var unread_nums = args["unread_nums"]
                var feedslists = args["feedslists"]

                for(var i = 0; i < names.length; i++){

                    noticers1_model.append({"name": names[i], "unread_num": unread_nums[i],"feedslist": feedslists[i]})
                }
                if(names.length != 0){
                    load_feeds_list(names[0])
                }else{
                    feeds_list_model.clear()
                }

            }

            function load_feeds_list(name){
                feeds_list_model.clear()
                var model = noticers1_model
                var feedslist = []

                for(var j = 0;j < model.count; j++){
                    if(model.get(j).name === name){
                        feedslist = model.get(j)["feedslist"]
                    }
                }
                var feeds = feedslist["feeds"]

                for(var index in feeds){
                    feeds_list_model.append({"name": feedslist["name"],"action": feeds[index]["action"],"url": feeds[index]["url"], "is_read": feeds[index]["is_read"]})
                }
            }


            ListModel {
                id: noticers1_model
                objectName: "noticers1_model"
            }
            Text{
                id: current_noticer_name
                x:2000
                width: 0
                height: 0
                objectName: "current_noticer_name"
            }

            ListView {
                id: listViewNoticers1
                x: 0

                objectName: "noticers_list"

                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom

                anchors.topMargin: 35
                anchors.rightMargin: 1
                anchors.leftMargin: 1
                layoutDirection: Qt.RightToLeft
                currentIndex: -1

                model: noticers1_model

                delegate: Component {
                    Item{
                        id: listItem1
                        anchors.leftMargin:20
                        anchors.left: parent.left
                        anchors.right: parent.right

                        height:24

                        Text{
                            objectName: "noticer_text"
                            width:60
                            height:24
                            text: name

                            font.pixelSize: 14
                            font.family: "Times New Roman"
                        }


                        MouseArea{
                            anchors.fill: parent
                            acceptedButtons: Qt.LeftButton | Qt.RightButton // 激活右键（别落下这个）
                            onClicked:{
                                listViewNoticers1.currentIndex = index
                                listViewFeeds.currentIndex = -1
                                current_noticer_name.text = noticers1_model.get(listViewNoticers1.currentIndex)["name"]
                                if (mouse.button == Qt.LeftButton){
                                    rectangle1.load_feeds_list(name)
                                }

                                 if (mouse.button == Qt.RightButton) {
                                    noticerMenu.popup()
                                }
                            }
                        }

                    }
                }

                highlight: Rectangle {
                    anchors.left: parent.left
                    anchors.right: parent.right
                    height: 20
                    color: '#d5d5d5'
                }
                focus: true
                //                onCurrentItemChanged:
            }


            Menu { // 右键菜单
                id: noticerMenu

                MenuItem {
                    objectName: "change_notice_method"
                    text:"更改关注方式"
                    onTriggered: {
                    }
                }
                MenuItem {
                    objectName: "delete_noticer"
                    text:"取消关注"

                }
            }


            Text {
                id: text1
                x: 10
                y: 12
                color: "#878787"
                text: qsTr("关注")
                font.bold: true
                font.family: "Helvetica"
                font.pixelSize: 16
                z:1
            }

        }

        Rectangle {
            id: rectangle2

            anchors.top: parent.top
            anchors.topMargin: -2
            anchors.left: rectangle1.right
            width: 250
            anchors.bottom: parent.bottom

            antialiasing: true

            Rectangle{
                anchors.left: rectangle2.left
                width: 1
                anchors.top: rectangle2.top
                anchors.bottom: rectangle2.bottom
                color:  "#dbdbdb"
                z:1
            }



            Rectangle{
                anchors.right: rectangle2.right
                anchors.rightMargin: 0
                width: 1
                anchors.top: rectangle2.top
                anchors.bottom: rectangle2.bottom
                color:  "#dbdbdb"
                z:1
            }

            Rectangle{
                anchors.right: rectangle2.right
                anchors.rightMargin: 5
                anchors.left: parent.left
                anchors.leftMargin: 1
                anchors.top: rectangle2.top
                height: 40
                color:  "#fafafa"
                z:1
            }
            Text {
                id: text2
                x: 5
                y: 13
                color: "#878787"
                text: qsTr("动态")
                font.bold: true
                font.family: "Helvetica"
                font.pixelSize: 16
                z:2
            }


            ListView {
                id: listViewFeeds
                x: 2

                anchors.top: text2.bottom
                anchors.bottom: parent.bottom
                anchors.bottomMargin: -13
                anchors.topMargin: 8
                width: rectangle2.width-14
                height: 593
                currentIndex: -1

                model: ListModel {
                    id: feeds_list_model

                }
                delegate: Component {
                    Item{
                        id: listItem1
                        x:0
                        width: 200
                        height:56
                        Rectangle{
                            anchors.top: parent.top

                            width: rectangle2.width
                            height: 1
                            border.color: "#efeff0"
                            border.width: 1
                        }

                        Text{
                            x:-3
                            color: is_read? "#9f9f9f":"#3b3b3b"
                            width:55
                            height:55
                            text: is_read?  action.replace('="4"', '="3"').replace("black", "grey").replace('="4"', '="3"').replace("black", "grey") :action
                            textFormat: Text.RichText
                            font.pixelSize: 11
                            font.family: "Times New Roman"
                        }
                        MouseArea{
                            anchors.fill: parent
                            onClicked:{
                                listViewFeeds.currentIndex = index
                                console.debug(index + is_read)

                                webView.url = url
                                feeds_list_model.get(index)["is_read"] = true

                                for(var i = 0; i < noticers1_model.count; i++){

                                    if(noticers1_model.get(i)["name"] == name){
                                        noticers1_model.get(i)["unread_num"]--
                                    }
                                }
                                root.sendClicked(url)
                            }
                        }
                    }
                }
                highlight: Rectangle {
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.rightMargin: -2

                    height: 20
                    color: '#ebebeb'
                }
                highlightFollowsCurrentItem : true
                highlightMoveDuration: 1
            }


            Rectangle{
                anchors.right: rectangle2.right
                anchors.rightMargin: 1
                width:8
                anchors.top: rectangle2.top
                anchors.bottom: rectangle2.bottom
                color: "#f5f5f5"
                z:1
            }


            ScrollBar{
                flk: listViewFeeds
                radius: 10
                color: "grey"
                expandedWidth: 5
                anchors.topMargin: -34
                anchors.rightMargin: -10
            }

        }



        WebView{
            id: webView

            anchors.rightMargin: 5
            anchors.bottomMargin: 0
            anchors.leftMargin: 0

            anchors.left: rectangle2.right
            anchors.top: parent.top
            anchors.topMargin: url.toString().match("www.zhihu.com")=="www.zhihu.com" ? -65 : 0
            anchors.right: parent.right
            anchors.bottom: parent.bottom



            objectName: "web_view"

            opacity: 1
            flickDeceleration: 1800
            z: 1
            scale: 1
            maximumFlickVelocity: 2000

        }
        Rectangle{
            anchors.right: parent.right
            anchors.rightMargin: -1
            width: 11
            anchors.top: webView.top
            color: "#f5f5f5"
            anchors.bottom: webView.bottom

            z:2
        }

        ScrollBar{
            flk: webView
            radius: 10
            color: "grey"
            expandedWidth: 5
            anchors.topMargin: webView.url.toString().match("www.zhihu.com")=="www.zhihu.com" ? 66 : 0
            anchors.right: parent.right
            anchors.rightMargin: 2
            z:3
        }


    }





}
