import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ========================
# Prepare dataset
# ========================
texts = [
    "excellent product with amazing quality",
    "absolutely love this item",
    "fantastic experience overall",
    "highly recommend to everyone",
    "terrible product quality",
    "worst purchase ever made",
    "completely disappointed with item",
    "awful customer service experience",
    "okay shopping experience",
    "average product quality"
]

labels = np.array([
    2, 2, 2, 2, 0, 0, 0, 0, 1, 1
])

# ========================
# Tokenizer
# ========================
tokenizer = Tokenizer(num_words=500, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)

sequences = tokenizer.texts_to_sequences(texts)
padded = pad_sequences(sequences, maxlen=10, padding="post")

# ========================
# Build model
# ========================
model = Sequential([
    Embedding(input_dim=500, output_dim=16, input_length=10),
    GlobalAveragePooling1D(),
    Dense(16, activation="relu"),
    Dense(3, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# ========================
# Train model
# ========================
model.fit(padded, labels, epochs=50, validation_split=0.2)

# ========================
# Save model and tokenizer
# ========================
model.save("sentiment_model.h5")
with open("tokenizer.pickle", "wb") as f:
    pickle.dump(tokenizer, f)

print("Model and tokenizer saved successfully!")
