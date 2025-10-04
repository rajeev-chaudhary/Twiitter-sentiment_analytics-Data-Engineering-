import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(page_title="Tweet Stream Dashboard", layout="wide")
st.title("📊 Real-Time Tweet Stream Dashboard")

# Connect DB
conn = sqlite3.connect("tweets.db")

# Load latest tweets
df = pd.read_sql_query("SELECT * FROM tweets ORDER BY timestamp DESC LIMIT 100", conn)

# ---------------------
# 🚨 ALERTING SYSTEM
# ---------------------
if not df.empty:
    recent = df.head(30)  # check last 30 tweets
    neg_ratio = (recent["sentiment"] == 0).mean() * 100
    if neg_ratio > 70:
        st.error(f"🚨 ALERT: {neg_ratio:.1f}% recent tweets are NEGATIVE!")
    else:
        st.success(f"✅ System Normal: Only {neg_ratio:.1f}% negative tweets.")

# ---------------------
# Latest Tweets Section
# ---------------------
st.subheader("📰 Latest Tweets")
for _, row in df.iterrows():
    sentiment = {0: "😡 Negative", 1: "😐 Neutral", 2: "😊 Positive"}[row["sentiment"]]
    st.write(f"**{row['user']}**: {row['text']} ({sentiment})")

# ---------------------
# Sentiment Pie Chart
# ---------------------
st.subheader("📈 Sentiment Distribution")
sent_counts = df["sentiment"].value_counts()
fig, ax = plt.subplots()
ax.pie(sent_counts, labels=[{0:"Negative",1:"Neutral",2:"Positive"}[i] for i in sent_counts.index],
       autopct="%1.1f%%")
st.pyplot(fig)

# ---------------------
# Word Cloud
# ---------------------
st.subheader("☁️ Word Cloud of Tweets")
if not df.empty:
    text = " ".join(df["text"].tolist())
    wc = WordCloud(width=600, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
