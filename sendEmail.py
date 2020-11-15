#!/usr/bin/python
# -*- coding: utf-8 -*-
 

import smtplib

from email.mime.text import MIMEText


#Адрес отправителя:
sender = 'Логин@mail.ru'
#Адрес получателя:
recipient = 'Адрес получателя'
#Тема письма:
subj = 'ТЕСТ'
#Текст сообщения:
message = '''Здравствуйте.
             Ознакомиться с моим резюме можно перейдя по <a href="https://github.com/neuromaka/">ссылке</a></body></html>.  
             Результат выполненного тестового задания расположен по <a href="https://github.com/neuromaka/send_email" target="_blank">ссылке</a>.  

          '''
msg = MIMEText(message, "", "utf-8")
msg['Subject'] = subj
msg['From'] = sender
msg['To'] = recipient
 

#Логин:
username = 'Логин@mail.ru'
#Пароль:
password = 'Пароль'
 
#Соединения с сервером по smtp
server = smtplib.SMTP('smtp.mail.ru')
#Переходим в защищенное режим (TLS)
server.starttls()
#Авторизация
server.login(username, password)
#Отправка письма
server.sendmail(sender, recipient, msg.as_string())
#Закрываем соединение с сервером
server.quit()
