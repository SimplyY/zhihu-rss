import QtQuick 2.0
import QtQuick.Controls 1.3

Rectangle {
    id: rectangle1
    width: 450
    height: 220
    color: "#ffffff"
    border.width: 0
    border.color: "#c7c7c7"

    TextInput {
        objectName: "email_input"
        id: email_input
        x: 175
        y: 33
        width: 273
        height: 20
        color: "#2e2e2e"
        text: qsTr("test@test.com")
        font.family: "Times New Roman"
        transformOrigin: Item.Center
        clip: false
        inputMask: ""
        cursorVisible: true
        font.pixelSize: 14
    }

    Text {
        id: text1
        x: 134
        y: 33
        text: qsTr("邮箱")
        font.pixelSize: 14
    }

    Text {
        id: text2
        x: 40
        y: 32
        width: 71
        height: 20
        text: qsTr("知乎小号:")
        font.bold: false
        wrapMode: Text.WordWrap
        textFormat: Text.PlainText
        font.pixelSize: 16
    }

    Text {
        id: text3
        x: 134
        y: 69
        text: qsTr("密码")
        font.family: "Times New Roman"
        font.pixelSize: 14
    }

    TextInput {
        objectName: "password_input"
        id: password_input
        x: 175
        y: 69
        width: 273
        height: 20
        text: qsTr("")
        font.family: "Times New Roman"
        inputMask: qsTr("")
        passwordCharacter: ""
        echoMode: TextInput.Password
        cursorVisible: true
        font.pixelSize: 14
    }

    Text {
        id: text4
        x: 40
        y: 116
        width: 71
        height: 17
        text: qsTr("知乎帐号:")
        font.bold: false
        font.pixelSize: 16
        textFormat: Text.PlainText
        wrapMode: Text.WordWrap
    }

    Text {
        id: text5
        x: 40
        y: 163
        width: 222
        height: 15
        text: qsTr("注：小号用来爬虫，防止大号被封号")
        font.family: "Times New Roman"
        font.italic: true
        font.pixelSize: 12
    }

    Text {
        id: text6
        x: 134
        y: 117
        text: qsTr("主页")
        font.pixelSize: 14
    }

    TextInput {
        objectName: "url_input"
        id: url_input
        x: 175
        y: 117
        width: 273
        height: 20
        text: qsTr("http://www.zhihu.com/people/yuwei-80")
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
        objectName: "button"
        id: button
        x: 342
        y: 158
        text: qsTr("确认")
        activeFocusOnPress: true
        isDefault: true
        checked: true
        enabled: true
        checkable: true
    }
}
