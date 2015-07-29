import QtQuick 2.2
import QtQuick.Controls 1.3

Rectangle {
    id: rectangle1
    width: 300
    height: 100
    color: "#ffffff"
    border.width: 0
    border.color: "#c7c7c7"

    Text {
        objectName: "errorInfoText"

        id: text1
        x: 20
        y: 40
        width: 160
        height: 20
        text: qsTr("错误")
        font.family: "Times New Roman"
        font.pixelSize: 14
    }
}

