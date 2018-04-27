## Project by
- Ravinder Lambadi, hid-sp18-514
- Orly Esteban, hid-sp18-506
# Please follow the below steps to test the Benford's Law verification.

### Prerequiste
1. Make sure python 2.7.13 or 3.6.4 is available
2. matplotlib will be installed when you follow the installation steps below.
3. Please follow the piazza link in case of any issues with matplotlin
	```sh
	https://piazza.com/class/jbkvbp3ed3m2ez?cid=431
	```
	
### Installation Steps
1. Open a terminal window and change directory to the folder you want to install the service in.
2. Run the commands below to clone my Git repository to your machine and the navigate to the project-code folder: 
    ```sh
    git clone https://github.com/cloudmesh-community/hid-sp18-514.git
    cd hid-sp18-514/project-code
    ```
3. Additional steps can then be performed by excuting the Makefile using the usage parameters below:
    -  Installing the sevice and dependencies
        ```sh
        make service
        ```
	- Edit .bashrc file and add the below entry and save it
		```sh
        alias ANA="pyenv activate anaconda3-4.3.1"
        ```
    -  Start the service
        ```sh
        make start
        ```
4. Testing
	- Once Python Eve server started. Open new terminal and navigate project-code folder and then perform rest of the steps.
	```sh
	cd hid-sp18-514/project-code
	 ```
	-  Download the excel file type dataset from data.gov to verify Benford's Law
	```sh
	curl -X GET 'http://localhost:5000/downloadDataSet?dataLocation=https://inventory.data.gov/dataset/67567804-073d-40ad-a710-2b0bed8b84e2/resource/360b0748-d161-4857-a7dc-dfccfaeea096/download/nsn-extract-4-5-17.xlsx&fileName=nsn-extract-4-5-17.xlsx'
    ```
	-  Benford's Law verification on excel file type dataset
	```sh
	curl -X GET 'http://localhost:5000/computeBenfordLawExcelDataSet?fileName=nsn-extract-4-5-17.xlsx&columnName=Price'
	```
	- Download the CSV file type dataset from data.gov to verify Benford's Law
	```sh
	curl -X GET 'http://localhost:5000/downloadDataSet?dataLocation=https://data.ok.gov/sites/default/files/res_purchase_card_%28pcard%29_fiscal_year_2014_3pcd-aiuu.csv&fileName=fiscal_year_2014.csv'
	```
	- Benford's Law verification on CSV file type dataset
	```sh
	curl -X GET 'http://localhost:5000/computeBenfordLawCSVDataSet?fileName=fiscal_year_2014.csv&columnName=Amount'
	```
5. Machine Leaning datase - Australian Credit Approval
	- Perform Benford's Law verification on Web dataset to detect the fraud on credit card dataset
	```sh
	curl -X GET 'http://localhost:5000/australianCreditApproalDS?dataURL=https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/australian/australian.dat&columnName=A2'
	```