#importações
import smtplib
from email.message import EmailMessage  

#======================================================================================================================

#Informações
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'italoespiritosantovieira@gmail.com'
sender_password = 'nqva dzhm kdmf yaye'

#=======================================================================================================================
def enviar2():
 #Compondo o e-mail
 msg = EmailMessage()
 msg['Subject'] = 'Email com anexo'
 msg['From'] = sender_email
 msg['To'] = 'italocontagamer@gmail.com'
 msg.set_content("Segue a Planilha de Excel")

 #anexando arquivo
 with open('Planilha.xlsx', 'rb') as content_file:
  content = content_file.read()
  msg.add_attachment(content, maintype='application', subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename='Planilha.xlsx')

 #Enviando o e-mail com anexo
 with smtplib.SMTP(smtp_server, smtp_port) as smtp:
  smtp.starttls()
  smtp.login(sender_email, sender_password)
  smtp.send_message(msg)
  smtp.quit()