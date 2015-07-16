import QtQuick 2.2
import QtQuick.Controls 1.3

Rectangle {
    id: rectangle1
    width: 500
    height: 200
    color: "#ffffff"
    border.width: 3
    border.color: "#c7c7c7"

    TextInput {
        objectName: "email_input"
        id: email_input
        x: 183
        y: 30
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
        x: 129
        y: 30
        text: qsTr("邮箱")
        font.pixelSize: 14
    }

    Text {
        id: text2
        x: 40
        y: 30
        width: 71
        height: 26
        text: qsTr("知乎小号")
        font.bold: false
        wrapMode: Text.WordWrap
        textFormat: Text.PlainText
        font.pixelSize: 16
    }

    Text {
        id: text3
        x: 129
        y: 71
        text: qsTr("密码")
        font.family: "Times New Roman"
        font.pixelSize: 14
    }

    TextInput {
        objectName: "password_input"
        id: password_input
        x: 183
        y: 68
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
        y: 114
        width: 71
        height: 23
        text: qsTr("知乎大号")
        font.bold: false
        font.pixelSize: 16
        textFormat: Text.PlainText
        wrapMode: Text.WordWrap
    }

    Text {
        id: text5
        x: 40
        y: 160
        width: 222
        height: 15
        text: qsTr("注：小号用来爬虫，防止大号被封号")
        font.family: "Times New Roman"
        font.italic: true
        font.pixelSize: 12
    }

    Text {
        id: text6
        x: 129
        y: 114
        text: qsTr("主页")
        font.pixelSize: 14
    }

    TextInput {
        objectName: "url_input"
        id: url_input
        x: 183
        y: 114
        width: 273
        height: 20
        text: qsTr("eg:http://www.zhihu.com/people/cai-tong")
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
        x: 395
        y: 155
        text: qsTr("确认")
        activeFocusOnPress: true
        isDefault: true
        checked: true
        enabled: true
        checkable: true
    }
}

