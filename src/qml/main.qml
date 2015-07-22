import QtQuick 2.2
import QtWebKit 3.0
import QtQuick.Controls 1.3
import QtQuick.Controls.Styles 1.3
import QtQuick.Layouts 1.0


ApplicationWindow {
    id: applicationWindow
    width: 1020
    height: 600
    color: "#dedede"


    Button {
        objectName: "home_button"
        x: 395
        y: 5
        width: 80
        height: 28
        text: qsTr("主页")
        z: 3
        iconSource: "/Users/yuwei/Pictures/Snip20150717_22.png"

    }
    Button {
        objectName: "add_button"

        x: 470
        y: 5
        width: 80
        height: 28
        text: qsTr("添加")
        z: 2
        iconSource: '/Users/yuwei/Pictures/Snip20150717_25.png'

    }

    Button {
        objectName: "remind_button"

        x: 545
        y: 5
        width: 80
        height: 28
        text: qsTr("提醒")
        iconSource: "/Users/yuwei/Pictures/Snip20150717_11.png"
        z: 1

    }

    Button {
        objectName: "sign_button"

        x: 937
        y: 5
        text: qsTr("登陆")
        z: 2
        enabled: true

    }



    Rectangle {
        id: rectangle0

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom

        anchors.topMargin: 38


        border.color: "#b0aeb0"
        border.width: 2

        Rectangle {
            id: rectangle1
            anchors.left: parent.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            width: 160

            color: "#f6f6f6"
            antialiasing: true
            border.color: "#b0aeb0"
            border.width: 0
            objectName: "rect"
            function updateNoticers1List(noticers1){
                noticers1_model.clear()

                var names = noticers1["names"]

                for(var i = 0; i < names.length; i++){
                    noticers1_model.append({"name": names[i]})                }

            }
            function updateNoticers2List(noticers2){
                noticers2_model.clear()
                var names = noticers2["names"]

                for(var i = 0; i < names.length; i++){
                    noticers2_model.append({"name": names[i]})
                }
            }

            ListModel {
                id: noticers1_model
                objectName: "noticers1_model"
            }

            ListView {
                id: listViewNoticers1
                x: 0
                y: 40
                anchors.left: parent.left
                anchors.right: parent.right
                height: 230
                layoutDirection: Qt.RightToLeft
                currentIndex: -1

                model: noticers1_model

                delegate: Component {
                    Item{
                        id: listItem1
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
                                listViewNoticers1.currentIndex = index
                                listViewNoticers2.currentIndex = -1
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
                font.family: "Courier"
                font.pixelSize: 13
            }

            Text {
                id: text2
                x: 15
                y: 285
                color: "#707070"
                text: qsTr("关注动态")
                font.bold: true
                font.family: "Courier"
                font.pixelSize: 13
            }



        }

        Rectangle {
            id: rectangle2

            anchors.top: parent.top
            anchors.left: rectangle1.right
            width: 208
            anchors.bottom: parent.bottom

            antialiasing: true
            border.color: "#dbdbdb"
            border.width: 1

            ListView {
                id: listViewAnswers
                x: 0
                y: 3
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.topMargin: 10
                width: 208
                height: 593
                model: ListModel {

                }
                delegate: Item {

                    Text {
                        font.pixelSize: 14
                        text: name
                        font.family: "Times New Roman"
                        anchors.verticalCenter: parent.verticalCenter
                    }
                }

            }
        }

        WebView{
            anchors.rightMargin: -18
            anchors.bottomMargin: 0
            anchors.leftMargin: 0

            anchors.left: rectangle2.right
            anchors.top: parent.top
            anchors.topMargin: 1
            anchors.right: parent.right
            anchors.bottom: parent.bottom


            objectName: "web_view"

            opacity: 1
            flickDeceleration: 1800
            z: 1
            scale: 1
            maximumFlickVelocity: 2000

        }

        Rectangle {
            id: rectangle3
            x: 0
            y: 0
            width: 1020
            height: 1
            color: "#afafaf"
            border.color: "#afafaf"
        }

    }





}
