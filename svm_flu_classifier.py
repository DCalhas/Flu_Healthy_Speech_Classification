# Imports
import numpy as np
from sklearn import svm,metrics
from sklearn.decomposition import PCA, KernelPCA

pca = PCA(n_components=0.9999999)
# CSV File Parsers
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


# Function to train the model
def train_model(data,labels,C=1.0, kernel='rbf', degree=3, gamma='auto', coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, max_iter=-1, decision_function_shape='ovr', random_state=None):
    
    model = svm.SVC(C=C, 
                    kernel=kernel,
                    degree=degree,
                    gamma=gamma,
                    coef0=coef0, 
                    shrinking=shrinking,
                    probability=probability,
                    tol=tol, 
                    cache_size=cache_size,
                    class_weight=class_weight,
                    max_iter=max_iter, 
                    decision_function_shape=decision_function_shape, 
                    random_state=random_state)
    pca.fit(data)
    x_data = pca.transform(data)
    model.fit(x_data,labels)  
                            
    return model

# Function to test the model
def test_model(data, labels, test_data, trained_model):
    x_data = pca.transform(data)
    predicted_labels = trained_model.predict(x_data)
    rounded_labels = np.clip(np.abs(np.round(predicted_labels)), 0, 1)

    predicted_test_labels = trained_model.predict(pca.transform(test_data))
    rounded_test_labels = np.clip(np.abs(np.round(predicted_test_labels)), 0, 1)

    print("DEV LABELS")
    for i in range(len(rounded_labels)):
        print(rounded_labels[i])
    print("TEST LABELS")
    for i in range(len(rounded_test_labels)):
        print(rounded_test_labels[i])
    f1 = metrics.precision_recall_fscore_support(labels,rounded_labels, labels=[0,1], average='macro')

    return f1, predicted_labels


def main():
    
    #gemaps
    #train_files = ('data_sets/train_features_gemaps.csv', 'labels_train.txt')
    #dev_files = ('data_sets/dev_features_gemaps.csv', 'labels_dev.txt')
    
    #egemaps
    train_files = ('data_sets/train_features_egemaps_norm.csv', 'labels_train.txt')
    dev_files = ('data_sets/dev_features_egemaps_norm.csv', 'labels_dev.txt')
    test_files = ('data_sets/dev_features_egemaps_norm.csv')
    #mfcc
    #train_files = ('data_sets/features_MFCC_train.csv', 'labels_train.txt')
    #dev_files = ('data_sets/features_MFCC_dev.csv', 'labels_dev.txt')
    
    #IS13
    #train_files = ('data_sets/train_features_IS13.csv', 'labels_train.txt')
    #dev_files = ('data_sets/dev_features_IS13.csv', 'labels_dev.txt')

    ## Load Data using Parsers
    
    # Training Data
    train_data = parse_data(train_files[0])
    train_labels = parse_labels(train_files[1])
    
    # Development Data
    dev_data = parse_data(dev_files[0])
    dev_labels = parse_labels(dev_files[1])
        
    test_data = parse_data(test_files)
    # Train Model
    model = train_model(train_data, train_labels,
                        C=30000, 
                        kernel='rbf', 
                        degree=2, 
                        gamma='auto',  
                        tol=1e-8)
    
    # Get metrics for the development set
    f1, predicted_labels = test_model(dev_data, dev_labels, test_data, model)
    
    print("Precision:", f1[0])
    print("Recall:", f1[1])
    print("F1 Score:", f1[2])
    print("Support:", f1[3])
    
    return
    
if __name__ == "__main__":
    main()
