import QtQuick 2.2
import QtWebKit 3.0
import QtQuick.Controls 1.3
import QtQuick.Controls.Styles 1.3
import QtQuick.Layouts 1.0


ApplicationWindow {
    id: test
    width: 900
    height: 650


    Button {
        objectName: "home_button"
        x: 317
        y: 12
        width: 80
        height: 28
        text: qsTr("主页")
        z: 3
        iconSource: "/Users/yuwei/Pictures/Snip20150717_22.png"
    }
    Button {
        objectName: "add_button"

        x: 392
        y: 12
        width: 80
        height: 28
        text: qsTr("添加")
        z: 2
        iconSource: '/Users/yuwei/Pictures/Snip20150717_25.png'

    }

    Button {
        objectName: "remind_button"

        x: 467
        y: 12
        width: 80
        height: 28
        text: qsTr("提醒")
        iconSource: "/Users/yuwei/Pictures/Snip20150717_11.png"
        z: 1

    }

    Button {
        objectName: "sign_button"

        x: 839
        y: 14
        text: qsTr("登陆")
        z: 2


        enabled: true

    }



    Rectangle {
        id: rectangle0

        anchors.left: parent.left
        anchors.right: parent.right

        y: 52

        height: 598
        border.width: 2

        Rectangle {
            id: rectangle1
            anchors.left: parent.left
            width: 210
            height: 598
            color: "#ffffff"
            antialiasing: true
            border.color: "#b0aeb0"
            border.width: 1

            ListView {
                id: listView2
                x: 8
                y: 8
                width: 110
                height: 160
                model: ListModel {
                    ListElement {
                        name: "Grey"
                        colorCode: "grey"
                    }

                    ListElement {
                        name: "Red"
                        colorCode: "red"
                    }

                    ListElement {
                        name: "Blue"
                        colorCode: "blue"
                    }

                    ListElement {
                        name: "Green"
                        colorCode: "green"
                    }
                }
                delegate: Item {
                    x: 5
                    width: 80
                    height: 40
                    Row {
                        id: row2
                        spacing: 10
                        Rectangle {
                            width: 40
                            height: 40
                            color: colorCode
                        }

                        Text {
                            text: name
                            font.bold: true
                            anchors.verticalCenter: parent.verticalCenter
                        }
                    }
                }
            }

            ListView {
                id: listView3
                x: 8
                y: 298
                width: 110
                height: 160
                model: ListModel {
                    ListElement {
                        name: "Grey"
                        colorCode: "grey"
                    }

                    ListElement {
                        name: "Red"
                        colorCode: "red"
                    }

                    ListElement {
                        name: "Blue"
                        colorCode: "blue"
                    }

                    ListElement {
                        name: "Green"
                        colorCode: "green"
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
                            color: colorCode
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

            anchors.left: rectangle1.right
            width: 210
            height: 598
            color: "#ffffff"
            antialiasing: true
            border.color: "#b0aeb0"
            border.width: 1

            ListView {
                id: listView1
                x: 0
                y: 0
                width: 210
                height: 598
                model: ListModel {
                    ListElement {
                        name: "Grey"
                        colorCode: "grey"
                    }

                    ListElement {
                        name: "Red"
                        colorCode: "red"
                    }

                    ListElement {
                        name: "Blue"
                        colorCode: "blue"
                    }

                    ListElement {
                        name: "Green"
                        colorCode: "green"
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
                            color: colorCode
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
