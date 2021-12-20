from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
iacsd_bot = ChatBot(
    'Iacsdbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
) 
chatbot = open('D:\machine learning\chatbot_iacsd\chatbot.txt').read().splitlines()
personal = open('D:\machine learning\chatbot_iacsd\personal.txt').read().splitlines()
training_data = chatbot+personal
trainer = ListTrainer(iacsd_bot)
trainer.train(training_data)
trainer_corpus = ChatterBotCorpusTrainer(iacsd_bot)
trainer_corpus.train(
    'chatterbot.corpus.english'
)
