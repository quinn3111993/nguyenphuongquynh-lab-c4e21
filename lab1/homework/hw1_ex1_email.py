from gmail import GMail, Message
import datetime as dt 

mail = GMail("quinn.nguyen311@gmail.com", "hvtt123456")
body = '''
<p>Đơn xin nghỉ phép</p>
<p>&nbsp;</p>
<p>I need a break. Thanks!</p>
<p>&nbsp;</p>
<p><em>Quinn.</em></p>'''
msg = Message("Đơn xin nghỉ phép", to="nphuongquynh311@gmail.com", html=body)

while True:
    now = dt.datetime.now().hour
    if now == 7:
        mail.send(msg)
        break