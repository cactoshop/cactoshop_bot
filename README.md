# cactoshop_bot

## Configurando o bot

###### Requisitos
1. Instalar o Python 3.11.1 + pip 3.11

2. Ativar um ambiente virtual (env)

3. Para subir a aplicação:
3.1 Instalar o flask
```
pip install flask
```

3.2 Rodar o webserver
```
python3 webapp.py
```
Acessar o endereço https://localhost:5000 no seu navegador.

4. Para integração com o Telegram:
4.1 Instalar o pacote do Python Telegram Bot
```
pip install python-telegram-bot
```

4.2 Inicializar o bot
```
python3 telegram_bot_integration.py
```

É importante ressaltar que para criar um bot no telegram, deve-se seguir a documentação do próprio Telegram, substituindo a chave de API pela que foi gerada pela plataforma.

## Comandos básicos do bot
Para iniciar uma conversa, basta digitar "oi" ou "olá". Para ver o menu principal, digitar "ajuda".
