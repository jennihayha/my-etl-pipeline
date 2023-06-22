import os
from datetime import datetime
from src.extract import extract_transactional_data
from src.transform import identify_and_remove_duplicates
from src.load import df_to_s3

# cdfrom dotenv import load_dotenv
# load_dotenv()

# import variables from .env file
dbname = os.getenv("dbname")
host = os.getenv("host")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("password")
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key_id = os.getenv("aws_secret_access_key_id")

# track the time when script was executed
start_time = datetime.now()

# make connection to redshift, extract data with sql
print("Extracting and transforming data in SQL")
online_transaction_cleaned = extract_transactional_data(dbname, host, port, user, password)

# remove duplicated data
print("Removing duplicated data")
online_transaction_no_dupl = identify_and_remove_duplicates(online_transaction_cleaned)


# load to s3
print("Loading data to s3")
s3_bucket = "waia-data-dump"
key = "bootcamp2/etl/jh_online_trans_cleaned.csv"

df_to_s3(online_transaction_no_dupl, key, s3_bucket, aws_access_key_id, aws_secret_access_key_id)

# calculates how long it takes to run the script
execution_time = datetime.now() - start_time
print(f"\nTotal execution time (hh:mm:ss.ms) {execution_time}")