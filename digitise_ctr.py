import pandas as pd
from sklearn.preprocessing import LabelEncoder

ctr = pd.read_csv('./data/QUIC_Fact_CTR.csv', sep='\t')
customers = pd.read_csv('./data/QUIC_Dim_Customer.csv', sep='\t')
days = pd.read_csv('./data/QUIC_Dim_Day_digitised.csv', sep='\t')

# first clean datasets separately
def clean_city_data(city):
    # first remove spaces
    city = city.strip()
    # and remove anything except symbols and digits
    city = filter(lambda x: x.isdigit() or x.isalpha(), city)
    return city

ctr['STORE_CITY'] = ctr['STORE_CITY'].apply(clean_city_data)
customers['CITY_NM'] = customers['CITY_NM'].apply(clean_city_data)

# replace empty values in datasets
def replace_empty(dataset, column, empty):
    dataset.ix[dataset[column] == '  ', column] = empty

replace_empty(customers, 'EMAILABLE', 'N')
replace_empty(customers, 'COUNTRY_CD', 'CA')

# then join
dataset = pd.merge(ctr, customers, on='CUSTOMER_ID')

# replace text representation with class
def replace_with_labels(dataset, column):
    le = LabelEncoder().fit(dataset[column])
    labels = le.transform(dataset[column])
    dataset[column] = labels

def replace_with_labels_multycolumn(dataset, columns):
    le = LabelEncoder().fit([y for x in dataset[columns].get_values() for y in x])
    for c in columns:
        labels = le.transform(dataset[c])
        dataset[c] = labels

replace_with_labels_multycolumn(dataset, ['STORE_CITY','CITY_NM'])
replace_with_labels_multycolumn(dataset, ['STORE_PROV','PROVINCE_CD'])
replace_with_labels(dataset, 'STORE_ONSITE_PETRO')
replace_with_labels(dataset, 'DIVISION_CD')
replace_with_labels(dataset, 'DIVISION_NM')
replace_with_labels(dataset, 'AUTO_INVOICE')
replace_with_labels(dataset, 'REG_PROMO')
replace_with_labels(dataset, 'COUNTRY_CD')
replace_with_labels(dataset, 'CUSTOMER_CTR')
replace_with_labels(dataset, 'CUSTOMER_CTP')
replace_with_labels(dataset, 'CUSTOMER_OMC')
replace_with_labels(dataset, 'EMAILABLE')
replace_with_labels(dataset, 'GENDER_CD')

dataset = pd.merge(dataset, days, on='DAY_ID')

dataset.to_csv('./data/QUIC_Fact_CTR_joined_digitised.csv', sep='\t')

