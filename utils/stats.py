import collections
import pandas as pd
from itertools import islice
import json
import matplotlib.pyplot as plt
	
def getCategoryVocab(df_raw):
    df_raw = pd.read_csv(df_raw)
    category_vocab = [item for sublist in (category.split(' ') for category in df_raw['Category']) for item in sublist]
    return category_vocab

def getCategoryVocabByYear(df_raw):
    df_raw = pd.read_csv(df_raw)
    category_year_vocab = []
    pair = []
    for i in range(len(df_raw)):
        splitted = df_raw.iloc[i,-1].split(' ')
        for splits in splitted:
            pair.append(splits)
            pair.append(df_raw.iloc[i,-2])
            pair = []
            category_year_vocab.append(pair)
    return category_year_vocab

def countCategoryVocabByYear(category_vocab_by_year):
    count = collections.defaultdict(dict)
    i = 0
    for pair in category_vocab_by_year:
        try:
            count[str(pair[1])][pair[0]] = 0
        except Exception as e:
            if e is IndexError:
                print('This exception is not possible. But it happens.')
    for pair in category_vocab_by_year:
        try:
            count[str(pair[1])][pair[0]] += 1
        except Exception as e:
            if e is IndexError:
                print('This exception is not possible. But it happens.')
    return count

def countCategories(category_vocab,k):
    countCat = collections.defaultdict(int)
    for cat in category_vocab:
        countCat[cat] += 1
    return dict(islice(collections.OrderedDict(countCat).items(), k))

def populars(df_csv_raw, k=10):
    df_raw = pd.read_csv(df_csv_raw)
    category_vocab = getCategoryVocab(df_csv_raw)
    topk = countCategories(category_vocab,10)
    print("TOP 10 CATEGORY BY POPULARITY")
    for key, value in topk.items():
        print("  {}: {}".format(key,value))

def popularsbar(df_csv_raw,k):
    df_raw = pd.read_csv(df_csv_raw)
    category_vocab = getCategoryVocab(df_csv_raw)
    topk = countCategories(category_vocab,k)
    cat_dir = '../data/categories.json'
    with open(cat_dir) as json_file:
        categories = json.load(json_file)
    legends = []
    for a in list(topk.keys()):
        if a in categories:
            legends.append(categories[a])
    plt.figure(num=None, figsize=(13, 7), dpi=80, facecolor='w', edgecolor='k')
    plt.bar(legends,list(topk.values()))
    #plt.rcParams['xtick.labelsize'] = small
    plt.tight_layout()
    plt.xticks(rotation='vertical')
    plt.xlabel("categories")
    plt.ylabel("Count")
    plt.title("Top 10 Categories")
    plt.show()
