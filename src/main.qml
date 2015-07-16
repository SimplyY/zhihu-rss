import QtQuick 2.2
import QtWebKit 3.0
import QtQuick.Controls 1.3


Rectangle {
    id: test
    width: 1100
    height: 700

    Button {
        objectName: "sign_button"
        x: 697
        y: 20
        text: qsTr("Button")
        z: 2
    }

    WebView{
        width: 100
        height: 200
        anchors.rightMargin: -100
        anchors.bottomMargin: 0
        anchors.leftMargin: 400
        anchors.topMargin: 80
        objectName: "web_view"
        anchors.fill: parent
        opacity: 1
        flickDeceleration: 1800
        z: 1
        scale: 1
        maximumFlickVelocity: 2000

    }
}
