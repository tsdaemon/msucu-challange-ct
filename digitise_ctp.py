import pandas as pd
from sklearn.preprocessing import LabelEncoder

ctp = pd.read_csv('./data/QUIC_Fact_CTP_clean.csv', sep='\t')
customers = pd.read_csv('./data/QUIC_Dim_Customer_clean.csv', sep='\t')
days = pd.read_csv('./data/QUIC_Dim_Day_digitised.csv', sep='\t')

# then join
dataset = pd.merge(ctp, customers, on='CUSTOMER_ID')

# replace text representation with class
def replace_with_labels(dataset, column):
    le = LabelEncoder().fit(dataset[column])
    labels = le.transform(dataset[column])
    dataset[column] = labels

def replace_with_labels_multycolumn(dataset, columns):
    v = dataset[columns].get_values().ravel()
    le = LabelEncoder().fit(v)
    for c in columns:
        labels = le.transform(dataset[c])
        dataset[c] = labels

replace_with_labels_multycolumn(dataset, ['STORE_CITY','CITY_NM'])
replace_with_labels_multycolumn(dataset, ['STORE_PROV','PROVINCE_CD'])
replace_with_labels(dataset, 'COUNTRY_CD')
replace_with_labels(dataset, 'CUSTOMER_CTR')
replace_with_labels(dataset, 'CUSTOMER_CTP')
replace_with_labels(dataset, 'CUSTOMER_OMC')
replace_with_labels(dataset, 'EMAILABLE')
replace_with_labels(dataset, 'GENDER_CD')

dataset = pd.merge(dataset, days, on='DAY_ID')
del dataset['Unnamed: 0_y']
del dataset['Unnamed: 0_x']

dataset.to_csv('./data/QUIC_Fact_CTP_joined_digitised.csv', sep='\t', index=False)

