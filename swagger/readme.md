## Homework by
- Ravinder Lambadi, hid-sp18-514
- Orly Eseban, hid-sp18-506
# Swagger REST API - Manage S&P 500 Pricing Data in the Database

This API provides operations like get all S&P pricing data, filter data by date, delete data by date, update data by date, and insert pricing details in he database using HTTP methods such as GET, PUT, PATCH and DELETE.

### Prerequiste

1. Make sure below database and table is created
    - Database
      ```sh
       SWAGGERAPIDB
       ```
    - Table
      ```sh
       SNP_PRICE_DETAILS
       ``` 
     - SQL Query To Create Table
       ```sh
       CREATE TABLE SNP_PRICE_DETAILS(id MEDIUMINT NOT NULL AUTO_INCREMENT, Date DATE, Open FLOAT, High FLOAT, Low FLOAT, Close FLOAT,  AdjClose FLOAT, Volume BIGINT, PRIMARY KEY (id))
       ```  
2. Download S&P 500 pricing data from below web site and save into the above DB Table.
     - S&P 500 Data
       ```sh
       https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC
        ``` 
### Installation Steps
1. Open a terminal window and change directory to the folder you want to install the service in.
2. Run the commands below to clone my Git repository to your machine and the navigate to the swagger folder: 
    ```sh
    git clone https://github.com/cloudmesh-community/hid-sp18-514.git
    cd hid-sp18-514/swagger
    ```
3. Additional steps can then be performed by excuting the Makefile using the usage parameters below:
    -  Installing the sevice and dependencies
        ```sh
        make service
        ```
    -  Remove service and cleanup files
        ```sh
        make clean
        ```
    -  Start the service
        ```sh
        make start
        ```
    -  Stop the service
        ```sh
        make stop
        ```
    -  Test the service using GET, PUT, PATCH and DELETE curl calls:
        ```sh
        make test
        ```
    -  Create a Docker image and container named cloudmesh-snp-sql using Dockerfile:
        ```sh
        make container
        ```
    -  Run the Docker container named cloudmesh-snp-sql:
        ```sh
        make container_start
        ```
