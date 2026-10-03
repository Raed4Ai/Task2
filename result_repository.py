import sqlite3
import pandas as pd


class ResultRepository:
    #Repository for storing and retrieving toxicity results

    def __init__(self, database_path):
        self.database_path = database_path

    def save(self, text, result):
        #Save a prediction result

        with sqlite3.connect(self.database_path) as connection:

            connection.execute(
                """
                INSERT INTO results
                ( text,toxic,severe_toxic,obscene,threat,insult,identity_hate) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    text,
                    result["toxic"],
                    result["severe_toxic"],
                    result["obscene"],
                    result["threat"],
                    result["insult"],
                    result["identity_hate"]
                )
            )

            connection.commit()

    def get_all(self):
        #Return all prediction results

        with sqlite3.connect(self.database_path) as connection:
            return pd.read_sql_query("SELECT * FROM results", connection)