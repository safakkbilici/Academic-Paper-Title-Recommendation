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


# Tutorial

## Data preparation from scratch

Dowload the [arXiv dataset from Kaggle](https://www.kaggle.com/Cornell-University/arxiv).

Save this in arbitrary path. Then run

```bash
python3 prep_data.py --datapath /path/to/your_json_file.json
```

This script parses your .json file then converts into .csv file, after that it does NLP techniques for abstracts.
After this script, you will have ./data/df_to_model.csv file. You can use it for training from scratch. 

## Seq2Seq LSTM
Seq2Seq LSTM is written with Keras. The summary of model looks like:

    Layer (type)                    Output Shape         Param #     Connected to                     
    ==================================================================================================
    encoder_inputs (InputLayer)     [(None, None)]       0                                            
    __________________________________________________________________________________________________
    encoder_embedding (Embedding)   (None, None, 100)    500200      encoder_inputs[0][0]             
    __________________________________________________________________________________________________
    decoder_inputs (InputLayer)     [(None, None, 2001)] 0                                            
    __________________________________________________________________________________________________
    encoder_lstm (LSTM)             [(None, 100), (None, 80400       encoder_embedding[0][0]          
    __________________________________________________________________________________________________
    decoder_lstm (LSTM)             [(None, None, 100),  840800      decoder_inputs[0][0]             
                                                                     encoder_lstm[0][1]               
                                                                     encoder_lstm[0][2]               
    __________________________________________________________________________________________________
    decoder_dense (Dense)           (None, None, 2001)   202101      decoder_lstm[0][0]               
    ==================================================================================================
    Total params: 1,623,501
    Trainable params: 1,623,501
    Non-trainable params: 0
    __________________________________________________________________________________________________

Additional: Also you can choose your Seq2Seq LSTM summarizer with global vectors for word representation (GloVe).

The Seq2Seq LSTM model can learn wording of academic titles and capture the main topic of the paper, but it cannot specify the title. Results are not sufficient.

### Training from scratch

First extract the .csv file from ./data/df_to_model.tar.gz to ./data folder (or create it from stracth).

Then run the training scripts

```bash
python3 train_lstm.py
```

### Generate titles from checkpoints

./models folder contains checkpoints for specific epochs. Move your .json, .npy and .h5 file into ./modes (default = epoch 100). Then run

```bash
python3 generate_lstm.py --abstract /path/to/your_abstract_file.txt
```

Then the generated title will be saved in ./docs/titles folder.


## T5

The T5 model was presented in [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/pdf/1910.10683.pdf) by Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, Peter J. Liu.

T5 is an encoder-decoder model pre-trained on a multi-task mixture of unsupervised and supervised tasks and for which each task is converted into a text-to-text format. T5 works well on a variety of tasks out-of-the-box by prepending a different prefix to the input corresponding to each task, e.g., for translation: translate English to German, ... for summarization: summarize...

T5 is an encoder-decoder model and converts all NLP problems into a text-to-text format. It is trained using teacher forcing. This means that for training we always need an input sequence and a target sequence.

The prefix can be easily added to csv_to_model file like

```python
train_df['prefix'] = "summarize"
eval_df['prefix'] = "summarize"
```

We trained T5-Base (which has ~220M parameters with 12-layers, 768-hidden-state, 3072 feed-forward hidden-state, 12-heads) on arXiv paper dataset from stractc, using [🤗 Huggingface/transformers](https://github.com/huggingface/transformers) and [Simpletransformers](https://github.com/ThilinaRajapakse/simpletransformers).

Training and generating script for T5 also provided in ./T5 director.


## Data Analysis

We also provided exploratory data analysis scripts for papers in the ./utils directory.

- Top 10 categories
<img src="./docs/img/stats1.png" alt="drawing" width="700"/>

- Distribution Over Category Frequenicies
<img src="./docs/img/stats2.png" alt="drawing" width="700"/>

- Top 10 Popular Categories From 1995 To 2012
<img src="./docs/img/stats3.png" alt="drawing" width="700"/>

- Top 50 Used Words In Abstracts With Word Length > 3
<img src="./docs/img/stats5.png" alt="drawing" width="700"/>

- Word Cloud For Top 100 Words
<img src="./docs/img/stats4.png" alt="drawing" width="700"/>

    TOP 10 AUTHOR BY PUBLICATON:
       B. Aubert: 260
       The BABAR Collaboration: 193
       CLEO Collaboration: 167
       ZEUS Collaboration: 154
       D0 Collaboration: 148
       John Ellis: 140
       Lorenzo Iorio: 138
       R. Horsley: 138
       Cambridge: 136
       CDF Collaboration: 122
       


