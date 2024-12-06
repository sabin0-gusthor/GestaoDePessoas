import os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

EMAIL ="api.rh.gs@gmail.com"
PASSWORD ="jfjqjnmahdjijxvp"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def carregar_destinatarios():
    try:
        with open("emails.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Erro: Arquivo 'emails.json' não encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: Não foi possível decodificar o arquivo 'emails.json'.")
        return []

def carregar_mensagem():
    try:
        with open("mensagem.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Erro: Arquivo 'mensagem.json' não encontrado.")
        return {"assunto": "Assunto padrão", "mensagem": ""}
    except json.JSONDecodeError:
        print("Erro: Não foi possível decodificar o arquivo 'mensagem.json'.")
        return {"assunto": "Assunto padrão", "mensagem": ""}

def enviar_email(destinatario):
    mensagem_data = carregar_mensagem()
    assunto = mensagem_data["assunto"]
    link = mensagem_data["mensagem"]

    mensagem_html = f"""
        <html>
        <head>
            <meta charset="UTF-8">
        </head>
        <body>
            <h2>Acesse o Formulário</h2>
            <p>Olá,</p>
            <p>Estamos realizando uma pesquisa importante para aprimorar nossos processos e serviços. Sua participação é fundamental para nos ajudar a entender melhor suas necessidades e expectativas.</p>
            <p>Por favor, dedique alguns minutos para preencher o formulário no link abaixo:</p>
            <p><a href="{link}">Acesse o Formulário</a></p>
            <p>Agradecemos sua colaboração!</p>
            <p>Atenciosamente,<br>Equipe de Gestão</p>
        </body>
        </html>
        """


    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem_html, 'html'))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, destinatario, msg.as_string())
        print(f"E-mail enviado para {destinatario}")
    except Exception as e:
        print(f"Erro ao enviar e-mail para {destinatario}: {e}")

def main():
    destinatarios = carregar_destinatarios()
    for destinatario in destinatarios:
        enviar_email(destinatario)

if __name__ == "__main__":
    main()
