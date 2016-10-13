import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy import stats, integrate

ctp = pd.read_csv('./data/QUIC_Fact_CTP_clean.csv', sep='\t')
customers = pd.read_csv('./data/QUIC_Dim_Customer_clean.csv', sep='\t')
days = pd.read_csv('./data/QUIC_Dim_Day_digitised.csv', sep='\t')

dataset = pd.merge(ctp, customers, on='CUSTOMER_ID')
dataset = pd.merge(dataset, days, on='DAY_ID')


# time activity
def time_activity():
    transaction_per_time = []
    for i in range(24):
        start = i*60**2
        end = (i+1)*60**2
        transactions = len(dataset[(dataset.TRANSACTION_TM > start) & (dataset.TRANSACTION_TM < end)])
        transaction_per_time.append(transactions)

    plt.plot(transaction_per_time)
    plt.show()


def time_petroleum():
    petro_per_time = []
    for i in range(24):
        start = i*60**2
        end = (i+1)*60**2
        petro = dataset[(dataset.TRANSACTION_TM > start) & (dataset.TRANSACTION_TM < end)].PETRO_SPEND.sum()
        petro_per_time.append(petro)

    plt.plot(petro_per_time)
    plt.show()


def gender():
    f, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    g_dt = dataset.groupby(['GENDER_CD'])
    x = ['Men', 'Women', 'Unknown']

    y1 = g_dt['PETRO_SPEND'].mean()
    sb.barplot(x, y1, palette="RdBu_r", ax=ax1)
    ax1.set_ylabel("Petroleum mean")

    y2 = g_dt['CUSTOMER_AGE'].mean()
    sb.barplot(x, y2, palette="BuGn_d", ax=ax2)
    ax2.set_ylabel("Age mean")

    plt.show()


def transaction_time_distribution(df):
    sb.distplot(df.TRANSACTION_TM, kde=False, fit=stats.gamma)
    plt.show()


def store_city_by_season_num(df):
    return

transaction_time_distribution(dataset)

