# Academic Paper Title Recommendation

Recommended repository names based on README:

    [['Using Language-Based Summarization Methods',
      'A New Method for Language Modeling',
      'The Supervised Summarization Model']]

Sequence to sequence Natural Processing Language tasks are progressing rapidly. They can used for Language Modeling, Machine Translation, Question Answering, and **Summarization**.

In this project, our aim is to create a supervised summarization model that generates titles from academic papers (their abstracts). Paper titles are exiciting section of papers, some of them relevent with paper content, some of them are not (e.g Attention Is All You Need). Titles motivate people to read the papers, have a big role on accepted submission to conferences. Maybe it can help people write more creative titles.

We have trained 2 models (yet).

- Seq2Seq LSTM (baseline)
- T5 Base (best results)

## About The Data

We use arXiv as a source for paper [dataset](https://www.kaggle.com/Cornell-University/arxiv). arXiv is a open pre-print and e-print website for papers and free.

This dataset is in .json format, we provided scripts for parsing data. Also tokenization and other preprocessing scripts are provided, they are explained in tutorial section.

The cleaned, parsed and tokenized version of data is provided in ./data folder as compressed.

A sample example from json data:

    Title: Sparsity-certifying Graph Decompositions 

    Abstract:   We describe a new algorithm, the $(k,\ell)$-pebble game with colors, and use
    it obtain a characterization of the family of $(k,\ell)$-sparse graphs and
    algorithmic solutions to a family of problems concerning tree decompositions of
    graphs. Special instances of sparse graphs appear in rigidity theory and have
    received increased attention in recent years. In particular, our colored
    pebbles generalize and strengthen the previous results of Lee and Streinu and
    give a new proof of the Tutte-Nash-Williams characterization of arboricity. We
    also present a new decomposition that certifies sparsity based on the
    $(k,\ell)$-pebble game with colors. Our work also exposes connections between
    pebble game algorithms and previous sparse graph algorithms by Gabow, Gabow and
    Westermann and Hendrickson.

    Ref: None 
    Categories: 
    Authors: math.CO cs.CG
    Authors Parsed: Ileana Streinu and Louis Theran

## Data Analysis

We also provided exploratory data analysis scripts for papers in the ./utils directory.

<img src="./docs/img/stats1.png" alt="drawing" width="800"/>


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
