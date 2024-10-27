from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
import torch
from torch.utils.data import Dataset
import pandas as pd
import random

# Define the dataset class
class ChatDataset(Dataset):
    def __init__(self, data):
        self.data = data
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        chat = self.data.iloc[idx]
        input_text = "Chat: " + " ".join(eval(chat["Messages"])) + " Output: "
        mcq_text = "MCQ: " + chat["MCQ"] + " Correct Answer: " + chat["Correct Answer"] + " Distractors: " + ", ".join(eval(chat["Distractors"]))
        article_text = "Article: " + chat["Article"]
        output_text = mcq_text if random.random() > 0.5 else article_text
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt').squeeze()
        output_ids = self.tokenizer.encode(output_text, return_tensors='pt').squeeze()
        return input_ids, output_ids

# Load the dataset
df = pd.read_csv("chat_mcq_article_dataset.csv")

# Prepare the dataset
train_dataset = ChatDataset(df)

# Load the model
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Define the training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
)

# Define the trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
)

# Train the model
trainer.train()

# Save the model
model.save_pretrained("fine_tuned_gpt2")
