# Scramble Classes CTGU

main.py是主程序

打包好的程序在dist文件夹下

usage.ui、usage_ui.py、main.ui、main_ui.py是ui界面

logo.ico以及resources文件夹里是一些基本ico资源

<font style="font-weight:700;color:#B399FF">详细的使用方法已经封装到软件里了，来说一下几个关键点吧</font>

1. Pyside2弹窗跳转

   ```
   class Usage(QWidget):
       def __init__(self):
           super(Usage, self).__init__()
           self.ui = Ui_Form()
           self.ui.setupUi(self)
   ```

   使用了“动态加载”会有bug。采用静态方式加载，这样事件也可以覆盖，非常类似于直接使用Qt IDE开发工具一样方便。

2. 提交选课请求

   提交选课请求，抓包，看发送的数据，寻找差异点requests构造请求。

3. 模拟登陆

   提交登录请求，抓包，查看login，发现post请求提交的参数有四个，分别是：账号、密码（这里有加密）、验证码结果以及验证码ID。验证码通过另一个包也就是captcha返回的数据进行分析。

4. 密码加密

   在js代码中拿到AES密钥后python构造函数加密，补齐方式为PKCS7Padding。

   ```
   key = b"MWMqg2tPcDkxcm11"
   iv = b"0000000000000000"
   aes = AEScryptor(key, AES.MODE_ECB, iv, paddingMode="PKCS7Padding", characterSet='utf-8')
   data = self.ui.lineEdit_5.text()
   rData = aes.encryptFromString(data)
   ```

   