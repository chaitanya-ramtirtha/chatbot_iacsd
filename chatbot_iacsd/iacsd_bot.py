{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [],
   "source": [
    "from chatterbot import ChatBot\n",
    "from chatterbot.trainers import ListTrainer\n",
    "from chatterbot.trainers import ChatterBotCorpusTrainer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [],
   "source": [
    "iacsd_bot = ChatBot(\n",
    "    'Iacsdbot',\n",
    "    storage_adapter='chatterbot.storage.SQLStorageAdapter',\n",
    "    logic_adapters=[\n",
    "        'chatterbot.logic.MathematicalEvaluation',\n",
    "        'chatterbot.logic.TimeLogicAdapter',\n",
    "        'chatterbot.logic.BestMatch',\n",
    "        {\n",
    "            'import_path': 'chatterbot.logic.BestMatch',\n",
    "            'default_response': 'I am sorry, but I do not understand. I am still learning.',\n",
    "            'maximum_similarity_threshold': 0.90\n",
    "        }\n",
    "    ],\n",
    "    database_uri='sqlite:///database.sqlite3'\n",
    ") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [],
   "source": [
    "chatbot = open('D:\\machine learning\\chatbot_iacsd\\chatbot.txt').read().splitlines()\n",
    "personal = open('D:\\machine learning\\chatbot_iacsd\\personal.txt').read().splitlines()\n",
    "training_data = chatbot+personal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "List Trainer: [####################] 100%\n"
     ]
    }
   ],
   "source": [
    "trainer = ListTrainer(iacsd_bot)\n",
    "trainer.train(training_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training ai.yml: [####################] 100%\n",
      "Training botprofile.yml: [####################] 100%\n",
      "Training computers.yml: [####################] 100%\n",
      "Training conversations.yml: [####################] 100%\n",
      "Training emotion.yml: [####################] 100%\n",
      "Training food.yml: [####################] 100%\n",
      "Training gossip.yml: [####################] 100%\n",
      "Training greetings.yml: [####################] 100%\n",
      "Training health.yml: [####################] 100%\n",
      "Training history.yml: [####################] 100%\n",
      "Training humor.yml: [####################] 100%\n",
      "Training literature.yml: [####################] 100%\n",
      "Training money.yml: [####################] 100%\n",
      "Training movies.yml: [####################] 100%\n",
      "Training politics.yml: [####################] 100%\n",
      "Training psychology.yml: [####################] 100%\n",
      "Training science.yml: [####################] 100%\n",
      "Training sports.yml: [####################] 100%\n",
      "Training trivia.yml: [####################] 100%\n"
     ]
    }
   ],
   "source": [
    "trainer_corpus = ChatterBotCorpusTrainer(iacsd_bot)\n",
    "trainer_corpus.train(\n",
    "    'chatterbot.corpus.english'\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
