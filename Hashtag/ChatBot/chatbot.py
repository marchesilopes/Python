import openai

chave_api = "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"

openai.api_key = chave_api

def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )
    
    resposta = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "user", "content": mensagem}
        ],
    )

    return resposta["choices"][0]["message"]

while True:
    texto = input("Escreva aqui sua mensagem: ")
    print(enviar_mensagem("Em que ano Eistein publicou a teoria geral da relatividade?"))

    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        print("Chatbot: ", resposta["content"])