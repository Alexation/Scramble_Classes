# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(637, 401)
        font = QFont()
        font.setFamily(u"\u9ed1\u4f53")
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamily(u"\u9ed1\u4f53")
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.textBrowser.setFont(font1)
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
"	font: 9pt \"\u9ed1\u4f53\";\n"
"	background-color: rgba(170, 170, 255, 0); \n"
"	rgba: (170, 170, 255, 0)\n"
"}")
        self.textBrowser.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.textBrowser.setFrameShape(QFrame.Box)
        self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textBrowser.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.textBrowser)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Instruction", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\u9ed1\u4f53'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-------------------------------Welcome to Scramble for classes ---------------------------------</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'SimSun';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u4f7f\u7528\u65b9\u6cd5\uff1a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px"
                        ";\">1.\u786e\u8ba4\u7f51\u7edc\u8fde\u63a5\u6b63\u5e38\u3001\u6b64\u8f6f\u4ef6\u80fd\u6b63\u786e\u8bbf\u95ee\u7f51\u7edc</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u5728\u53f3\u4fa7\u8f93\u5165\u8d26\u53f7\u5bc6\u7801\u8fdb\u884c\u767b\u5f55\uff0c\u6216\u8005\u5de6\u4fa7\u9876\u90e8\u8f93\u5165\u4e2a\u4ebatoken\uff08\u767b\u5f55\u540e\u968f\u4fbf\u9009\u62e9\u4e00\u4e2a\u6570\u636e\u5305\uff0c\u8f93\u5165cookie\u4e2d\u7684Authorization\u7684\u503c\u5373\u53ef)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u767b\u5f55\u6210\u529f\u540e\uff0c\u9009\u62e9\u8bfe\u7a0b\u5e76\u6dfb\u52a0\u5230\u9009\u8bfe\u5217\u8868\u4e2d</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.\u786e\u8ba4\u9009\u8bfe\u5217\u8868\u65e0\u8bef\u540e\uff0c\u5f00\u59cb\u9009\u8bfe</p>\n"
"<"
                        "p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6ce8\u610f\u4e8b\u9879\uff1a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u4f7f\u7528\u672c\u8f6f\u4ef6\u767b\u5f55\u8d26\u53f7\u53ef\u80fd\u4f1a\u5bfc\u81f4\u6d4f\u89c8\u5668\u8d26\u53f7\u88ab\u8feb\u4e0b\u7ebf</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u9ed8\u8ba4\u9009\u8bfe\u987a\u5e8f\u5373\u4e3a\u9009\u8bfe\u5217\u8868\u987a\u5e8f</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u7531\u4e8e\u5b50\u7ebf\u7a0b\u4e0e\u8fdc\u7a0b\u670d\u52a1\u5668\u4ea4\u4e92\uff0c\u4f1a\u6709"
                        "\u4e00\u6bb5\u65f6\u95f4\u7684\u5ef6\u8fdf\uff0c\u8bf7\u8010\u5fc3\u7b49\u5f85\u54e6\uff1c\uff08\uff3e\uff0d\uff3e\uff09\uff1e</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u514d\u8d23\u58f0\u660e\u26a0\uff1a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u672c\u8f6f\u4ef6\u63d0\u4f9b\u7684\u6240\u6709\u529f\u80fd\uff0c\u4ec5\u53ef\u4f5c\u5b66\u4e60\u4ea4\u6d41\u4f7f\u7528\uff0c\u672a\u7ecf\u539f\u4f5c\u8005\u6388\u6743\uff0c\u7981\u6b62\u7528\u4e8e\u5176\u4ed6\u7528\u9014\u3002\u8bf7\u5728\u4e0b\u8f7d24\u5c0f\u65f6\u5185\u5220\u9664\u3002\u8c22\u8c22</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u82e5"
                        "\u62a5\u9519\u3001\u751a\u81f3\u65e0\u6cd5\u8fd0\u884c\u7b49\u60c5\u51b5\u51fa\u73b0\u53ef\u7b49\u5f85\u6bb5\u65f6\u95f4\u518d\u6b21\u5c1d\u8bd5\u6216\u91cd\u542f\u672c\u7a0b\u5e8f</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u672c\u7a0b\u5e8f\u5c1a\u672a\u5927\u91cf\u6d4b\u8bd5\uff0c\u56e0\u4f7f\u7528\u672c\u8f6f\u4ef6\u4ea7\u751f\u7684\u95ee\u9898\uff0c\u8f6f\u4ef6\u4f5c\u8005\u6982\u4e0d\u8d1f\u8d23</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.\u672c\u7a0b\u5e8f\u672a\u8fdb\u884c\u5ef6\u8fdf\u4ee5\u53ca\u5f02\u5e38\u5904\u7406\uff0c\u6ca1\u6709\u4f7f\u7528ip\u4ee3\u7406\u3001\u82e5\u51fa\u73b0\u672c\u5730ip\u88ab\u8be5\u7f51\u7ad9\u5c01\u6740\u7b49\u60c5\u51b5\uff0c\u8bf7\u81ea\u884c\u91cd\u542f\u8def\u7531\u5668\uff0c\u82e5\u8fc7\u5206\u4f7f\u7528\u672c\u7a0b\u5e8f\u9020\u6210\u670d\u52a1\u5668\u5d29\u6e83\uff0c\u672c\u7a0b\u5e8f\u4e0d\u8d1f"
                        "\u76f8\u5173\u8d23\u4efb</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u7a0b\u5e8f\u6e90\u7801:<a href=\"https://github.com/Alexation/Scramble_Classes\"><span style=\" text-decoration: underline; color:#0000ff;\">Alexation/Scramble_Classes (github.com)</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u66f4\u65b0\u8bf4\u660e\uff1a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">v4.0</p>\n"
"<p style=\""
                        " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u518d\u6b21\u91cd\u6784\u7a0b\u5e8f\u4ee3\u7801\uff0c\u6dfb\u52a0\u9009\u4fee\u8bfe\u7a0b\u641c\u7d22\u529f\u80fd</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u8865\u5145\u4e00\u4e9b\u5c0f\u529f\u80fd\u3001\u4f18\u5316\u4ee3\u7801\u7ec6\u8282</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">v3.0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u91cd\u6784\u8f6f\u4ef6\u6574\u4f53\u67b6\u6784\uff0c\u4fee\u590d\u91cd\u590d\u9009\u8bfe\u65e0\u6548\u7684bug</p>\n"
"<p style=\" margin-top:0px; margin-b"
                        "ottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u652f\u6301\u8d26\u53f7\u5bc6\u7801\u767b\u5f55\u64cd\u4f5c</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">v2.0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u8865\u5145GUI\u754c\u9762\uff0c\u64cd\u4f5c\u66f4\u65b9\u4fbf</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u4e0d\u540c\u7c7b\u578b\u8bfe\u7a0b\u5206\u5e03\u6574\u7406\uff0c\u5229\u4e8e\u7528\u6237\u67e5\u770b</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u91cd\u6784\u7c7b</p>"
                        "\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">v1.0</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u9009\u8bfe\uff01</p></body></html>", None))
    # retranslateUi

