import pandas as pd
from simpletransformers.t5 import T5Model
from google.colab import drive
import pandas as pd
drive.mount('/content/drive',force_remount=True)


df = pd.read_csv('/content/drive/My Drive/data/df_to_model.csv')
eval_df = df.sample(frac=0.2, random_state=101)
train_df = df.drop(eval_df.index)


train_df['prefix'] = "summarize"
eval_df['prefix'] = "summarize"

model_args = {
    "reprocess_input_data": True,
    "overwrite_output_dir": True,
    "max_seq_length": 256,
    "train_batch_size": 8,
    "num_train_epochs": 1,
    "save_eval_checkpoints": True,
    "save_steps": -1,
    "use_multiprocessing": False,
    "evaluate_during_training": True,
    "evaluate_during_training_steps": 15000,
    "evaluate_during_training_verbose": True,
    "fp16": False,
    "best_model_dir": "/content/drive/My Drive/outputs/best_model",
    "output_dir": "/content/drive/My Drive/outputs",
    "wandb_project": "Paper Summarization with T5",
}

model = T5Model("t5", "t5-base", args=model_args)
model.train_model(train_df, eval_data=eval_df)

