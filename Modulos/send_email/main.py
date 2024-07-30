import os
from dotenv import load_dotenv
from pathlib import Path
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()
# CAMINHO DO HTML
CAMINHO_HTML = Path(__file__).parent / 'index.html'
# dados do remetente e destinatario
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# config SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# mensagem de texto
with open(CAMINHO_HTML, 'r', encoding='utf8') as file:
    text = file.read()
    template = Template(text)
    email_text = template.safe_substitute(nome='João')

# Transformar mensagem emm MIMEmultpart
mime_multpart = MIMEMultipart()
mime_multpart['from'] = remetente
mime_multpart['to'] = destinatario
mime_multpart['subject'] = 'Este é o assunto do email'

corpo = MIMEText(email_text, 'html', 'utf-8')
mime_multpart.attach(corpo)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(mime_multpart)
    print('Email enviado com sucesso')
