import tensorflow as tf
import streamlit as st

class ModelFactory:

    @staticmethod
    @st.cache_resource
    def create_model(model_path):

        #Load and cache a TensorFlow model.
        return tf.keras.models.load_model(
            model_path,
            compile=False
        )

