# Imports

# Import numpy for arrays
import numpy as np
from sklearn import preprocessing
# Keras Imports
from keras.models import Sequential            
from keras.layers import Dense, Activation, BatchNormalization, Dropout    # Layers
from keras import optimizers                # Optimization Algorithm

# Metrics Function
from sklearn.metrics import recall_score, precision_recall_fscore_support

####################################################################################################
# The following lines define the random seeds
# Using the same seeds allows the results to be reproducible at each run

from sklearn.decomposition import PCA, KernelPCA


import os
import random as rn
import tensorflow as tf
from keras import backend as K

def parse_data(file_name):

    # Input: File Path
    # Outputs: Data Array

    with open(file_name, 'r') as f:        # Open File
        data = []
        for line in f:
            line = line.rstrip('\n')    # Remove new line characters
            line = line.split(',')        # Split line by ',' obtaining a list of strings as a result

            sample = [float(value) for value in line] # For each string in the list cast as a float
            
            data.append(sample)            # Add to Data array
        
    return np.array(data)                # Return data as Numpy Array


def parse_labels(file_name):

    with open(file_name, 'r') as f:            # Open File
        labels = [int(line.rstrip('\n')) for line in f]    # For each line in the file, 
                                                            # remove new line characters and cast the remaning string as an int
    return np.array(labels)



train_files = ('data_sets/train_features_gemaps.csv', 'labels_train.txt')
dev_files = ('data_sets/dev_features_gemaps.csv', 'labels_dev.txt')
test_files = ('data_sets/test_features_gemaps.csv', 'labels_test.txt')

## Load Data using Parsers

# Training Data
train_data = parse_data(train_files[0])
# Development Data
dev_data = parse_data(dev_files[0])
test_data = parse_data(test_files[0])

data = np.concatenate((np.concatenate((train_data, dev_data), axis=0), test_data), axis=0)

scaled_zero = preprocessing.scale(data)

scaler = preprocessing.MaxAbsScaler()
data_maxabs = scaler.fit_transform(scaled_zero)


train_file_norm = open('data_sets/train_features_gemaps_norm.csv', 'w')
dev_file_norm = open('data_sets/dev_features_gemaps_norm.csv', 'w')
test_file_norm = open('data_sets/test_features_gemaps_norm.csv', 'w')
for i in range(len(data_maxabs)):
	if(i < 13000):
		last = 0
		for j in range(len(data_maxabs[i])-1):
			train_file_norm.write(str(data_maxabs[i][j]) + ",")
			last = j
		train_file_norm.write(str(data_maxabs[i][last+1]))
		train_file_norm.write('\n')
	elif(i < 16000):
		last = 0
		for j in range(len(data_maxabs[i])-1):
			dev_file_norm.write(str(data_maxabs[i][j]) + ",")
			last = j
		dev_file_norm.write(str(data_maxabs[i][last+1]))
		dev_file_norm.write('\n')

	else:
		last = 0
		for j in range(len(data_maxabs[i])-1):
			test_file_norm.write(str(data_maxabs[i][j]) + ",")
			last = j
		test_file_norm.write(str(data_maxabs[i][last+1]))
		test_file_norm.write('\n')

train_file_norm.close()
test_file_norm.close()
dev_file_norm.close()