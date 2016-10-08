import pandas as pd
import datetime

days = pd.read_csv('./data/QUIC_Dim_Day.csv', sep='\t')

days = days.drop(['SEASON_NAME'], axis=1)

def day_of_the_week(date_str):
    year, month, day  = (int(x) for x in date_str.split('-'))
    dt = datetime.date(year, month, day)
    return dt.weekday()

days['WEEKDAY'] = days['DAY_DATE'].apply(day_of_the_week)

days.to_csv('./data/QUIC_Dim_Day_digitised.csv', sep='\t')

