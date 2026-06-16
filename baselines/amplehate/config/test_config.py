datatype = "White"
dataset = ["/data/chenjt/Datasets/White/stg1_pure"]
model_path = ["White/seed_1/lambda_0.75"]

tuning_param  = ["learning_rate","train_batch_size","eval_batch_size","nepoch","SEED","dataset","model_path"] ## list of possible paramters to be tuned

train_batch_size = [16]
eval_batch_size = [16]
hidden_size = 768
nepoch = [6]    
learning_rate = [2e-5]

model_type = "/data/public_model/bert-base-uncased"
SEED = [1]
e = 0.75
param = {"e":e, "dataset":dataset,"model_path":model_path,"learning_rate":learning_rate,"train_batch_size":train_batch_size,"eval_batch_size":eval_batch_size,"hidden_size":hidden_size,"nepoch":nepoch,"dataset":dataset, "SEED":SEED,"model_type":model_type,"datatype":datatype}
