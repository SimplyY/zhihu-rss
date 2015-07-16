import QtQuick 2.2
import QtWebKit 3.0
import QtQuick.Controls 1.3


Rectangle {
    id: test
    width: 1100
    height: 700

    Button {
        objectName: "sign_button"
        x: 868
        y: 20
        text: qsTr("Button")
    }

    WebView{
        objectName: "web_view"
        x: 526
        y: 76
        width: 418
        height: 462

    }
}
