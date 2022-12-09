# cactoshop_bot

## Configurando o bot

##### Requisitos
1. Instalar o Python 3.11.1 + pip 3.11

2. Ativar o ambiente virtual (env)

3. Instalar o flask:
```
pip install flask
```

4. Instalar o pacote do Python Telegram Bot integração com o Telegram:
```
pip install python-telegram-bot
```

5. Rodar o servidor web e subir o bot localmente
```
python3 webapp.py
```
Acessar o endereço https://localhost:5000 no seu navegador.

##### Inicializar o bot
Inicializar o bot separadamente da aplicação web
```
python3 telegram_bot_integration.py
```

É importante ressaltar que para criar um bot no telegram, deve-se seguir a documentação do próprio Telegram, substituindo a chave de API pela que foi gerada pela plataforma.

## Comandos básicos do bot
Para iniciar uma conversa, basta digitar "oi" ou "olá". Para ver o menu principal, digitar "ajuda".
