#!/usr/bin/python3

import numpy as np


dataset=[11,10,12,14,15,13,15,102,12,14,107,10,10,13,12,14,108,12,11,12,15,15,11,10,12,14,15,13,15,14,12,13,20,12,25]


# Formula z= (Observations - Mean)/Standard Deviation

outliers=[]

def detect_outliers(data):

	threshold = 3         #Within 3rd SD it is not an outlier 
	mean = np.mean(data)
	std=np.std(data)
	
	for i in data: 
		z_score = (i - mean) / std	
		if np.abs(z_score) > threshold:
			outliers.append(i)
	return outliers

O=detect_outliers(dataset)
print(O)
