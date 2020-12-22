from simpletransformers.t5 import T5Model
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--checkpoints", "-ckpts", help="checkpoints for t5 base",type = str, default = './best_model')
parser.add_argument("--abstract", "-abs", help="abstract to generate title",type = str)
args = parser.parse_args()

model_args = {
    "reprocess_input_data": True,
    "overwrite_output_dir": True,
    "max_seq_length": 256,
    "eval_batch_size": 128,
    "num_train_epochs": 1,
    "save_eval_checkpoints": False,
    "use_multiprocessing": False,
    "num_beams": None,
    "do_sample": True,
    "max_length": 50,
    "top_k": 50,
    "top_p": 0.95,
    "num_return_sequences": 3,
}

with open(args.abstract) as f:
    data = f.read()

model = T5Model("t5",args.checkpoints, args=model_args,use_cuda=False)
abss =["summarize: "+data]
predicted_title = model.predict(abss)
print(predicted_title)
