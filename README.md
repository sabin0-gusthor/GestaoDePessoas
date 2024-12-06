🌟 Projeto: Monitoramento de Bem-Estar dos Funcionários
Este repositório contém a implementação de um sistema para monitorar o bem-estar dos funcionários, unindo automação de processos com análise de dados.

📋 Descrição do Projeto
O projeto foi desenvolvido para automatizar o envio de formulários de bem-estar, coletar as respostas e apresentar os resultados em um dashboard de Business Intelligence (BI). Ele é composto por três etapas principais:

📧 Envios Automatizados de E-mails

Script em Python para envio de e-mails personalizados com o link do Microsoft Forms.
📊 Coleta e Armazenamento de Respostas

Integração com a API do Microsoft Forms para extração e armazenamento das respostas.
📈 Dashboard Interativo

Visualização de dados coletados em gráficos e indicadores para análise e tomada de decisão.
👥 Autores
📝 Luiz Eduardo: Criador do escopo e planejamento do projeto.
💻 Gusthor Sabino: Desenvolvimento e implementação do código em Python.
📋 Gabriel Oliveira: Criação e estruturação dos formulários no Microsoft Forms.

🔧 Tecnologias Utilizadas
🐍 Python
Bibliotecas: smtplib, json, email.
📧 Gmail SMTP
Configuração para envio de e-mails através do servidor do Gmail.
📋 Microsoft Forms
Ferramenta de criação de formulários.
🚀 Como Usar
1. Pré-requisitos
✅ Python 3.x instalado.
✅ Conta no Gmail configurada para acesso via SMTP.
✅ Configurar a permissão para "Aplicativos menos seguros" na conta do Gmail.
2. Configuração Inicial
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/nome-do-repositorio.git  
Insira os destinatários no arquivo emails.json no seguinte formato:

json
Copiar código
[  
    "email1@exemplo.com",  
    "email2@exemplo.com"  
]  
Personalize o conteúdo da mensagem no arquivo mensagem.json:

json
Copiar código
{  
    "assunto": "Seu Assunto Aqui",  
    "mensagem": "https://link-do-formulario.com"  
}  
Configure o e-mail e senha no arquivo main.py:

python
Copiar código
EMAIL = "seu-email@gmail.com"  
PASSWORD = "sua-senha-aqui"  
3. Executando o Script
Execute o arquivo principal para enviar os e-mails:

bash
Copiar código
python main.py  
📌 Observações
Certifique-se de que sua conta do Gmail está habilitada para envio por aplicativos.
Utilize contas de e-mail seguras para evitar problemas de autenticação.
Para melhorar a segurança, recomenda-se o uso de Google App Passwords em vez da senha principal.
