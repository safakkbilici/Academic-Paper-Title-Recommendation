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

model = T5Model("t5","./best_model", args=model_args,use_cuda=False)
abss =["summarize: "+"""How can we perform efficient inference and learning in directed probabilistic models, 
in the presence of continuous latent variables with intractable posterior distributions, and large datasets? 
We introduce a stochastic variational inference and learning algorithm that scales to large datasets and, under some mild differentiability conditions, 
even works in the intractable case. Our contributions is two-fold. 
First, we show that a reparameterization of the variational lower bound yields a lower bound estimator that can be straightforwardly 
optimized using standard stochastic gradient methods. Second, we show that for i.i.d. datasets with continuous latent variables per datapoint, 
posterior inference can be made especially efficient by fitting an approximate inference model (also called a recognition model) 
to the intractable posterior using the proposed lower bound estimator. Theoretical advantages are reflected in experimental results."""]
predicted_title = model.predict(abss)
print(predicted_title)
