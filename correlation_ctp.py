import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

ctp = pd.read_csv('./data/QUIC_Fact_CTP_joined_digitised.csv', sep='\t')

del ctp['STORE_PROV']  # STORE_PROV and STORE_CITY correllate as shit, cant guess why
del ctp['STORE_CITY']  # the same about customer city and store city
del ctp['PROVINCE_CD']
del ctp['COUNTRY_CD']
corr = ctp.corr()

sns.set(style="white")
f, ax = plt.subplots(figsize=(12, 12))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr, cmap=cmap, vmax=.3,
            square=True, xticklabels=2, yticklabels=2,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)
plt.show()

corr.to_csv('./data/QUIC_Fact_CTP_correlation.csv', sep='\t')
#  1 CUSTOMER_CTP -> EMAILABLE negative correlation
#  2 STORE_CITY -> SEASON_NUM negative correlation