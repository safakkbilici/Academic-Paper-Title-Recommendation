from process.abs_tokenizer_1 import absTokenizer1
from helpers.json_parser import json2list
import pandas as pd

def df2model(path_to_json):
    data = json2list(path_to_json)

    df_to_model = pd.DataFrame({
        'Abstracts'  : absTokenizer1(r'\w+', data['abstracts']),
        'Titles'     : data['titles']
    })

    df_to_model.columns = ['input_text', 'target_text']

    for i in range(len(df_to_model)):
        df_to_model.iloc[i,0] = ' '.join(df_to_model.iloc[i,0])

    print('df_to_model.csv is prepared...')
    return df_to_model
