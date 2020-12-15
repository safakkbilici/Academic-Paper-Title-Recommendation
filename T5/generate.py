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

model = T5Model("t5","outputs/best_model", args=model_args)

abstr = ["summarize: "+"""Transfer learning, where a model is first pre-trained on a data-rich task before being finetuned  on a downstream task,
has emerged as a powerful technique in natural language processing (NLP).  
The effectiveness of transfer learning has given rise to a diversity of approaches, methodology, and practice. 
In this paper, we explore the landscape of transfer learning techniques for NLP by introducing a unified framework 
that converts all text-based language problems into a text-to-text format. 
Our systematic study compares pre-training objectives, architectures, unlabeled data sets, 
transfer approaches, and other factors on dozens of language understanding tasks. 
By combining the insights from our exploration with scale and our new Colossal Clean Crawled Corpus, we achieve state-of-the-art 
results on many benchmarks covering summarization, question answering, text classification, and more. 
To facilitate future work on transfer learning for NLP, we release our data set, pre-trained models, and code."""]
predicted_title = model.predict(abstr)
print(predicted_title)

