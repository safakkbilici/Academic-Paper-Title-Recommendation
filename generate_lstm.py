from __future__ import print_function

import pandas as pd
from sklearn.model_selection import train_test_split
from lstm_seq2seq.library.utility.plot_utils import plot_and_save_history
from lstm_seq2seq.library.seq2seq import Seq2SeqSummarizer
import numpy as np

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--abstract", "-a", help="path to you abstract.txt",type = str)
args = parser.parse_args()

np.random.seed(170110)
data_dir_path = './data'
model_dir_path = './models'

config = np.load(Seq2SeqSummarizer.get_config_file_path(model_dir_path=model_dir_path),allow_pickle=True).item()

summarizer = Seq2SeqSummarizer(config)
summarizer.load_weights(weight_file_path=Seq2SeqSummarizer.get_weight_file_path(model_dir_path=model_dir_path))

with open(args.abstract) as f:
    data = f.read()
headline = summarizer.summarize(data)

print('Generated Tile: ')
print(headline)

with open("title_"+args.abstract,"w") as output:
    print('{}'.format(headline), file=output)




