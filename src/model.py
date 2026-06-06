import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle

# ========================
# Load model and tokenizer
# ========================
model = load_model("sentiment_model.h5")
with open("tokenizer.pickle", "rb") as f:
    tokenizer = pickle.load(f)

# ========================
# Streamlit UI
# ========================
st.title("Sentiment Analysis Web App")

user_input = st.text_area("Enter your text for sentiment analysis:")
submit_button = st.button("Analyze Sentiment")

# ========================
# Predict sentiment
# ========================
if submit_button and user_input:
    sequence = tokenizer.texts_to_sequences([user_input])
    padded_sequence = pad_sequences(sequence, maxlen=10, padding="post", truncating="post")

    prediction = model.predict(padded_sequence)
    predicted_class = np.argmax(prediction, axis=1)[0]

    sentiment_labels = {0: "Negative", 1: "Neutral", 2: "Positive"}
    predicted_sentiment = sentiment_labels[predicted_class]

    confidence = prediction[0][predicted_class]

    if predicted_sentiment == "Positive":
        st.success(f"Sentiment: {predicted_sentiment} ({confidence*100:.2f}%)")
    elif predicted_sentiment == "Neutral":
        st.warning(f"Sentiment: {predicted_sentiment} ({confidence*100:.2f}%)")
    else:
        st.error(f"Sentiment: {predicted_sentiment} ({confidence*100:.2f}%)")
