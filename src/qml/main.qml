import QtQuick 2.2
import QtWebKit 3.0
import QtQuick.Controls 1.3
import QtQuick.Controls.Styles 1.3
import QtQuick.Layouts 1.0


ApplicationWindow {
    id: test
    width: 1020
    height: 600


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
            border.width: 1
            objectName: "rect"


            ListModel {
                id: noticers1_model
                objectName: "noticers1_model"
                function updateNoticersList(noticers1_names){
                    noticers1_model.clear()
                    for(var i = 0; i < noticers1_names.length; i++){
                        noticers1_model.append({"name":noticers1_names[i]})
                    }

                }
            }


            ListView {
                id: listViewNoticers1
                x: 25
                y: 40

                width: 135
                height: 230

                model: noticers1_model


                delegate: Component {

                        Text {
                            width:50
                            height: 24
                            text: name
                            font.pixelSize: 14
                            font.family: "Times New Roman"
                        }
                }
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
                model: ListModel {
                    ListElement {
                        name: "Grey"

                    }
                }
                delegate: Item {
                    x: 5
                    width: 80
                    height: 60



                        Text {

                            text: name
                            font.family: "Times New Roman"
                            font.pixelSize: 14
                            anchors.verticalCenter: parent.verticalCenter
                        }

                }
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
            width: 190
            anchors.bottom: parent.bottom

            antialiasing: true
            border.color: "#b0aeb0"
            border.width: 1

            ListView {
                id: listViewAnswers
                x: 0
                y: 3
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.topMargin: 10
                width: 190
                height: 593
                model: ListModel {
                    ListElement {
                        name: "Grey"

                    }

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

    }




}
