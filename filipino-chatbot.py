from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Kaisa',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  database_uri='sqlite:///database.sqlite3')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("./filipino-random-conversations.yml")
# trainer.train("./filipino-games.yml") Unfinished
while True:
    try:
        print("User: ")
        bot_input = chatbot.get_response(input())
        print("Bot: ")
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
