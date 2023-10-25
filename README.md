# MailOC
基于email，smtplib实现的发送邮件

## 前置步骤
在正式使用前需要将已实例化的mime和stp传入MailOC，如下：
```python
import smtplib
from email.mime.multipart import MIMEMultipart
from mail_oc import MailOC

# mime
mime = MIMEMultipart('related')

# stp
stp = smtplib.SMTP()
stp.connect("smtp.qq.com", 25)  # MAIL_HOST, MAIL_PORT 
stp.login(os.environ.get("EMAIL"), os.environ.get("LICENSE"))   # EMAIL, LICENSE

# init
MailOC(mime, stp)
```
