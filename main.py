import pprint
import time
import sys
import requests
import json
import re
import PIL.Image

from PySide2.QtWidgets import QApplication, QMessageBox, QWidget, QMainWindow
from PySide2.QtGui import QIcon
from PySide2.QtCore import Signal, QObject
from threading import Thread

from Crypto.Cipher import AES
import base64
import binascii
from hashlib import md5

from main_ui import Ui_MainWindow
from usage_ui import Ui_Form


class Catch_Signals(QObject):
    text_print = Signal(str)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.signal = 3
        self.time_limit = 0
        self.sort_kind = 0
        self.index = -1
        self.class_choose_index = 0
        self.class_choose_index_hold = 0
        self.class_in_0_hold = 0
        self.class_in_1_hold = 0
        self.class_phy_0_hold = 0
        self.class_phy_1_hold = 0
        self.ui.ms = Catch_Signals()
        self.ui.ms.text_print.connect(self.gui)
        self.authorization = self.ui.lineEdit.text()
        self.ui.actionins.triggered.connect(self.usageshowFun)
        self.ui.comboBox_4.addItem('请搜索关键字')
        self.ui.textBrowser.forward()
        # self.ui.textBrowser.setReadOnly(True)

        self.ui.comboBox_2.currentIndexChanged.connect(self.selectionchange_fanan_teacher)
        self.ui.comboBox_3.currentIndexChanged.connect(self.selectionchange_fenji_class)
        self.ui.comboBox_4.currentIndexChanged.connect(self.selectionchange_xuanxiu_num)
        self.ui.comboBox_5.currentIndexChanged.connect(self.selectionchange_fanan_class)
        self.ui.comboBox_6.currentIndexChanged.connect(self.selectionchange_fenji_teacher)

        self.ui.pushButton.clicked.connect(self.go)
        self.ui.pushButton_2.clicked.connect(self.edit_clear)
        self.ui.pushButton_3.clicked.connect(self.handleCalc_fanan)
        self.ui.pushButton_4.clicked.connect(self.handleCalc_fenji)
        self.ui.pushButton_5.clicked.connect(self.handleCalc_xuanxiu)
        self.ui.pushButton_6.clicked.connect(self.handleCalc_get_class)
        self.ui.pushButton_7.clicked.connect(self.handleCalc_get_qr)
        self.ui.pushButton_8.clicked.connect(self.handleCalc_get_token)
        self.ui.pushButton_9.clicked.connect(self.handleCalc_get_choose_class)
        self.ui.pushButton_10.clicked.connect(self.handleCalc_clear_list)
        self.ui.pushButton_11.clicked.connect(self.handleCalc_auto)

        self.uuid = ''
        self.login = {
            'loginname': '',
            'password': '',
            'captcha': '',
            'uuid': ''
        }

        # 获取课程信息的请求网址
        self.list_url = 'http://jwxk.ctgu.edu.cn/xsxk/elective/clazz/list'
        # 提交抢课请求的网址
        self.add_url = 'http://jwxk.ctgu.edu.cn/xsxk/elective/clazz/add'
        # 这个值目前不清楚每个人是否一样，但对每个人是不会变的，也就是说最多设置一次
        self.batchId = '40d2ffddeb04487a98f02ba2b50f60a8'
        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
            'batchId': self.batchId,
            'Authorization': self.authorization,
            'Referer': 'http://jwxk.ctgu.edu.cn/xsxk/elective/grablessons?' + 'batchId=' +
                       self.batchId + 'token=' + self.authorization,
            'Content-Type': 'application/json;charset=UTF-8',
            'Host': 'jwxk.ctgu.edu.cn',
            'Origin': 'http://jwxk.ctgu.edu.cn',
            'Connection': 'keep-alive',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate'
        }

        # 初始化课程类型、方便后续调用
        self.teachingClassType = ['TYKC', 'XGKC', 'FANKC']  # 分别对应：分级课程、全校公共选修、方案内课程

        # 初始化获取到课程的数据库
        self.class_list = [[] for _ in range(100)]
        self.class_list_backup = [[] for _ in range(100)]
        self.class_in_database = [[[] for _ in range(100)] for _ in range(51)]
        self.class_phy_database = [[[] for _ in range(100)] for _ in range(51)]
        self.class_choose_database = [[] for _ in range(51)]
        # 初始化请求参数
        self.get_info_params = {
            'campus': "01",
            'orderBy': "",
            'pageNumber': 1,
            'pageSize': 50,
            'teachingClassType': 'TYKC'
        }

    def usageshowFun(self):
        self.usageFun = Usage()
        self.usageFun.show()

    def gui(self, text):
        self.ui.textBrowser.append(str(text))
        # self.ui.textBrowser.ensureCursorVisible()

    def edit_clear(self):
        self.ui.textBrowser.clear()

    # 选择框条件变更函数
    def selectionchange(self, sort_kind):
        self.sort_kind = sort_kind

    def selectionchange_fanan_teacher(self, sort_kind):
        self.class_in_1_hold = sort_kind

    def selectionchange_fenji_class(self, sort_kind):
        self.class_phy_0_hold = sort_kind
        self.ui.comboBox_6.clear()
        for index, value in enumerate(self.class_phy_database[sort_kind]):
            if value:
                self.ui.comboBox_6.addItem(self.class_phy_database[sort_kind][index][4])

    def selectionchange_xuanxiu_num(self, sort_kind):
        self.class_choose_index_hold = sort_kind

    def selectionchange_fanan_class(self, sort_kind):
        self.class_in_0_hold = sort_kind
        self.ui.comboBox_2.clear()
        for index, value in enumerate(self.class_in_database[sort_kind]):
            if value:
                self.ui.comboBox_2.addItem(self.class_in_database[sort_kind][index][4])

    def selectionchange_fenji_teacher(self, sort_kind):
        self.class_phy_1_hold = sort_kind

    # 添加课程按钮事件触发函数
    def handleCalc_fanan(self):
        self.index += 1
        class_name = self.ui.comboBox_5.currentText()
        class_teacher = self.ui.comboBox_2.currentText()
        class_content = class_name + '---' + class_teacher
        self.ui.comboBox.addItem(class_content)
        for i in self.class_in_database[self.class_in_0_hold][self.class_in_1_hold]:
            self.class_list[self.index].append(i)

    def handleCalc_fenji(self):
        self.index += 1
        class_name = self.ui.comboBox_3.currentText()
        class_teacher = self.ui.comboBox_6.currentText()
        class_content = class_name + '---' + class_teacher
        self.ui.comboBox.addItem(class_content)
        for i in self.class_phy_database[self.class_phy_0_hold][self.class_phy_1_hold]:
            self.class_list[self.index].append(i)

    def handleCalc_xuanxiu(self):
        self.index += 1
        class_content = '选修' + '---' + self.ui.comboBox_4.currentText()
        self.ui.comboBox.addItem(class_content)
        for i in self.class_choose_database[self.class_choose_index_hold]:
            self.class_list[self.index].append(i)

    # 获取验证码
    def handleCalc_get_qr(self):
        thread_get_qrcode = Thread(target=self.thread_get_qrcode,
                                   args=())
        thread_get_qrcode.setDaemon(True)
        thread_get_qrcode.start()

    def thread_get_qrcode(self):
        url_qr = 'http://jwxk.ctgu.edu.cn/xsxk/auth/captcha'
        headers = {
            'Host': 'jwxk.ctgu.edu.cn',
            'Origin': 'http://jwxk.ctgu.edu.cn',
            'Referer': 'http://jwxk.ctgu.edu.cn/xsxk/profile/index.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',

        }
        response = requests.post(url=url_qr, headers=headers).text
        response_json = json.loads(response)
        img_url = response_json['data']['captcha']
        self.uuid = response_json['data']['uuid']
        img_url = re.findall('base64,(.*)', img_url)[0]

        with open('验证码.jpg', 'wb') as f:
            jiema = base64.urlsafe_b64decode(img_url)
            f.write(jiema)

        img = PIL.Image.open('验证码.jpg')
        img.show()

    # 模拟登录
    def handleCalc_get_token(self):
        key = b"MWMqg2tPcDkxcm11"
        iv = b"0000000000000000"
        aes = AEScryptor(key, AES.MODE_ECB, iv, paddingMode="PKCS7Padding", characterSet='utf-8')
        data = self.ui.lineEdit_5.text()
        rData = aes.encryptFromString(data)
        self.login['loginname'] = self.ui.lineEdit_3.text()
        self.login['password'] = str(rData)
        self.login['uuid'] = self.uuid

        if self.ui.lineEdit_4.text():
            self.login['captcha'] = self.ui.lineEdit_4.text()
        else:
            thread_get_token = Thread(target=self.thread_get_qr,
                                      args=())
            thread_get_token.start()

        thread_get_token = Thread(target=self.thread_get_token,
                                  args=())
        thread_get_token.setDaemon(True)
        thread_get_token.start()

    def thread_get_qr(self):
        qr = Chaojiying_Client('Alexation', '1234qwer', '927082')  # 用户中心>>软件ID 生成一个替换 96001
        im = open('验证码.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        self.login['captcha'] = str(qr.PostPic(im, 1902))  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()

    def thread_get_token(self):
        #self.authorization = ''
        headers = {
            'Host': 'jwxk.ctgu.edu.cn',
            'Origin': 'http://jwxk.ctgu.edu.cn',
            'Referer': 'http://jwxk.ctgu.edu.cn/xsxk/profile/index.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
        }
        response = requests.post(url='http://jwxk.ctgu.edu.cn/xsxk/auth/login', data=self.login, headers=headers).text
        response_json = json.loads(response)
        if response_json['data'] == None:
            self.ui.ms.text_print.emit(response_json['msg'])
        else:
            self.ui.ms.text_print.emit(response_json['msg'])
            # self.authorization = response_json['data']['token']
            # self.headers['Authorization'] = self.authorization
            self.headers['Authorization'] = response_json['data']['token']
            self.headers['Referer'] = 'http://jwxk.ctgu.edu.cn/xsxk/elective/grablessons?' + \
                                      'batchId=' + self.batchId + 'token=' + self.authorization
            self.handleCalc_get_class()

    def handleCalc_auto(self):
        before = time.time()
        self.signal += 1
        if self.signal % 2 == 0:
            self.ui.pushButton_11.setText('停止')
            thread_auto = Thread(target=self.thread_auto,
                                 args=(before,))
            thread_auto.setDaemon(True)
            thread_auto.start()
        else:
            self.ui.pushButton_11.setText('自动选课')

    def thread_auto(self, before):
        while 1:
            time.sleep(0.3)
            if self.signal % 2 == 0 and (self.time_limit < 5 * 60):
                self.go()
                self.time_limit = time.time() - before
            else:
                self.ui.pushButton_11.setText('自动选课')
                break

    # 搜索选修事件触发
    def handleCalc_get_choose_class(self):
        self.ui.comboBox_4.clear()
        self.class_choose_database = [[] for _ in range(100)]
        thread_choose_get = Thread(target=self.thread_get_class,
                                   args=(1,))
        thread_choose_get.start()
        thread_choose_get.join()

    # 清空备选列表
    def handleCalc_clear_list(self):
        self.index = -1
        self.ui.comboBox.clear()
        self.class_list = [[] for _ in range(100)]

    # 通过token获取课表
    def handleCalc_get_class(self):
        self.ui.comboBox_2.clear()
        self.ui.comboBox_3.clear()
        self.ui.comboBox_4.clear()
        self.ui.comboBox_5.clear()
        self.ui.comboBox_6.clear()
        self.class_in_database = [[[] for _ in range(100)] for _ in range(51)]
        self.class_phy_database = [[[] for _ in range(100)] for _ in range(51)]
        self.class_choose_database = [[] for _ in range(51)]

        # 获取体育课表
        thread_phy_get = Thread(target=self.thread_get_class,
                                args=(0,))
        thread_phy_get.start()
        thread_phy_get.join()
        # 获取选修课表
        thread_choose_get = Thread(target=self.thread_get_class,
                                   args=(1,))
        thread_choose_get.start()
        thread_choose_get.join()
        # 获取专业内课表
        thread_in_get = Thread(target=self.thread_get_class,
                               args=(2,))
        thread_in_get.start()
        thread_in_get.join()

    # 获取课程信息
    def thread_get_class(self, class_type):
        # self.headers['Authorization'] = self.authorization
        self.get_class_form(self.get_info_params, self.headers, class_type)

    def request_class_info(self, data, headers):
        json_data = json.dumps(data)
        self.headers['Content-Type'] = 'application/json;charset=UTF-8'
        res = requests.post(self.list_url, data=json_data, headers=headers)
        res = json.loads(res.text)
        return res

    def get_class_form(self, data, headers, class_type):
        # 获取体育课程信息
        if class_type == 0:
            data['teachingClassType'] = self.teachingClassType[0]
            if 'KEY' in data.keys():
                del data['KEY']
            res = self.request_class_info(data, headers)
            rows = res['data']['rows']
            time = -1
            for row in rows:
                time += 1
                get_class_name = row['KCM']
                self.ui.comboBox_3.addItem(get_class_name)
                for index, choose_teacher in enumerate(row['tcList']):
                    class_type_str = self.teachingClassType[0]
                    class_id = choose_teacher['JXBID']
                    class_secret = choose_teacher['secretVal']
                    class_name = choose_teacher['sportName']
                    class_teacher = choose_teacher['KXH'] + choose_teacher['SKJS']
                    class_content_list = [class_type_str, class_id, class_secret, class_name, class_teacher]

                    for i in class_content_list:
                        self.class_phy_database[time][index].append(i)

        # 获取选修课程信息
        elif class_type == 1:
            data['teachingClassType'] = self.teachingClassType[1]
            data['KEY'] = self.ui.lineEdit_2.text()
            res = self.request_class_info(data, headers)
            rows = res['data']['rows']
            time = -1
            for row in rows:
                time += 1
                class_type_str = self.teachingClassType[1]
                class_id = row['JXBID']
                class_secret = row['secretVal']
                class_name = row['KCM'] + row['KXH']
                class_teacher = row['KXH'] + row['SKJS']
                class_content_list = [class_type_str, class_id, class_secret, class_name, class_teacher]

                for i in class_content_list:
                    self.class_choose_database[time].append(i)

                self.ui.comboBox_4.addItem(class_name)

        # 获取专业内课程信息
        elif class_type == 2:
            data['teachingClassType'] = self.teachingClassType[2]
            if 'KEY' in data.keys():
                del data['KEY']
            res = self.request_class_info(data, headers)
            rows = res['data']['rows']
            time = -1
            for row in rows:
                time += 1
                get_class_name = row['KCM']
                self.ui.comboBox_5.addItem(get_class_name)
                for index, choose_teacher in enumerate(row['tcList']):
                    class_type_str = self.teachingClassType[2]
                    class_id = choose_teacher['JXBID']
                    class_secret = choose_teacher['secretVal']
                    class_name = choose_teacher['KCM']
                    class_teacher = choose_teacher['KXH'] + choose_teacher['SKJS']
                    class_content_list = [class_type_str, class_id, class_secret, class_name, class_teacher]

                    for i in class_content_list:
                        self.class_in_database[time][index].append(i)

    # 抢！！！
    def go(self):
        self.ui.ms.text_print.emit('\n')
        thread_phy = Thread(target=self.thread_send,
                            args=())
        thread_phy.start()
        thread_phy.join()

    def thread_send(self):
        for class_params in self.class_list:
            if class_params:
                thread_class_params = Thread(target=self.thread_send_go,
                                             args=(class_params,))
                thread_class_params.start()
                # thread_class_params.join()
            else:
                break

    def thread_send_go(self, class_params):
        self.add_class(class_params)

    # 对接选课接口
    def add_class(self, class_info):
        self.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        add_class_data = {
            'clazzType': class_info[0],
            'clazzId': class_info[1],
            'secretVal': class_info[2]
        }
        res = requests.post(self.add_url, data=add_class_data, headers=self.headers)
        res = json.loads(res.text)
        self.ui.ms.text_print.emit(
            res['msg'] + ': ' + class_info[3] + '---' + class_info[4])


# 自定义使用说明类
class Usage(QWidget):
    def __init__(self):
        super(Usage, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


# 以下两个类是aes加密代码、可直接移植、不过要注意更改补全类型
class MData():
    def __init__(self, data=b"", characterSet='utf-8'):
        # data肯定为bytes
        self.data = data
        self.characterSet = characterSet

    def saveData(self, FileName):
        with open(FileName, 'wb') as f:
            f.write(self.data)

    def fromString(self, data):
        self.data = data.encode(self.characterSet)
        return self.data

    def fromBase64(self, data):
        self.data = base64.b64decode(data.encode(self.characterSet))
        return self.data

    def fromHexStr(self, data):
        self.data = binascii.a2b_hex(data)
        return self.data

    def toString(self):
        return self.data.decode(self.characterSet)

    def toBase64(self):
        return base64.b64encode(self.data).decode()

    def toHexStr(self):
        return binascii.b2a_hex(self.data).decode()

    def toBytes(self):
        return self.data

    def __str__(self):
        try:
            return self.toString()
        except Exception:
            return self.toBase64()


class AEScryptor():
    def __init__(self, key, mode, iv=b'', paddingMode="NoPadding", characterSet="utf-8"):
        '''
        构建一个AES对象
        key: 秘钥，字节型数据
        mode: 使用模式，只提供两种，AES.MODE_CBC, AES.MODE_ECB
        iv： iv偏移量，字节型数据
        paddingMode: 填充模式，默认为NoPadding, 可选NoPadding，ZeroPadding，PKCS5Padding，PKCS7Padding
        characterSet: 字符集编码
        '''
        self.key = key
        self.mode = mode
        self.iv = iv
        self.characterSet = characterSet
        self.paddingMode = paddingMode
        self.data = ""

    def __PKCS5_7Padding(self, data):
        needSize = 16 - len(data) % 16
        if needSize == 0:
            needSize = 16
        return data + needSize.to_bytes(1, 'little') * needSize

    def __StripPKCS5_7Padding(self, data):
        paddingSize = data[-1]
        return data.rstrip(paddingSize.to_bytes(1, 'little'))

    def __paddingData(self, data):
        if self.paddingMode == "NoPadding":
            if len(data) % 16 == 0:
                return data
            else:
                return self.__ZeroPadding(data)
        elif self.paddingMode == "ZeroPadding":
            return self.__ZeroPadding(data)
        elif self.paddingMode == "PKCS5Padding" or self.paddingMode == "PKCS7Padding":
            return self.__PKCS5_7Padding(data)
        else:
            return

    def __stripPaddingData(self, data):
        if self.paddingMode == "NoPadding":
            return self.__StripZeroPadding(data)
        elif self.paddingMode == "ZeroPadding":
            return self.__StripZeroPadding(data)

        elif self.paddingMode == "PKCS5Padding" or self.paddingMode == "PKCS7Padding":
            return self.__StripPKCS5_7Padding(data)
        else:
            return

    def setCharacterSet(self, characterSet):
        '''
        设置字符集编码
        characterSet: 字符集编码
        '''
        self.characterSet = characterSet

    def setPaddingMode(self, mode):
        '''
        设置填充模式
        mode: 可选NoPadding，ZeroPadding，PKCS5Padding，PKCS7Padding
        '''
        self.paddingMode = mode

    def encryptFromString(self, data):
        '''
        对字符串进行AES加密
        data: 待加密字符串，数据类型为str
        '''
        self.data = data.encode(self.characterSet)
        return self.__encrypt()

    def __encrypt(self):
        if self.mode == AES.MODE_CBC:
            aes = AES.new(self.key, self.mode, self.iv)
        elif self.mode == AES.MODE_ECB:
            aes = AES.new(self.key, self.mode)
        else:
            return

        data = self.__paddingData(self.data)
        enData = aes.encrypt(data)
        return MData(enData)


# 识别验证码
class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()['pic_str']

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('resources\\logo.png'))
    main_window = MainWindow()
    main_window.show()
    MessageBox = QMessageBox()
    MessageBox.warning(main_window, "警告！",
                       "<div style='font-family: SimHei' size='5' color='#00'>本软件禁止商用！</div>")
    sys.exit(app.exec_())
