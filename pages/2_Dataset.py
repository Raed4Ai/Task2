import streamlit as st

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

    </style>
    """,
    unsafe_allow_html=True
)


from result_repository import ResultRepository

# Initialize the repository for storing prediction results
repository = ResultRepository("database.db")


st.title("Dataset")


df = repository.get_all()

st.dataframe(
    df,
    use_container_width=True
)
