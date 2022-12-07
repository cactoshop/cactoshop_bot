import json
import re
import respostas_aleatorias

def carrega_json(file):
    with open(file) as respostas_bot:
        print(f"Arquivo {file} carregado.")
        return json.load(respostas_bot)
    
dados_resposta = carrega_json("respostas.json")

def pega_resposta(input_string):
    separa_mensagem = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    lista_score = []
    
    for resposta in dados_resposta:
        resposta_score = 0
        score_requerido = 0
        palavras_requeridas = resposta["palavras_requeridas"]
        
        if palavras_requeridas:
            for palavra in separa_mensagem:
                if palavra in palavras_requeridas:
                    score_requerido += 1
                    
        if score_requerido == len(palavras_requeridas):
            for palavra in separa_mensagem:
                if palavra in resposta["user_input"]:
                    resposta_score += 1
                    
        lista_score.append(resposta_score)
    
    melhor_resposta = max(lista_score)
    index_resposta = lista_score.index(melhor_resposta)
    
    if input_string == "":
        return "Por favor, digite algo para iniciar a conversa."
    
    if melhor_resposta != 0:
        return dados_resposta[index_resposta]["resposta_bot"]
    
    return respostas_aleatorias.random_string()

# while True:
    # user_input = input("vc: ")
    # print("bot:", pega_resposta(user_input))