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
python3 train_lstm.py
```

## Generate titles from checkpoints

./models folder contains checkpoints for specific epochs. Move your .json, .npy and .h5 file into ./modes (default = epoch 100). Then run

```bash
python3 generate_lstm.py --abstract /path/to/your_abstract_file.txt
```

Then the generated title will be saved in ./docs/titles folder.
