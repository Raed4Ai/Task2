import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

import nltk

@st.cache_resource
def setup_nltk():
    nltk.download("punkt_tab", quiet=True)
    nltk.download("stopwords", quiet=True)
    nltk.download("wordnet", quiet=True)

setup_nltk()


# Configure the Streamlit page
st.set_page_config(
    page_title="Toxicity Detection System",
    page_icon="🛡️",
    layout="wide"
)


BASE = Path(__file__).parent


def image_to_base64(path):
    """Convert an image file to a base64 data URL."""

    with open(path, "rb") as file:
        return base64.b64encode(file.read()).decode()


safe_image = image_to_base64(BASE / "safe.png")
toxic_image = image_to_base64(BASE / "toxic.png")


# Application background
st.markdown(
    """
    <style>

        /* Main application background */

        .stApp {
            background:
                linear-gradient(
                    135deg,
                    #26343d 0%,
                    #34444f 45%,
                    #59636a 100%
                );
        }


        /* Main content */

        .main {
            background: transparent;
        }


        /* Sidebar */

        [data-testid="stSidebar"] {
            background:
                linear-gradient(
                    180deg,
                    #202b33 0%,
                    #3d484f 100%
                );
        }


        /* Sidebar text */

        [data-testid="stSidebar"] * {
            color: #e8edf0;
        }

    </style>
    """,
    unsafe_allow_html=True
)


components.html(
    f"""
    <!DOCTYPE html>

    <html>

    <head>

        <style>

            html,
            body {{
                margin: 0;
                padding: 0;

                background: transparent;

                overflow: visible;
            }}


            .hero {{

                height: 1000px;

                display: flex;

                justify-content: center;

                align-items: flex-start;

                padding-top: 10px;

                box-sizing: border-box;
            }}


            .title {{

                display: flex;

                flex-direction: column;

                align-items: center;

                gap: 5px;

                font-family: Arial, sans-serif;

                font-weight: 900;

                transform: translateY(-20px);
            }}


            .word-wrapper {{

                position: relative;

                display: inline-block;

                overflow: visible;
            }}


            .word {{

                font-size: 115px;

                line-height: 1.2;

                color: transparent;

                background-size: 200% 100%;

                background-repeat: no-repeat;

                background-clip: text;

                -webkit-background-clip: text;

                -webkit-text-fill-color: transparent;

                overflow: visible;
            }}


            /* Safe image */

            .safe {{

                background-image: url(
                    "data:image/png;base64,{safe_image}"
                );

                background-position: 100% center;

                animation:
                    safeMove 12s linear infinite;
            }}


            /* Toxic image */

            .toxic {{

                position: absolute;

                top: 0;

                left: 0;

                background-image: url(
                    "data:image/png;base64,{toxic_image}"
                );

                background-position: 0% center;

                opacity: 0;

                filter:
                    drop-shadow(0 0 8px red)
                    drop-shadow(0 0 20px red)
                    drop-shadow(0 0 35px red);

                animation:
                    toxicMove 12s linear infinite,
                    toxicSwitch 9s linear infinite;
            }}


            /* Safe image moves right → left */

            @keyframes safeMove {{

                0% {{
                    background-position: 100% center;
                }}

                100% {{
                    background-position: 0% center;
                }}

            }}


            /* Toxic image moves left → right */

            @keyframes toxicMove {{

                0% {{
                    background-position: 0% center;
                }}

                100% {{
                    background-position: 100% center;
                }}

            }}


            /* Toxicity */

            .word-1 .toxic {{
                animation-delay: 0s, 0s;
            }}


            /* Detection */

            .word-2 .toxic {{
                animation-delay: 0s, 3s;
            }}


            /* System */

            .word-3 .toxic {{
                animation-delay: 0s, 6s;
            }}


            /* Toxic word switching */

            @keyframes toxicSwitch {{

                0% {{
                    opacity: 0;
                }}

                5% {{
                    opacity: 1;
                }}

                28% {{
                    opacity: 1;
                }}

                33% {{
                    opacity: 0;
                }}

                100% {{
                    opacity: 0;
                }}

            }}

        </style>

    </head>


    <body>

        <div class="hero">

            <div class="title">

                <div class="word-wrapper word-1">

                    <div class="word safe">
                        Toxicity
                    </div>

                    <div class="word toxic">
                        Toxicity
                    </div>

                </div>


                <div class="word-wrapper word-2">

                    <div class="word safe">
                        Detection
                    </div>

                    <div class="word toxic">
                        Detection
                    </div>

                </div>


                <div class="word-wrapper word-3">

                    <div class="word safe">
                        System
                    </div>

                    <div class="word toxic">
                        System
                    </div>

                </div>

            </div>

        </div>

    </body>

    </html>
    """,
    height=1000,
)
