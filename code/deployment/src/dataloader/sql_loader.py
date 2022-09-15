import pandas as pd
import pyodbc
from ..utils import logger

server = ''
database = ''
username = ''
password = ''
driver = '{ODBC Driver 17 for SQL Server}'


def get_training_data():
    conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server +
                          ';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = conn.cursor()
    cursor.execute(
        'SELECT * FROM Table'
    )
    rows = cursor.fetchall()
    column_names = [col[0] for col in cursor.description]
    rows = [list(row) for row in rows]
    data = pd.DataFrame(rows, columns=column_names)
    conn.close()

    return data


def get_scoring_data():
    pass
