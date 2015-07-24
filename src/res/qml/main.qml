import QtQuick 2.0
import QtWebKit 3.0
import QtQuick.Controls 1.3
import QtQuick.Controls.Styles 1.3
import QtQuick.Layouts 1.0


ApplicationWindow {
    id: applicationWindow
    width: 1100
    height: 660
    color: "#dedede"
    maximumWidth: 1500
    title: "zhihu-rss"
    minimumWidth: 800
    minimumHeight: 600
    maximumHeight: 1000

    toolBar: ToolBar {
        id: navigationBar
        RowLayout {
            anchors.fill: parent
            spacing: 0


            Item { Layout.preferredWidth: 2 }
            ToolButton {
                objectName: "add_button"

                x: 470
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

            Item { Layout.preferredWidth: 102 }
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

            Item { Layout.preferredWidth: 75 }

            TextField {
                Layout.fillWidth: true
                id: urlField
                x: 370
                inputMethodHints: Qt.ImhUrlCharactersOnly | Qt.ImhPreferLowercase
                text: webView.url

                onAccepted: webView.url = text

                ProgressBar {
                    x: 3
                    y: 18
                    width: parent.width
                    height: 20
//                    color:
                    visible: webView.loading && Qt.platform.os !== "ios"
                    minimumValue: 0
                    maximumValue: 100
                    value: webView.loadProgress > 100 ? 0 : webView.loadProgress
                }
            }

            Item { Layout.preferredWidth: 25 }




            Item { Layout.preferredWidth: 8 }
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

            color: "#f6f6f6"
            anchors.bottomMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 1
            antialiasing: true
            border.color: "#b0aeb0"
            border.width: 0
            objectName: "rect"

            function add_new_feedslist(args){
                var feeds_list = args["feeds_list"]
                var notice_method = args["notice_method"]

                var model = notice_method===1 ? noticers1_model: noticers2_model
                console.debug(feeds_list["name"])
                model.append({"name": feeds_list["name"], "feedslist": feeds_list})

                var feeds = feeds_list["feeds"]

                for(var i in feeds){
                    console.debug(feeds)
                    feeds_list_model.append({"name": feeds[i]["action"], "url": feeds[i]["url"]})
                }
            }


            function updateNoticers1List(args){
                noticers1_model.clear()

                var names = args["names"]
                var feedslists = args["feedslists"]

                for(var i = 0; i < names.length; i++){
                    noticers1_model.append({"name": names[i], "feedslist": feedslists[i]})
                }
                noticers1_model.append({"length": names.length})
            }

            function updateNoticers2List(args){
                noticers2_model.clear()

                var names = args["names"]
                var feedslists = args["feedslists"]

                for(var i = 0; i < names.length; i++){
                    noticers2_model.append({"name": names[i], "feedslist": feedslists[i]})
                }

            }

            function load_feeds_list(name, i){
                feeds_list_model.clear()
                var model = i===1 ? noticers1_model: noticers2_model
                var feedslist = []


                for(var j = 0;j < model.count; j++){
                    if(model.get(j).name === name){
                        feedslist = model.get(j)["feedslist"]
                        console.debug("test" + feedslist["feeds"][0]["action"])
                    }
                }
                var feeds = feedslist["feeds"]
                for(var index in feeds){
                    feeds_list_model.append({"name": feeds[index]["action"], "url": feeds[index]["url"]})
                }
            }


            ListModel {
                id: noticers1_model
                objectName: "noticers1_model"
            }

            ListView {
                id: listViewNoticers1
                x: 0
                y: 41
                anchors.left: parent.left
                anchors.right: parent.right
                height: 230
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
                            width:60
                            height:24
                            text: name

                            font.pixelSize: 14
                                    font.family: "Times New Roman"
                        }
                        MouseArea{
                            anchors.fill: parent
                            onClicked:{
                                listViewNoticers1.currentIndex = index
                                listViewNoticers2.currentIndex = -1
                                rectangle1.load_feeds_list(name, 1)
                            }
                        }
                    }
                }

                highlight: Rectangle {
                    anchors.left: parent.left
                    anchors.right: parent.right
                    height: 24
                    color: '#ddd'
                }
                focus: true
                //                onCurrentItemChanged:
            }

            ListView {
                id: listViewNoticers2
                x: 8
                y: 298
                flickDeceleration: 1498
                maximumFlickVelocity: 2497
                anchors.rightMargin: 0
                anchors.right: listViewNoticers1.right
                anchors.left: listViewNoticers1.left
                anchors.top: listViewNoticers1.bottom
                anchors.topMargin:40
                anchors.bottom: parent.bottom
                currentIndex: -1

                model: ListModel {
                    id: noticers2_model
                    objectName: "noticers2_model"

                }
                delegate: Component {
                    Item{
                        id: listItem2
                        x:20
                        width: 60
                        height:24

                        Text{
                            width:60
                            height:24
                            text: name

                            font.pixelSize: 14
                                    font.family: "Times New Roman"
                        }
                        MouseArea{
                            anchors.fill: parent
                            onClicked:{

                                listViewNoticers2.currentIndex = index;
                                listViewNoticers1.currentIndex = -1
                                rectangle1.load_feeds_list(name, 2)
                            }
                        }
                    }
                }

                highlight: Rectangle {
                    anchors.left: parent.left
                    anchors.right: parent.right
                    height: 24
                    color: '#ddd'
                }
                focus: true
                //                onCurrentItemChanged:
            }

            Text {
                id: text1
                x: 15
                y: 20
                color: "#878787"
                text: qsTr("关注回答")
                font.bold: true
                        font.family: "Helvetica"
                font.pixelSize: 13
            }

            Text {
                id: text2
                x: 15
                y: 285
                color: "#707070"
                text: qsTr("关注动态")
                font.bold: true
                       font.family: "Helvetica"
                font.pixelSize: 13
            }



        }

        Rectangle {
            id: rectangle2

            anchors.top: parent.top
            anchors.left: rectangle1.right
            width: 218
            anchors.bottom: parent.bottom

            antialiasing: true
            border.color: "#dbdbdb"
            border.width: 1

            ListView {
                id: listViewFeeds
                x: 2
                y: 0
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.topMargin: 2
                width: 214
                height: 593
                currentIndex: -1

                model: ListModel {
                    id: feeds_list_model

                }
                delegate: Component {
                    Item{
                        id: listItem1
                        x:2
                        width: 210
                        height:68

                        Text{
                            width:50
                            height:65
                            text: name

                            font.pixelSize: 12
                            font.family: "Times New Roman"
                        }
                        MouseArea{
                            anchors.fill: parent
                            onClicked:{
                                listViewFeeds.currentIndex = index
                                webView.url = url

                            }
                        }
                    }
                }
                highlight: Rectangle {
                    anchors.left: parent.left
                    anchors.right: parent.right
                    height: 24
                    color: '#ddd'
                }
                focus: true
            }
        }



        WebView{
            id: webView
            width: 762
            anchors.rightMargin: 0
            anchors.bottomMargin: 0
            anchors.leftMargin: 2

            anchors.left: rectangle2.right
            anchors.top: parent.top
            anchors.topMargin: url.toString().match("www.zhihu.com")=="www.zhihu.com" ? -95 : 0
            anchors.right: parent.right
            anchors.bottom: parent.bottom


            objectName: "web_view"

            opacity: 1
            flickDeceleration: 1800
            z: 1
            scale: 1
            maximumFlickVelocity: 2000

        }



    }





}
