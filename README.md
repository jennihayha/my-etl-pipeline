# My ETL Pipeline

This repository contains an ETL (_extract, transform, load_) pipeline that performs following tasks:

- extracting transactional data of ca. 400k invoices from Redshift
- transforming the data: identifying and removing duplicates, changing the data type of the invoice_date field to type datetime  
- loading the transformed data to an s3 bucket

## Requirements

The minimum requirements for running the code are as follows:

- Python 
- Docker for Mac: [Docker >= 20.10.2](https://docs.docker.com/desktop/install/mac-install/)
- Docker for Windows:
  - Installation: [Docker](https://docs.docker.com/desktop/install/windows-install/)
  - Manual installation for an older WSL version (_Windows Subsystem for Linux_): [Docker WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)

## Instructions on how to run the code







