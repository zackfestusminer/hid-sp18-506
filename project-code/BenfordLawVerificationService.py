from eve import Eve

import numpy as np

import pandas as pd

import benford as bf

import matplotlib.pyplot as plt

import requests

from flask import request

app = Eve ()


# This function returns whether the column name is valid.
def isInputColumnNameValid(ds, column):
	if column in ds.columns.values:
    		return True
	else:
		return False

def findColumnCount(ds, column):
	return ds[column].count()

def isEmptyString(text):
	if not text:
		return True
	return False
		

@app.route('/downloadDataSet', methods=['GET'])	
def downloadDataSet():
	
	dataLocation = request.args.get('dataLocation')
	fileName = request.args.get('fileName')

	if isEmptyString(fileName) or isEmptyString(dataLocation):
		return "dataLocation or fileName is Empty"

	resp = requests.get(dataLocation)

	with open(fileName, 'wb') as output:
		output.write(resp.content)

	return "Dataset in a file:"+fileName+" got downloaded"


@app.route('/computeBenfordLawCSVDataSet', methods=['GET'])	
def computeBenfordLawCSVDataSet():
	fileName = request.args.get('fileName')
	column = request.args.get('columnName')
	ds = pd.read_csv(fileName)

	if isEmptyString(fileName) or isEmptyString(column):
		return "fileName or Column is Empty"
	
	# Check column name
	if(isInputColumnNameValid(ds,column) == False):
		return "Column:"+ column +" Does not exists in the dataset"
	else:
		if(findColumnCount(ds,column) > 0):

			simpleReturnCol = 'simpleReturn'+'_'+column
			logReturnCol = 'logReturn'+'_'+column

			ds[simpleReturnCol] = ds[column]/ds[column].shift()-1    
			ds[logReturnCol] = np.log(ds[column]/ds[column].shift())
	
			bf.first_digits(ds[logReturnCol], digs=1, decimals=8) # digs=1 for the first digit (1-9)

			return "Benford's Law Verification for the dataset in the file:"+fileName+"-"+"Complete"
		else:
			return "Data set is empty / Column" +"-"+ column + "-Does not have any data"


@app.route('/computeBenfordLawExcelDataSet', methods=['GET'])	
def computeBenfordLawExcelDataSet():
	fileName = request.args.get('fileName')
	column = request.args.get('columnName')
	
	if isEmptyString(fileName) or isEmptyString(column):
		return "fileName or Column is Empty"

	ds = pd.read_excel(fileName,skipinitialspace=True)

	# Check column name
	if(isInputColumnNameValid(ds,column) == False):
		return "Column:"+ column +" Does not exists in the dataset"
	else:
		if(findColumnCount(ds,column) > 0):
			simpleReturnCol = 'simpleReturn'+'_'+column
			logReturnCol = 'logReturn'+'_'+column
			ds[simpleReturnCol] = ds[column]/ds[column].shift()-1
			ds[logReturnCol] = np.log(ds[column]/ds[column].shift())

			bf.first_digits(ds[logReturnCol], digs=1, decimals=8) # digs=1 for the first digit (1-9)
			
			return "Benford's Law verification for the data set in the file:"+fileName +"-"+ "Complete"
			
		else:
			return "Data set is empty / Column" +"-"+ column + "-Does not have any data"



@app.route('/australianCreditApproalDS', methods=['GET'])	
def computeBenfordLawWebDataSetService():	
	dataURL = request.args.get('dataURL')
	column = request.args.get('columnName')
	
	if isEmptyString(dataURL) or isEmptyString(column):
		return "dataURL or Column is Empty"

	column_names = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15']

	dataset = pd.read_csv(dataURL,delim_whitespace=True,header=None);

	ds = pd.DataFrame(dataset.values, columns = column_names)

	# Check column name
	if(isInputColumnNameValid(ds,column) == False):
		return "Column:"+ column +" Does not exists in the dataset"
	else:
		if(findColumnCount(ds,column) > 0):
			simpleReturnCol = 'simpleReturn'+'_'+column
			logReturnCol = 'logReturn'+'_'+column
			ds[simpleReturnCol] = ds[column]/ds[column].shift()-1
			ds[logReturnCol] = np.log(ds[column]/ds[column].shift())
			bf.first_digits(ds[logReturnCol], digs=1, decimals=8) # digs=1 for the first digit (1-9)
			return "Benford's Law verification for Fraud Detection is complete."
		else:
			return "Data set is empty / Column" +"-"+ column + "-Does not have any data"



if __name__ == '__main__':
    app.run()
