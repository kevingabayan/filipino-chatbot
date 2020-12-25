from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('KaiSa',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  database_uri='sqlite:///database.sqlite3')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("./filipino-random-conversations.yml")
trainer.train("./filipino-games.yml")

while True:
    try:
        bot_input = chatbot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
