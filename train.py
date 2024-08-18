import os

project_name = 'my-autotrain-llm'
model_name = 'taide/TAIDE-LX-7B-Chat'
# data_path ='./llm_training_data.csv'
#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

push_to_hub = False
hf_token = "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"
repo_id = "Enjoyyy/chat_model"  
backend = "local"
# run_llm 修改 bankend + block_size_split

learning_rate = 2e-4
num_epochs = 4
batch_size = 1
block_size = 1024
trainer = "sft"
warmup_ratio = 0.1
weight_decay = 0.01
gradient_accumulation = 4
use_peft = True
lora_r = 16
lora_alpha = 32
lora_dropout = 0.045

cmd = f"autotrain llm --train --project-name {project_name} --model {model_name} " \
      f"--data-path . --lr {learning_rate} --epochs {num_epochs} " \
      f"--batch-size {batch_size} --block-size {block_size} --trainer {trainer} " \
      f"--warmup-ratio {warmup_ratio} --weight-decay {weight_decay} " \
      f"--gradient-accumulation {gradient_accumulation} " \
      f"{'--peft' if use_peft else ''} " \
      f" --lora-r {lora_r} " \
      f"--lora-alpha {lora_alpha} --lora-dropout {lora_dropout}"

os.system(cmd)
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"