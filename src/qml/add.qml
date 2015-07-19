import QtQuick 2.2
import QtQuick.Controls 1.3

Rectangle {
    id: rectangle1
    width: 450
    height: 220
    color: "#ffffff"
    border.width: 0
    border.color: "#c7c7c7"

    Text {
        id: text6
        x: 51
        y: 36
        width: 28
        height: 17
        text: qsTr("主页url")
        font.pixelSize: 14
        font.family: "Times New Roman"
    }

    TextInput {
        objectName: "url_input"
        id: url_input
        x: 130
        y: 33
        width: 273
        height: 20
        text: qsTr("http://www.zhihu.com/people/yuwei-80")
        selectionColor: "#800000"
        opacity: 1
        visible: true
        passwordCharacter: "•"
        font.family: "Times New Roman"
        echoMode: TextInput.Normal
        cursorVisible: true
        horizontalAlignment: Text.AlignLeft
        font.pixelSize: 14
    }

    Button {
        id: button1
        x: 195
        y: 186
        text: qsTr("确认")
        activeFocusOnPress: true
        enabled: true
        checked: true
        isDefault: true
        objectName: "button"
        checkable: true
    }

    Text {
        id: text1
        x: 51
        y: 87
        text: qsTr("关注方式")
        font.pixelSize: 12
        font.family: "Times New Roman"
    }


    SpinBox {
        id: spinBox1
        x: 130
        y: 83
        minimumValue: 1
        maximumValue: 2

        objectName: 'notice_method'
    }


    Text {
        id: text2
        x: 51
        y: 150
        text: qsTr("是否提醒")
        font.pixelSize: 12
        font.family: "Times New Roman"
    }

    SpinBox {
        id: spinBox2
        x: 130
        y: 146

        minimumValue: 0
        maximumValue: 1

        objectName: 'is_remind'
    }

    Text {
        id: text3
        x: 213
        y: 87
        text: qsTr("1为关注回答，2为关注动态")
        font.pixelSize: 12
        font.family: "Times New Roman"
    }

    Text {
        id: text4
        x: 213
        y: 151
        text: qsTr("0为不提醒，1为提醒")
        font.pixelSize: 12
        font.family: "Times New Roman"
    }
}

