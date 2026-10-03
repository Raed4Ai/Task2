# Toxic Text Classification

an end-to-end text classification system for detecting toxic content using Deep Learning and NLP techniques.

## Overview


the system take the user input text or uploaded image (after make image captioning) then do inference using LSTM model, and save the result in dataset.




This project uses an LSTM-based neural network to classify text into six toxicity categories:

* Toxic
* Severe Toxic
* Obscene
* Threat
* Insult
* Identity Hate





## Technologies

* Python
* TensorFlow / Keras
* NLTK
* NumPy
* Pandas
* Streamlit
*sqlite3
*Blip2

## Model

The model uses:

* Text preprocessing
* Text Vectorization
* Embedding layer
* Bidirectional LSTM
* Dropout
* Dense output layer
* Class-weighted Binary Cross-Entropy to handle class imbalance



## How to Run

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run main.py
```

## Results

Macro F1:   0.9564
Micro F1:   0.9510
Weighted F1: 0.9508

## Purpose

This project was developed as part of NLP and Machine Learning training at Cellula Tech.
