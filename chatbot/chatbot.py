from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('TW Chat Bot')

conversa = ['Oi', 'Olá', 'Bom dia?','Bom dia', 'Tudo bem?',  'Tudo ótimo', 'Quero pesquisar um processo', 'Qual o número do processo?', '8181818', 'Seu processo está na na 3ª Turma']

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('TW Bot: ', resposta)
    else:
        print('TW Bot: Ainda não sei responder esta pergunta')