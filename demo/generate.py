import os
#os.system("conda activate simpletransformers3")

def recommend(abstract: str):
    from simpletransformers.t5 import T5Model
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
    model = T5Model("t5","./checkpoint_15000_1", args=model_args,use_cuda=False)
    abss =["summarize: "+abstract]
    predicted_title = model.predict(abss)
    return predicted_title
