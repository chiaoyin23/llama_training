# llama_training
llm 模型訓練 by autotrain
### 1. 先確認資料夾有裝git ###
```
git init
git rev-parse --git-dir
```
有回傳 .git 表示成功
### 2. 整理資料 ###
```
python convert_data.py
```

### 3. 將參數寫在finetune.py後執行 ###
```
python finetune.py

```


### 4. 修改會出問題的檔案
1.autotrain/cli/run_llm.py
在 __init__ 加上
if isinstance(self.args.block_size, str):
            block_size_split = self.args.block_size.strip().split(",")
        else:
            block_size_split = [self.args.block_size]
在 run 設定
self.args.backend = 'local' 

2.autotrain/trainers/cli/train_clm_sft.py
註解掉
   # trainer_args = dict(
   #    args=args,
   #    model=model,
   #     callbacks=callbacks,
   # )
修改成 args = SFTConfig(**training_args)

3.autotrain/trainers/cli/utils.py
   AutoModelForCausalLM.from_pretrained 去掉 #quantization_config=bnb_config,
