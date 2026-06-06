<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sentiment Analysis Web App</title>

<style>
    body{
        font-family: 'Segoe UI', sans-serif;
        background:#f4f7fc;
        margin:0;
        padding:0;
        color:#333;
    }

    .container{
        width:85%;
        margin:auto;
        padding:40px 0;
    }

    .hero{
        background:linear-gradient(135deg,#2563eb,#1e40af);
        color:white;
        padding:60px;
        border-radius:20px;
        text-align:center;
        box-shadow:0 10px 30px rgba(0,0,0,0.15);
    }

    .hero h1{
        font-size:42px;
        margin-bottom:15px;
    }

    .hero p{
        font-size:18px;
        max-width:800px;
        margin:auto;
    }

    .section{
        background:white;
        margin-top:30px;
        padding:30px;
        border-radius:15px;
        box-shadow:0 5px 15px rgba(0,0,0,0.08);
    }

    h2{
        color:#2563eb;
        margin-bottom:15px;
    }

    ul{
        padding-left:20px;
    }

    li{
        margin-bottom:10px;
    }

    .tech{
        display:flex;
        flex-wrap:wrap;
        gap:12px;
    }

    .tag{
        background:#2563eb;
        color:white;
        padding:10px 18px;
        border-radius:25px;
        font-size:14px;
    }

    .footer{
        text-align:center;
        margin-top:40px;
        color:#666;
    }
</style>
</head>

<body>

<div class="container">

   <div class="hero">
        <h1>Sentiment Analysis Web Application</h1>
        <p>
            An NLP-powered web application developed using TensorFlow, Keras, and Streamlit 
            that classifies user text into Positive, Neutral, or Negative sentiments with confidence scores.
            This project demonstrates the complete machine learning workflow from text preprocessing 
            and model training to deployment through an interactive web interface.
        </p>
    </div>

   <div class="section">
        <h2>📌 Project Overview</h2>
        <p>
            The Sentiment Analysis Web App leverages Natural Language Processing (NLP) and
            Deep Learning techniques to analyze textual input and determine its emotional tone.
            The application uses an LSTM-based neural network model trained on labeled sentiment data
            and deployed through Streamlit for real-time predictions.
        </p>
    </div>

   <div class="section">
        <h2>✨ Key Features</h2>
        <ul>
            <li>Real-time sentiment prediction from user text input.</li>
            <li>Classifies text into Positive, Neutral, or Negative categories.</li>
            <li>Displays prediction confidence scores.</li>
            <li>Simple, responsive, and user-friendly interface.</li>
            <li>Fast inference using a trained TensorFlow model.</li>
        </ul>
    </div>

   <div class="section">
        <h2>🛠 Technology Stack</h2>

  <div class="tech">
            <span class="tag">Python</span>
            <span class="tag">TensorFlow</span>
            <span class="tag">Keras</span>
            <span class="tag">NumPy</span>
            <span class="tag">Streamlit</span>
            <span class="tag">Pickle</span>
            <span class="tag">NLP</span>
            <span class="tag">LSTM</span>
        </div>
    </div>

   <div class="section">
        <h2>⚙️ Project Workflow</h2>
        <ol>
            <li>Text preprocessing and tokenization using Keras Tokenizer.</li>
            <li>Sequence padding to maintain fixed input length.</li>
            <li>Feature extraction through Embedding Layer.</li>
            <li>Sentiment learning using LSTM Neural Network.</li>
            <li>Classification through Dense Softmax Output Layer.</li>
            <li>Deployment using Streamlit Web Framework.</li>
        </ol>
    </div>

  <div class="section">
        <h2>📂 Project Structure</h2>

<pre>
├── train_model.py
├── app.py
├── sentiment_model.h5
├── tokenizer.pickle
├── README.md
</pre>

  </div>

  <div class="section">
        <h2>📊 Sentiment Classes</h2>
        <ul>
            <li><strong>0 → Negative</strong></li>
            <li><strong>1 → Neutral</strong></li>
            <li><strong>2 → Positive</strong></li>
        </ul>
    </div>
    <div class="section">
        <h2>🎯 Learning Outcomes</h2>
        <ul>
            <li>Natural Language Processing fundamentals.</li>
            <li>Text preprocessing and tokenization techniques.</li>
            <li>Deep Learning using LSTM networks.</li>
            <li>Model saving and loading techniques.</li>
            <li>Deploying Machine Learning applications using Streamlit.</li>
        </ul>
    </div>
    <div class="section">
        <h2>🚀 Future Enhancements</h2>
        <ul>
            <li>Train on larger and more diverse datasets.</li>
            <li>Improve model accuracy and generalization.</li>
            <li>Enhance UI/UX with modern design components.</li>
            <li>Deploy on cloud platforms for public access.</li>
            <li>Add multilingual sentiment analysis support.</li>
        </ul>
    </div>
    <div class="footer">
        <h3>Developed By</h3>
        <p><strong>Jitesh Yadav</strong> | Data Analyst & Aspiring Data Scientist</p>
    </div>

</div>

</body>
</html>
