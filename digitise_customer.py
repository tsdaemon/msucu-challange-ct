import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

customers = pd.read_csv('./data/QUIC_Dim_Customer_clean.csv', sep='\t')

# replace text representation with class
def replace_with_labels(dataset, column):
    le = LabelEncoder().fit(dataset[column])
    labels = le.transform(dataset[column])
    dataset[column] = labels

def replace_with_labels_and_save(dataset, column):
    le = LabelEncoder().fit(dataset[column])
    labels = le.transform(dataset[column])
    np.save('./data/' + column + '.npy', le.classes_)
    dataset[column] = labels

def replace_with_labels_load(dataset, column, filename):
    le = LabelEncoder().fit(dataset[column])
    le.classes_ = np.load('./data/' + filename + '.npy')
    labels = le.transform(dataset[column])
    dataset[column] = labels

replace_with_labels(customers, 'CUSTOMER_CTR')
replace_with_labels(customers, 'CUSTOMER_CTP')
replace_with_labels(customers, 'CUSTOMER_OMC')
replace_with_labels(customers, 'EMAILABLE')
replace_with_labels(customers, 'GENDER_CD')
replace_with_labels_and_save(customers, 'CITY_NM')
replace_with_labels_and_save(customers, 'PROVINCE_CD')
replace_with_labels(customers, 'COUNTRY_CD')

customers.to_csv('./data/QUIC_Dim_Customer_digitised.csv', sep='\t')

