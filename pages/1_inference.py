import streamlit as st
import streamlit.components.v1 as components
import time


st.set_page_config(
    page_title="Inference",
    page_icon="🔍"
)



st.markdown(
    """
    <style>

        .stApp {
            background:
                linear-gradient(
                    135deg,
                    #26343d 0%,
                    #34444f 45%,
                    #59636a 100%
                );
        }

        .main {
            background: transparent;
        }

        [data-testid="stSidebar"] {
            background:
                linear-gradient(
                    180deg,
                    #202b33 0%,
                    #3d484f 100%
                );
        }

        [data-testid="stSidebar"] * {
            color: #e8edf0;
        }

        [data-testid="InputInstructions"] {
            display: none;
        }

    </style>
    """,
    unsafe_allow_html=True
)


# Loading Screen

if "inference_loaded" not in st.session_state:

    loading = st.empty()

    with loading.container():

        components.html(
            """
            <!DOCTYPE html>
            <html>
            <head>
                <style>

                    html, body {
                        margin: 0;
                        padding: 0;
                        background: transparent;
                    }

                    .loading {
                        height: 70vh;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        text-align: center;
                        font-family: Arial, sans-serif;
                    }

                    .title {
                        font-size: 42px;
                        font-weight: 900;
                        color: #e8edf0;
                        margin-bottom: 15px;
                    }

                    .subtitle {
                        font-size: 28px;
                        font-weight: 700;
                        color: #b8c3c9;
                    }

                </style>
            </head>

            <body>

                <div class="loading">

                    <div class="title">
                        Getting things ready for you
                    </div>

                    <div class="subtitle">
                        Please wait......
                    </div>

                </div>

            </body>
            </html>
            """,
            height=600,
            scrolling=False
        )

    time.sleep(0.5)




from result_repository import ResultRepository
from PIL import Image
from imagecaption import createimagecaption
import inference


# Finish Loading


if "inference_loaded" not in st.session_state:

    st.session_state.inference_loaded = True

    loading.empty()




# Initialize the repository for storing prediction results
repository = ResultRepository("database.db")



st.title("inference")




tab1,tab2=st.tabs(["Text","Image"])

# inference text
with tab1:
        text = st.text_input("Enter your text here:")
        if st.button("Predict"):
          if text: 
                with st.spinner("Loading.."):
                   result=inference.infer(text)
                   repository.save(text, result)
                st.write(result)

# inference image        
with tab2:
         uploaded_file = st.file_uploader(
        "Upload an image",
         type=["jpg", "jpeg", "png"]
                 )
         if st.button("Predict", key="image_predict"):
                if uploaded_file is not None:
                        image = Image.open(uploaded_file).convert("RGB")
                        st.image(image, caption="Uploaded Image")
                        st.write("please wait")
                        imcaption=createimagecaption(image)
                        st.subheader("Generated Caption")
                        st.write(imcaption)
                        result=inference.infer(imcaption)
                        repository.save(imcaption, result)
                        st.write(result)

                


