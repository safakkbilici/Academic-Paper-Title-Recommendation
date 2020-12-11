# Academic Paper Title Recommendation

## Data preparation from scratch

Dowload the [arXiv dataset from Kaggle](https://www.kaggle.com/Cornell-University/arxiv).

Save this in arbitrary path. Then run

```bash
python3 prep_data.py --datapath /path/to/your_json_file.json
```

This script parses your .json file then converts into .csv file, after that it does NLP techniques for abstracts.

After this script, you will have ./data/df_to_model.csv file. You can use it for training from scratch. 

## Training from scratch

First extract the .csv file from ./data/df_to_model.tar.gz to ./data folder

Then run the training scripts

```bash
python3 train_lstm
```
