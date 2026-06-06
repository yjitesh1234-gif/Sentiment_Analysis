Sentiment Analysis Web App -

This is a simple Sentiment Analysis web application built using TensorFlow, Keras, and Streamlit.
The app predicts whether a given text is Positive, Negative, or Neutral.
I built this project to understand how NLP models work and how to deploy them using Streamlit.

Features -

Takes user text input
Predicts sentiment (Positive / Neutral / Negative)
Shows prediction confidence
Simple and clean UI using Streamlit

Tech Stack -

Python

TensorFlow / Keras

NumPy
Streamlit
Pickle

Project Structure -
├── train_model.py
├── app.py
├── sentiment_model.h5
├── tokenizer.pickle
├── README.md
How It Works -
Text data is tokenized using Keras Tokenizer.
Sequences are padded to fixed length.

Model uses:

Embedding Layer
LSTM Layer
Dense Output Layer (Softmax)
Output gives probability for 3 classes:

0 → Negative
1 → Neutral
2 → Positive

How To Run The Project
  Install Dependencies
pip install tensorflow streamlit numpy
  Train the Model
python train_model.py
  Run the Web App
streamlit run app.py
  What I Learned

Basics of NLP preprocessing
How tokenization works
How LSTM models process text
Saving and loading trained models
Deploying ML models using Streamlit

Future Improvements -

Train model on larger dataset
Improve accuracy
Add better UI design
Deploy online

Author -
Shreyas Dhomase
