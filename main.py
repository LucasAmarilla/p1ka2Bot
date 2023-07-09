import telebot
from dotenv import load_dotenv
import os

load_dotenv()
KEY = os.getenv('TOKEN')
bot = telebot.TeleBot(KEY)

@bot.message_handler(commands=["imagemFoda"])
def imgFoda(msg):
    bot.send_photo(msg.chat.id, photo=(open("assets/mine.jpg", 'rb')))

@bot.message_handler(commands=["musicaFoda"])
def musicaFoda(msg):
    bot.send_audio(msg.chat.id, audio=open("assets/monster.mp3", 'rb'))

@bot.message_handler(commands=["textoMotivacional"])
def txtMoti(msg):
    txt = """
    
    Motivação para a vida

    Talvez você esteja preocupado(a) demais,
    desanimado com essa ou aquela situação.
    Vivendo sob grande tensão.
    Sem saber por onde ir ou como fazer.
    Pois vou lhe dar alguns motivos para melhorar.
    mesmo sem grandes recursos financeiros,
    mesmo sem médico, sem analista e sem dor.
    """
    bot.send_message(msg.chat.id, txt)

@bot.message_handler(commands=['all'])
def handle_alex(msg):
    bot.reply_to(msg, "Executando todas as três funções...")
    imgFoda(msg)
    musicaFoda(msg)
    txtMoti(msg)

def verificar (msg):
    return True

@bot.message_handler(func = verificar)
def responder(msg):
    txt = """\n
    Bem vindo ao pika bot, aqui temos as seguites coisas(Clique em alguma):\n
    /musicaFoda(vai mandar a musica da semana)
    /imagemFoda(vai mandar uma imagem do dia)
    /textoMotivacional(vai mandar um texto motivacional)
    /all (vai mandar todos)

    Responder qualquer outra coisa não vai funcaionar
    """
    bot.reply_to(msg, txt)


bot.polling()