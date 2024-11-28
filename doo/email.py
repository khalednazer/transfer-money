import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, body):
    # إعدادات البريد
    sender_email = "khaledkgccc@gmail.com"
    sender_password = 65958030123

    # إعداد الرسالة
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    print('stpe one ')

    try:
        # الاتصال بخادم SMTP
        print('status 1')
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # تفعيل التشفير
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(" success login email!")
    except Exception as e:
        print('cant send email ')
