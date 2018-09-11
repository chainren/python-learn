# -*- coding: utf8 -*-

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib


#获取参数
from_addr = input('From:')
password = input('Pass:')
to_addr = input('To:')
smtp_server = input('SMTP_Server:')
content = input('Content:')


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode('utf-8'), addr))


# 构建邮件内容
msg = MIMEMultipart()

# 添加文本内容
subtype = 'plain'
# 在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了，我们输入一段html，
if 'html' in content:
    subtype = 'html'
text = MIMEText(content, subtype, 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候----', 'utf-8').encode()

msg.attach(text)

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('./attch.jpg', 'rb') as f:
    # 设置附件的MIME和文件名
    mime = MIMEBase('image', 'jpeg', filename = 'test.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)


# 要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去，
# 然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。


# 利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative：
# msg = MIMEMultipart('alternative')


# 加密SMTP
# 使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
# 只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接。

# 发送邮件
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
