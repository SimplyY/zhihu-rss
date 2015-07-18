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
            width: 180

            color: "#f6f6f6"
            antialiasing: true
            border.color: "#b0aeb0"
            border.width: 1

            ListView {
                id: listViewNoticers0
                x: 8
                y: 8
                width: 170
                height: 250
                boundsBehavior: Flickable.StopAtBounds
                orientation: ListView.Horizontal

                model: listViewNoticers0Model

                delegate: Item {
                    x: 5
                    width: 80
                    height: 40

                    Row {
                        id: row2
                        spacing: 10

                        Text {
                            text: model.name
                            font.bold: true
                            anchors.verticalCenter: parent.verticalCenter
                        }
                    }
                }
            }

            ListView {
                id: listViewNoticers1
                x: 8
                y: 298
                anchors.right: listViewNoticers0.right
                anchors.top: listViewNoticers0.bottom
                anchors.bottom: parent.bottom
                model: ListModel {
                    ListElement {
                        name: "Grey"

                    }


                }
                delegate: Item {
                    x: 5
                    width: 80
                    height: 40
                    Row {
                        id: row3
                        spacing: 10
                        Rectangle {
                            width: 40
                            height: 40

                        }

                        Text {
                            text: name
                            font.bold: true
                            anchors.verticalCenter: parent.verticalCenter
                        }
                    }
                }
            }



        }

        Rectangle {
            id: rectangle2

            anchors.top: parent.top
            anchors.left: rectangle1.right
            width: 190
            anchors.bottom: parent.bottom
            color: "#ffffff"
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
                    x: 5
                    width: 80
                    height: 40
                    Row {
                        id: row1
                        spacing: 10
                        Rectangle {
                            width: 40
                            height: 40

                        }

                        Text {
                            text: name
                            font.bold: true
                            anchors.verticalCenter: parent.verticalCenter
                        }
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
