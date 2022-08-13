from cProfile import label
import telebot

BANED = [1342579234]

class TelebotHandler():
    def __init__(self, token:str or None) -> None:
        try:
                
            self.__bot = telebot.TeleBot(token, parse_mode=None)
            
            @self.__bot.message_handler(func=lambda m: True)#@self.__bot.message_handler(lambda message: True)
            def get_feed(message):
                #print(message.chat.id)
                if is_allowed(message.chat.id):
                    print(message.chat.id)
                    
            @staticmethod
            def is_allowed(chat_id):
                return chat_id not in BANED
        except:
            pass
        
    def start_bot(self)->None:
        self.__bot.infinity_polling()
    
'''
import telebot

bot = telebot.TeleBot("YOUR_BOT_TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
'''