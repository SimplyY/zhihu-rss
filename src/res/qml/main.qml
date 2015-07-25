import QtQuick 2.0
import QtWebKit 3.0
import QtQuick.Controls 1.3
import QtQuick.Controls.Styles 1.3
import QtQuick.Layouts 1.0


ApplicationWindow {
    id: applicationWindow
    width: 1400
    height: 750
    color: "#dedede"
    maximumWidth: 1500
    title: "zhihu rss "
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

            Item { Layout.preferredWidth: 100 }
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

            Item { Layout.preferredWidth: 100 }

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

            Item { Layout.preferredWidth: 100 }
            ToolButton {
                tooltip: qsTr("powered by SimplyY")
                text: qsTr("powered by SimplyY")
//                iconSource: "images/right-32.png"

                Layout.preferredWidth: navigationBar.height
                style: ButtonStyle {
                    background: Rectangle { color: "transparent" }

                }
            }

            Item { Layout.preferredWidth: 65 }


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

                var model = noticers1_model
                model.append({"name": feeds_list["name"], "feedslist": feeds_list})

                var feeds = feeds_list["feeds"]

                for(var i in feeds){
                    feeds_list_model.append({"name": feeds[i]["action"], "url": feeds[i]["url"]})
                }
            }


            function updateNoticersList(args){
                noticers1_model.clear()

                var names = args["names"]
                var feedslists = args["feedslists"]

                for(var i = 0; i < names.length; i++){
                    console.debug(i, names[i])
                    noticers1_model.append({"name": names[i], "feedslist": feedslists[i]})
                }

            }

            function load_feeds_list(name, i){
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

                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom

                anchors.topMargin: 40
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



            Text {
                id: text1
                x: 15
                y: 20
                color: "#878787"
                text: qsTr("noticers")
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


            Text {
                id: text2
                x: 5
                y: 18
                color: "#878787"
                text: qsTr("feeds")
                font.bold: true
                font.family: "Helvetica"
                font.pixelSize: 14
            }


            ListView {
                id: listViewFeeds
                x: 2
                y: 0
                anchors.top: text2.bottom
                anchors.bottom: parent.bottom
                anchors.topMargin: 9
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
                        width: 200
                        height:60

                        Text{
                            width:50
                            height:60
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

                    height: 20
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



    }





}
