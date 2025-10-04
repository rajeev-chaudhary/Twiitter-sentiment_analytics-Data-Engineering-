from datasets import load_dataset
import time, random

# Load dataset from HuggingFace
dataset = load_dataset("tweet_eval", "sentiment")
tweets = dataset["train"]

def get_stream():
    while True:
        sample = random.choice(tweets)
        yield {
            "user": f"user_{random.randint(1, 5000)}",
            "text": sample["text"],
            "sentiment": sample["label"]  # 0 = negative, 1 = neutral, 2 = positive
        }
        time.sleep(1)  # new tweet every sec
