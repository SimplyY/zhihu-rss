import QtQuick 2.0
import QtQuick.Controls 1.3

Rectangle {
    width: 400
    height: 200
    objectName: "rect"

    Text {
        id: text1
        x: 119
        y: 21
        width: 165
        height: 15
        text: qsTr("你想要关注的动态类型")
        font.bold: true

        font.pixelSize: 15
    }

    CheckBox {
        id: checkBox1
        x: 26
        y: 62
        text: qsTr("回答问题")
        objectName: "checkBox1"

    }

    CheckBox {
        id: checkBox2
        x: 116
        y: 62
        text: qsTr("赞同回答")
        objectName: "checkBox2"
    }

    CheckBox {
        id: checkBox3
        x: 206
        y: 62
        text: qsTr("提出问题")
        objectName: "checkBox3"
    }

    CheckBox {
        id: checkBox4
        x: 296
        y: 62
        text: qsTr("关注问题")
        objectName: "checkBox4"
    }

    CheckBox {
        id: checkBox5
        x: 26
        y: 113
        text: qsTr("赞同文章")
        objectName: "checkBox5"
    }

    CheckBox {
        id: checkBox6
        x: 116
        y: 113
        text: qsTr("关注话题")
        objectName: "checkBox6"
    }

    CheckBox {
        id: checkBox7
        x: 206
        y: 113
        text: qsTr("关注专栏")
        objectName: "checkBox7"
    }

    CheckBox {
        id: checkBox8
        x: 296
        y: 113
        text: qsTr("发表文章")
        objectName: "checkBox8"
    }

    Button {
        id: button1
        x: 223
        y: 155
        text: qsTr("确定")
        enabled: true
        activeFocusOnPress: true
        isDefault: false
        checkable: true
        objectName: "button"

    }

    Button {
        id: button2
        x: 116
        y: 155
        text: qsTr("全选")
        isDefault: false
        objectName: "all_sel_button"

    }


}
