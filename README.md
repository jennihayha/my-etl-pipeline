# My ETL Pipeline

This repository contains an ETL pipeline that performs following tasks:

- extracting transactional data of ca. 400k invoices from Redshift
- transforming the data: identifying and removing duplicates, changing the invoice_date field into datetime format 
- loading the transformed data to an s3 bucket

## Requirements

The minimum requirements for running the code are as follows:

- Python 
- Docker for Mac: [Docker >= 20.10.2](https://docs.docker.com/desktop/install/mac-install/)
- Docker for Windows:
  - Installation: [Docker](https://docs.docker.com/desktop/install/windows-install/)
  - Manual installation for an older WSL version (_Windows Subsystem for Linux_): [Docker WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)


## How to run the code

Copy the .env.example file to .env and fill out the environment variables.

Make sure you are executing the code from the etl_pipeline folder and that you have Docker Desktop running.

 1. To run it locally, first build the image:

    `docker image build -t etl-pipeline .`

 2. Then run the etl job using Docker:

    `docker run --env-file .env etl-pipeline`


