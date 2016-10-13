import pandas as pd
import numpy as np


def clean_city_data(city):
    if isinstance(city, basestring):
        # first remove spaces
        city = city.strip()
        # and remove anything except symbols and digits
        city = filter(lambda x: x.isdigit() or x.isalpha(), city)
        return city
    else:
        return 'UNKNOWN'


# replace empty values in datasets
def replace_empty(dataset, column, empty):
    dataset.ix[dataset[column] == '  ', column] = empty


def get_timestamp(long):
    seconds = long%100
    long = (long - seconds)/100
    minutes = long%100
    long = (long - minutes)/100
    hours = long
    return hours*60**2+minutes*60+seconds


def get_timestamp2(str_t):
    hours = int(str_t[0:2])
    minutes = int(str_t[3:5])
    seconds = int(str_t[6:8])
    return hours*60**2+minutes*60+seconds


ctp = pd.read_csv('./data/QUIC_Fact_CTP.csv', sep='\t')
ctp['STORE_CITY'] = ctp['STORE_CITY'].apply(clean_city_data)
ctp['TRANSACTION_TM'] = ctp['TRANSACTION_TM'].apply(get_timestamp)
ctp.to_csv('./data/QUIC_Fact_CTP_clean.csv', sep='\t')
del ctp

ctr = pd.read_csv('./data/QUIC_Fact_CTR.csv', sep='\t')
ctr['STORE_CITY'] = ctr['STORE_CITY'].apply(clean_city_data)
ctr['TRANSACTION_TM'] = ctr['TRANSACTION_TM'].apply(get_timestamp2)
ctr.to_csv('./data/QUIC_Fact_CTR_clean.csv', sep='\t')
del ctr

omc = pd.read_csv('./data/QUIC_Fact_OMC.csv', sep='\t')
omc.ix[omc['MERCHANT_CITY'] == np.nan, 'MERCHANT_CITY'] = ''
omc['MERCHANT_CITY'] = omc['MERCHANT_CITY'].apply(clean_city_data)
omc.to_csv('./data/QUIC_Fact_OMC_clean.csv', sep='\t')
del omc

customers = pd.read_csv('./data/QUIC_Dim_Customer.csv', sep='\t')
replace_empty(customers, 'EMAILABLE', 'N')
replace_empty(customers, 'COUNTRY_CD', 'CA')
customers['CITY_NM'] = customers['CITY_NM'].apply(clean_city_data)
customers.to_csv('./data/QUIC_Dim_Customer_clean.csv', sep='\t')
del customers
