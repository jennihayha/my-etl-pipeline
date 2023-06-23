import psycopg2
import pandas as pd


def connect_to_redshift(dbname, host, port, user, password):

    connect = psycopg2.connect(
        dbname=dbname, host=host, port=port, user=user, password=password
    )

    print("Connection to redshift made")

    return connect


def extract_transactional_data(dbname, host, port, user, password):

    # connect to redshift
    # read the sql query:
    # add description to the online transactions table
    # remove the stock codes M, D, CRUK, POST, BANK, CHARGES
    # replace missing stock_description with "Unknown"
    # fix the data type of invoice_date to datetime

    # connect to redshift
    connect = connect_to_redshift(dbname, host, port, user, password)

    # read sql query
    query = """
    SELECT ot.invoice,
        ot.stock_code,
        CASE WHEN s.description is null THEN 'Unknown'
            ELSE s.description END AS description, 
        ot.price,
        ot.quantity,
        /* add a variable that gives the total order values */
        ot.price * ot.quantity AS total_order_value,
        CAST(invoice_date as datetime) as invoice_date,
        ot.customer_id,
        ot.country 
    FROM bootcamp.online_transactions ot
    LEFT JOIN (SELECT *
            FROM bootcamp.stock_description
            WHERE description <> '?') AS s ON ot.stock_code = s.stock_code
    WHERE customer_id <> ''
    AND ot.stock_code NOT IN('BANK CHARGES', 'POST', 'D', 'M', 'CRUK')
    """

    online_trans_cleaned = pd.read_sql(query, connect)

    print(f"The shape of the extracted and transformed data is {online_trans_cleaned.shape}")

    return online_trans_cleaned