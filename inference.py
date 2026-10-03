import json
import re
from pathlib import Path
import numpy as np
import streamlit as st
from tensorflow.keras.layers import TextVectorization
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from model_factory import ModelFactory
from huggingface_hub import hf_hub_download


BASE = Path(__file__).parent


@st.cache_resource
def load_config():
    #Load and cache the model configuration

    with open(BASE / "config.json", encoding="utf-8") as file:
        return json.load(file)


@st.cache_resource
def load_model():
    model_path = hf_hub_download(
        repo_id="read4545/toxic-classifier",
        filename="model.keras"
    )

    return ModelFactory.create_model(model_path)


model = load_model()
cfg = load_config()


vec = TextVectorization(
    max_tokens=30000,
    output_mode="int",
    output_sequence_length=model.input_shape[1],
    vocabulary=cfg["vocabulary"][2:],
)


stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    #Clean and normalize input text before inference

    text = str(text)
    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z\s]"," ",text
        )

    text = re.sub(r"\s+"," ",text).strip()

    words = word_tokenize(text)

    # Remove stopwords and apply lemmatization
    clean_words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]

    return " ".join(clean_words)


def infer(text):
    #Run toxicity prediction on the input text

    text = preprocess_text(text)

    probs = model.predict(vec(np.array([text])),verbose=0)[0]

    result = {label: int(probability >= cfg["threshold"]) for label, probability in zip( cfg["label_cols"], probs)}

    return result

