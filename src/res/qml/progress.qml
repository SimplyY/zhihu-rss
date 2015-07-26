import QtQuick 2.2

Rectangle {
    width: 320
    height: 160
    border.width: 0
    objectName: "rect"

    function load_data(args){
        var name = args["name"]
        var amount_num = args["amount_num"]

        text_name.text = name
        text_amount_num.text = amount_num
    }

    function load_feeds_num(args){
        var feeds_num = args["feeds_num"]

        text_feeds_num.text = feeds_num
    }

    Text {
        id: text1
        x: 57
        y: 29
        text: qsTr("你正在添加关注")
        font.family: "Times New Roman"
        font.pixelSize: 14
    }

    Text {
        id: text_name
        x: 178
        y: 29
        width: 65
        height: 17
        text: qsTr("")
        font.pixelSize: 14
    }

    Text {
        id: text3
        x: 57
        y: 69
        text: qsTr("所需爬取的动态数")
        font.pixelSize: 14
    }

    Text {
        id: text_amount_num
        x: 198
        y: 69
        text: qsTr("Text")
        font.family: "Times New Roman"
        font.pixelSize: 14
    }

    Text {
        id: text5
        x: 57
        y: 109
        width: 112
        height: 16
        text: qsTr("目前已爬取动态数")
        font.family: "Times New Roman"
        font.pixelSize: 14
    }

    Text {
        id: text_feeds_num
        x: 198
        y: 109
        font.family: "Times New Roman"
        text: qsTr("Text")
        font.bold: false
        font.pixelSize: 14
    }


}

