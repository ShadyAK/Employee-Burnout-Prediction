import openai 
import pandas as pd 
from transformers import GPT2TokenizerFast
#Line 58
openai.api_key = 'sk-gTVWLHKHVvioYsvpcVh5QbJHANf8xT9f9fzDkWU4'

#a = openai.File.create(file=open("models_and_pipelines/gpt-3/train.jsonl"), purpose="classifications")
#print(a)


# Load the tokenizer.
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

# Make sure the labels are formatted correctly.
labels = ["Negative",'Neutral',"Positive"]
labels = [label.strip().lower().capitalize() for label in labels]

# Encode the labels with extra white space prepended.
labels_tokens = {label: tokenizer.encode(" " + label) for label in labels}



import numpy as np

# Take the starting tokens for probability estimation.
# Labels should have distinct starting tokens.
# Here tokens are case-sensitive.
first_token_to_label = {tokens[0]: label for label, tokens in labels_tokens.items()}
def return_feedback(texts):
    feedback = []

    for i in range(len(texts)):
        result = openai.Classification.create(
            file="file-UYNRK0BBMP1QOsyxc3bvrLgT",
            query=texts[i],
            search_model="ada",
            model="curie",
            max_examples=10,
            labels=labels,
            logprobs=3,  # Here we set it to be len(labels) + 1, but it can be larger.
            expand=["completion"],
        )
        top_logprobs = result["completion"]["choices"][0]["logprobs"]["top_logprobs"][0]
        token_probs = {
            tokenizer.encode(token)[0]: np.exp(logp) 
            for token, logp in top_logprobs.items()
        }
        label_probs = {
            first_token_to_label[token]: prob 
            for token, prob in token_probs.items()
            if token in first_token_to_label
        }

    # Fill in the probability for the special "Unknown" label.
        if sum(label_probs.values()) < 1.0:
            label_probs["Unknown"] = 1.0 - sum(label_probs.values())
        idx = 0 
        values = list(label_probs.values())
        max_val = max(values) 
        for i in range(len(values)):
            if values[i] == max_val:
                break 
        feedback.append(list(label_probs.keys())[i])

    return feedback