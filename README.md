# Twiitter-sentiment_analytics-Data-Engineering-
Twitter Data Streaming Pipeline (Lightweight Version)


📌 Components

Data Source → HuggingFace "tweet_eval" dataset (real tweets)

Streaming Simulation → Python generator emits 1 tweet per second

Storage Layer → SQLite (light, no heavy DB)

Dashboard → Streamlit for live tweets + sentiment analysis

1. Install Dependencies

Run once:

pip install datasets streamlit matplotlib wordcloud pandas


Run the Project

Start tweet stream storage:

python store_tweets.py


(this keeps inserting tweets in tweets.db)

In another terminal, start dashboard:

streamlit run dashboard.py
