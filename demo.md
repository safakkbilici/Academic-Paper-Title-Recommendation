#HOW TO BUILD?

- You are supposed to have a Conda and pip. If not, then please download:
    
[Install conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
[Install pip](https://pip.pypa.io/en/stable/reference/pip_install/)


- After installing conda, you need to create a new virtual environment to make a balance within dependencies. Please run this commands on a shell in order:

```bash
conda create -n simpletransformers python pandas tqdm python=3.7
conda activate simpletransformers
conda install pytorch cudatoolkit=11.0 -c pytorch
pip install simpletransformers
conda install -c conda-forge keras
conda install -c conda-forge h5py=2.10.0
conda install -c anaconda flask
```


- Now, you are done with dependencies. The github repo that you have installed contains only for seq2seq LSTM checkpoints. Not T5. We used seq2seq LSTM as a baseline model. T5 results state-of-the-art.

- Please download all files in this [drive link](https://drive.google.com/drive/folders/1-sKu2k3JHEo5F6OQXzM0HlNzrojau-Z1?usp=sharing)

- Extract the compressed file into the main folder of project.

- You must have now a folder called "checkpoint-15982-epoch-1". The file tree structure is then:

- checkpoint-15982-epoch-1
  * training_args.bin
  * tokenizer_config.json
  * spiece.model
  * special_tokens_map.json
  * scheduler.pt
  * pytorch_model.bin
  * optimizer.pt
  * model_args.json
  * eval_results.txt
  * config.json

- This "checkpoint-15982-epoch-1" file must be in same directory with app.py, generate.py, request.py

- After running $ls command the output must be look like this

  * app.py
  * crawler
  * generate_lstm.py
  * generate.py
  * helpers
  * lstm_seq2seq
  * models
  * prep_data.py
  * process
  * request.py
  * requirements.sh
  * static
  * T5
  * templates
  * train_lstm.py
  * utils
  * readme.txt
  * docs

- Now you are ready to play! Run this commands to start the demo web page on local:

```bash
conda activate simpletransformers
python3 app.py
```

- Open up the browser and go to http://127.0.0.1:5000/ (i think this url is constant, however it might be different in other machines. After running the command you can see your local url address, just open this url)


- We provide you to some abstracts to get a recommendation based on those. This abstracts in docs directory.

- Copy a paper abstract and paste it to T5 input section or lstm input section (T5 is SotA).
  
- Press the button! (T5 is relatively slow to predict, about 10 seconds).
