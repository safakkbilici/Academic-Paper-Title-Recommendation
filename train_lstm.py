from __future__ import print_function

import pandas as pd
from sklearn.model_selection import train_test_split
from lstm_seq2seq.library.utility.plot_utils import plot_and_save_history
from lstm_seq2seq.library.seq2seq import Seq2SeqSummarizer
from lstm_seq2seq.library.applications.fake_news_loader import fit_text
import numpy as np

LOAD_EXISTING_WEIGHTS = True
np.random.seed(170110)
report_dir_path = './reports'
model_dir_path = './models'

df = pd.read_csv('./data/df_to_model.csv')


Y = df['target_text']
X = df['input_text']

config = fit_text(X, Y)

summarizer = Seq2SeqSummarizer(config)

if LOAD_EXISTING_WEIGHTS:
    summarizer.load_weights(weight_file_path=Seq2SeqSummarizer.get_weight_file_path(model_dir_path=model_dir_path))

Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.2, random_state=42)

history = summarizer.fit(Xtrain, Ytrain, Xtest, Ytest, epochs=100)

history_plot_file_path = report_dir_path + '/' + Seq2SeqSummarizer.model_name + '-history.png'
plot_and_save_history(history, summarizer.model_name, history_plot_file_path, metrics={'loss', 'accuracy'})
